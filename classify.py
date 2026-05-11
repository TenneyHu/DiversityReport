"""Classify papers in test_set_papers_diversity.csv with gpt-5.4-mini and score against gold labels.

Runs three prompt variants separately and saves per-prompt predictions/metrics.
"""
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
from openai import OpenAI
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    cohen_kappa_score,
    confusion_matrix,
)

INPUT_CSV = "/Users/au805652/CLAN/Diversity/test_set_papers_diversity.csv"
OUTPUT_DIR = "/Users/au805652/CLAN/Diversity"
MODEL = "gpt-5.4-mini"
WORKERS = 16


PROMPT_1 = """You are an NLP/ML paper classifier.
TASK: Decide if a paper is about OUTPUT DIVERSITY — i.e., diversity of what a language model GENERATES (text, code, responses, reasoning paths, synthetic data, etc.).
DEFAULT: If diversity of generated outputs is a core part of the paper → "yes".
----------------------
ANSWER "yes" IF:
----------------------
• The paper explicitly studies or improves diversity of generated outputs:
 - Decoding/sampling diversity (e.g., diverse beam, MBR)
 - Generating diverse data (instructions, reasoning, stories, code, etc.)
 - Multi-agent / multi-perspective generation improving diversity
 - Pluralistic or multi-objective alignment producing varied outputs
 - Stylistic / lexical / persona diversity in outputs
 - Diverse candidate (MT, summarization, dialogue, etc.) / counterfactual information generation
 - Measuring or analyzing output diversity itself
----------------------
ANSWER "no" IF:
----------------------
• Speech/audio tasks (TTS, ASR, etc.)
• Vision models are part of the experiments
• Diversity only in training data for improving accuracy
• Annotator diversity (not model outputs)
• Dataset/resource papers without any analysis of the diversity of outputs
• Personalization/controllability (targeting specific not diverse outputs)
• Data synthesis pipelines without diversity in the output of models as a research focus

OUTPUT:
----------------------
Return ONLY: {"label": "yes"} or {"label": "no"}
"""


PROMPT_2 = """You are an NLP/ML paper classifier.

TASK:
Decide if a paper is about OUTPUT DIVERSITY — i.e., diversity of what a language model GENERATES (text, code, responses, reasoning paths, synthetic data, etc.).

CORE PRINCIPLE:
Answer "yes" if the paper's method, objective, or evaluation involves producing, improving, preserving, selecting, or analyzing VARIATION across model outputs.

If diversity is an intended effect (even if not the sole goal), answer "yes".


----------------------
ANSWER "yes" IF:
----------------------
• The paper explicitly targets diversity of generated outputs:
  - Diverse decoding/sampling (e.g., diverse beam search, MBR)
  - Generating multiple candidates and selecting among them (best-of-n, reranking for novelty/diversity)
  - Multi-agent / multi-perspective generation producing varied outputs
  - Pluralistic alignment or modeling diverse preferences/personas
  - Stylistic, lexical, semantic, or persona diversity in outputs
  - Measuring, analyzing, or preserving output diversity

• The method implicitly increases or preserves diversity of outputs:
  - Variational / latent-variable generation improving diversity
  - Methods preventing collapse, bias, or over-determinism in outputs
  - Exploration, novelty, or diversity in recommendations or generations
  - Reasoning diversity (e.g., multiple CoTs, removing answer bias)
  - Watermarking or constraints that preserve expressive diversity

• The paper generates synthetic data AND:
  - Emphasizes diversity/variety/coverage of generated outputs as a goal or key property
  - Uses diversity as a criterion in generation or evaluation

----------------------
ANSWER "no" IF:
----------------------
• Diversity is ONLY in training data (for robustness/accuracy), not model outputs
• Data generation/synthesis pipelines where diversity is incidental or not studied
• Dataset/resource papers without analysis of generated output diversity
• Personalization or controllability toward a SINGLE target output (not variety)
• Retrieval, ranking, or classification tasks without generating diverse outputs
• Multi-output generation exists BUT only one output is used and diversity is not analyzed
• Diversity refers ONLY to:
  - Annotators or human populations
  - Input questions/templates
  - Retrieved documents or knowledge sources
• The work focuses on:
  - Evaluation of distributions (e.g., bias, frequency of mentions) without generating diverse outputs as a goal
  - Systems that generate candidates but optimize only quality/accuracy (not diversity)
• Speech/audio tasks (TTS, ASR, etc.)
• Vision/multimodal tasks where text generation diversity is not the focus

----------------------
EDGE CASE RULES:
----------------------
• If multiple outputs are generated and USED (selection, comparison, exploration), this is usually "yes"
• If diversity is mentioned as a BENEFIT or METRIC of the method → "yes"
• If diversity is only a PROPERTY OF DATA (not outputs) → "no"
• When unsure: prefer "no" unless output diversity is clearly relevant

----------------------
OUTPUT:
----------------------
Return ONLY: {"label": "yes"} or {"label": "no"}
"""


