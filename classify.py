"""Classify papers in test_set_papers_diversity.csv with gpt-5.4-mini and score against gold labels."""
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
OUTPUT_CSV = "/Users/au805652/CLAN/Diversity/test_set_papers_diversity_pred.csv"
MODEL = "gpt-5.4-mini"
WORKERS = 16

SYSTEM_PROMPT = """You are an NLP/ML paper classifier.

TASK: Decide if a paper is about OUTPUT DIVERSITY — i.e., diversity of what a language model PRODUCES (text, code, responses, reasoning paths, synthetic data, etc.).

DEFAULT: If diversity of generated outputs is a core claim → "yes".

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
• Only multilingual coverage (no output diversity claim)
• Diversity only in training data for improving accuracy
• Bias/fairness/toxicity focus
• Annotator diversity (not model outputs)
• Utility diversity (e.g., distractors, retrieval)
• Dataset/resource papers without output diversity claims
• Personalization/controllability (targeting specific not diverse outputs)
• Data synthesis pipelines without diversity as a research focus

----------------------
DECISION:
----------------------
1. If audio/speech → no
2. If output diversity is clearly a contribution → yes
3. Otherwise → no
4. If unsure: "yes" only if diversity is a main claim about outputs

----------------------
OUTPUT:
----------------------
Return ONLY: {"label": "yes"} or {"label": "no"}
"""


def classify_one(client: OpenAI, title: str, abstract: str) -> str:
    user_msg = f"Title: {title}\n\nAbstract: {abstract}\n\nReturn JSON only."
    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
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


def main() -> None:
    df = pd.read_csv(INPUT_CSV)
    df = df[["title", "abstract", "label"]].copy()
    df["title"] = df["title"].fillna("")
    df["abstract"] = df["abstract"].fillna("")
    print(f"Rows: {len(df)}")
    print(f"Gold label distribution:\n{df['label'].value_counts()}\n")

    client = OpenAI()
    preds: list[str | None] = [None] * len(df)

    def task(idx: int) -> tuple[int, str]:
        return idx, classify_one(client, df.at[idx, "title"], df.at[idx, "abstract"])

    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(task, i) for i in df.index]
        for fut in as_completed(futures):
            idx, pred = fut.result()
            preds[idx] = pred
            done += 1
            if done % 25 == 0 or done == len(df):
                print(f"  {done}/{len(df)} done ({time.time() - t0:.1f}s)")

    df["pred"] = preds

    valid = df[df["pred"].isin(["yes", "no"])].copy()
    n_err = len(df) - len(valid)
    print(f"\nValid predictions: {len(valid)} / {len(df)}  (errors: {n_err})")

    y_true = valid["label"].tolist()
    y_pred = valid["pred"].tolist()

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label="yes", zero_division=0)
    rec = recall_score(y_true, y_pred, pos_label="yes", zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label="yes", zero_division=0)
    kappa = cohen_kappa_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred, labels=["yes", "no"])
    agreement = sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)

    print("\n=== Metrics (positive class = 'yes') ===")
    print(f"Accuracy           : {acc:.4f}")
    print(f"Precision          : {prec:.4f}")
    print(f"Recall             : {rec:.4f}")
    print(f"F1                 : {f1:.4f}")
    print(f"Cohen's kappa      : {kappa:.4f}")
    print(f"Raw agreement rate : {agreement:.4f}")
    print("\nConfusion matrix (rows=gold, cols=pred, order=[yes,no]):")
    print(cm)

    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved predictions to {OUTPUT_CSV}")

    summary = {
        "model": MODEL,
        "n_rows": len(df),
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
    with open("/Users/au805652/CLAN/Diversity/metrics.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Saved metrics to metrics.json")


if __name__ == "__main__":
    main()