PROMPT_3 = """You are an NLP/ML paper classifier.

TASK:
Decide if a paper is about OUTPUT DIVERSITY — i.e., diversity of what a language model GENERATES (text, code, responses, reasoning paths, synthetic data, etc.).

CORE PRINCIPLE:
Answer "yes" if the paper's method, objective, or evaluation involves producing, improving, preserving, selecting, or analyzing VARIATION across model outputs.

If diversity is an intended effect (even if not the sole goal), answer "yes".


----------------------
ANSWER "yes" IF:
----------------------
• The paper explicitly targets diversity of generated outputs:
  - Diverse decoding/sampling (e.g., diverse beam search, MBR)
  - Generating multiple candidates and selecting among them (best-of-n, reranking for novelty/diversity)
  - Multi-agent / multi-perspective generation producing varied outputs
  - Pluralistic alignment or modeling diverse preferences/personas
  - Stylistic, lexical, semantic, or persona diversity in outputs
  - Measuring, analyzing, or preserving output diversity

• The method implicitly increases or preserves diversity of outputs:
  - Variational / latent-variable generation improving diversity
  - Methods preventing collapse, bias, or over-determinism in outputs
  - Exploration, novelty, or diversity in recommendations or generations
  - Reasoning diversity (e.g., multiple CoTs, removing answer bias)
  - Watermarking or constraints that preserve expressive diversity

• The paper generates synthetic data AND:
  - Emphasizes diversity/variety/coverage of generated outputs as a goal or key property
  - Uses diversity as a criterion in generation or evaluation

----------------------
ANSWER "no" IF:
----------------------
• Diversity is ONLY in training data (for robustness/accuracy), not model outputs
• Data generation/synthesis pipelines where diversity is incidental or not studied
• Dataset/resource papers without analysis of generated output diversity
• Personalization or controllability toward a SINGLE target output (not variety)
• Retrieval, ranking, or classification tasks without generating diverse outputs
• Multi-output generation exists BUT only one output is used and diversity is not analyzed
• Diversity refers ONLY to:
  - Annotators or human populations
  - Input questions/templates
  - Retrieved documents or knowledge sources
• The work focuses on:
  - Evaluation of distributions (e.g., bias, frequency of mentions) without generating diverse outputs as a goal
  - Systems that generate candidates but optimize only quality/accuracy (not diversity)
• Speech/audio tasks (TTS, ASR, etc.)
• Vision/multimodal tasks where text generation diversity is not the focus

OUTPUT:
----------------------
Return ONLY: {"label": "yes"} or {"label": "no"}
"""


PROMPTS: dict[str, str] = {
    "prompt1": PROMPT_1,
    "prompt2": PROMPT_2,
    "prompt3": PROMPT_3,
}


def classify_one(client: OpenAI, system_prompt: str, title: str, abstract: str) -> str:
    user_msg = f"Title: {title}\n\nAbstract: {abstract}\n\nReturn JSON only."
    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg},
                ],
                response_format={"type": "json_object"},
            )
            content = resp.choices[0].message.content or ""
            obj = json.loads(content)
            label = str(obj.get("label", "")).strip().lower()
            if label in {"yes", "no"}:
                return label
            return "no"
        except Exception as e:
            if attempt == 3:
                print(f"  [error after retries] {e}")
                return "error"
            time.sleep(2 ** attempt)
    return "error"


def run_prompt(name: str, system_prompt: str, df: pd.DataFrame, client: OpenAI) -> dict:
    print(f"\n========== Running {name} ==========")
    preds: list[str | None] = [None] * len(df)

    def task(idx: int) -> tuple[int, str]:
        return idx, classify_one(client, system_prompt, df.at[idx, "title"], df.at[idx, "abstract"])

    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(task, i) for i in df.index]
        for fut in as_completed(futures):
            idx, pred = fut.result()
            preds[idx] = pred
            done += 1
            if done % 25 == 0 or done == len(df):
                print(f"  [{name}] {done}/{len(df)} done ({time.time() - t0:.1f}s)")

    out_df = df.copy()
    out_df["pred"] = preds

    valid = out_df[out_df["pred"].isin(["yes", "no"])].copy()
    n_err = len(out_df) - len(valid)
    print(f"\n[{name}] Valid predictions: {len(valid)} / {len(out_df)}  (errors: {n_err})")

    y_true = valid["label"].tolist()
    y_pred = valid["pred"].tolist()

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label="yes", zero_division=0)
    rec = recall_score(y_true, y_pred, pos_label="yes", zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label="yes", zero_division=0)
    kappa = cohen_kappa_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred, labels=["yes", "no"])
    agreement = sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)

    print(f"\n=== [{name}] Metrics (positive class = 'yes') ===")
    print(f"Accuracy           : {acc:.4f}")
    print(f"Precision          : {prec:.4f}")
    print(f"Recall             : {rec:.4f}")
    print(f"F1                 : {f1:.4f}")
    print(f"Cohen's kappa      : {kappa:.4f}")
    print(f"Raw agreement rate : {agreement:.4f}")
    print("Confusion matrix (rows=gold, cols=pred, order=[yes,no]):")
    print(cm)

    pred_path = os.path.join(OUTPUT_DIR, f"test_set_papers_diversity_pred_{name}.csv")
    metrics_path = os.path.join(OUTPUT_DIR, f"metrics_{name}.json")

    out_df.to_csv(pred_path, index=False)
    print(f"\nSaved predictions to {pred_path}")

    summary = {
        "prompt": name,
        "model": MODEL,
        "n_rows": len(out_df),
        "n_valid": len(valid),
        "n_errors": n_err,
        "accuracy": acc,
        "precision_yes": prec,
        "recall_yes": rec,
        "f1_yes": f1,
        "cohen_kappa": kappa,
        "agreement_rate": agreement,
        "confusion_matrix_yes_no": cm.tolist(),
    }
    with open(metrics_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved metrics to {metrics_path}")

    return summary


def main() -> None:
    df = pd.read_csv(INPUT_CSV)
    df = df[["title", "abstract", "label"]].copy()
    df["title"] = df["title"].fillna("")
    df["abstract"] = df["abstract"].fillna("")
    print(f"Rows: {len(df)}")
    print(f"Gold label distribution:\n{df['label'].value_counts()}\n")

    client = OpenAI()

    all_summaries: list[dict] = []
    for name, prompt in PROMPTS.items():
        summary = run_prompt(name, prompt, df, client)
        all_summaries.append(summary)

    combined_path = os.path.join(OUTPUT_DIR, "metrics_all_prompts.json")
    with open(combined_path, "w") as f:
        json.dump(all_summaries, f, indent=2)
    print(f"\nSaved combined metrics to {combined_path}")

    print("\n=== Summary across prompts ===")
    print(f"{'prompt':<10} {'acc':>8} {'prec':>8} {'rec':>8} {'f1':>8} {'kappa':>8}")
    for s in all_summaries:
        print(
            f"{s['prompt']:<10} {s['accuracy']:>8.4f} {s['precision_yes']:>8.4f} "
            f"{s['recall_yes']:>8.4f} {s['f1_yes']:>8.4f} {s['cohen_kappa']:>8.4f}"
        )


if __name__ == "__main__":
    main()
