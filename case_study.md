# Output Diversity Classification — 20 Error Case Studies

Model: `gpt-5.4-mini`  •  Dataset: `test_set_papers_diversity.csv` (219 rows)

Errors only: **FN** = gold yes, pred no (10 cases)  •  **FP** = gold no, pred yes (10 cases)

---

## Case 1 — [FN] (row 0)

**Title:** {MURI}: High-Quality Instruction Tuning Datasets for Low-Resource Languages via Reverse Instructions

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Instruction tuning enhances large language models (LLMs) by aligning them with human preferences across diverse tasks. Traditional approaches to create instruction tuning datasets face serious challenges for low-resource languages due to their dependence on data annotation. This work introduces a novel method, Multilingual Reverse Instructions (MURI), which generates high-quality instruction tuning datasets for low-resource languages without requiring human annotators or pre-existing multilingual models. Utilizing reverse instructions and a translation pipeline, MURI produces instruction-output pairs from existing human-written texts in low-resource languages. This method ensures cultural relevance and diversity by sourcing texts from different native domains and applying filters to eliminate inappropriate content. Our dataset, MURI-IT, includes more than 2 million instruction-output pairs across 200 languages. Evaluation by native speakers and fine-tuning experiments with mT5 models demonstrate the approach{'}s effectiveness for both NLU and open-ended generation. We publicly release datasets and models at https://github.com/akoksal/muri.

---

## Case 2 — [FN] (row 11)

**Title:** {W}at{ME}: Towards Lossless Watermarking Through Lexical Redundancy

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Text watermarking has emerged as a pivotal technique for identifying machine-generated text. However, existing methods often rely on arbitrary vocabulary partitioning during decoding to embed watermarks, which compromises the availability of suitable tokens and significantly degrades the quality of responses. This study assesses the impact of watermarking on different capabilities of large language models (LLMs) from a cognitive science lens. Our finding highlights a significant disparity; knowledge recall and logical reasoning are more adversely affected than language generation. These results suggest a more profound effect of watermarking on LLMs than previously understood. To address these challenges, we introduce Watermarking with Mutual Exclusion (WatME), a novel approach leveraging linguistic prior knowledge of inherent lexical redundancy in LLM vocabularies to seamlessly integrate watermarks. Specifically, WatME dynamically optimizes token usage during the decoding process by applying a mutually exclusive rule to the identified lexical redundancies. This strategy effectively prevents the unavailability of appropriate tokens and preserves the expressive power of LLMs. We provide both theoretical analysis and empirical evidence showing that WatME effectively preserves the diverse capabilities of LLMs while ensuring watermark detectability.

---

## Case 3 — [FN] (row 16)

**Title:** User Feedback Alignment for {LLM}-powered Exploration in Large-scale Recommendation Systems

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Exploration, the act of broadening user experiences beyond their established preferences, is challenging in large-scale recommendation systems due to feedback loops and limited signals on user exploration patterns. Large Language Models (LLMs) offer potential solutions by leveraging their world knowledge to recommend novel content outside these loops. A key challenge is aligning LLMs with user preferences while preserving their knowledge and reasoning. To enhance planning for new user interests using LLMs, this paper introduces a novel approach that combines hierarchical planning with LLM inference-time scaling. This method aims to improve recommendation relevancy without compromising novelty. We decouple novelty and user-alignment, training separate LLMs for each objective. We then scale up the novelty-focused LLM{'}s inference and select the best-of-n predictions using the user-aligned LLM. Live experiments demonstrate efficacy, showing significant gains in both user satisfaction (measured by watch activity and active user counts) and exploration diversity.

---

## Case 4 — [FN] (row 41)

**Title:** Fuse It More Deeply! A Variational Transformer with Layer-Wise Latent Variable Inference for Text Generation

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> The past several years have witnessed Variational Auto-Encoder{'}s superiority in various text generation tasks. However, due to the sequential nature of the text, auto-regressive decoders tend to ignore latent variables and then reduce to simple language models, known as the $\textit{KL vanishing}$ problem, which would further deteriorate when VAE is combined with Transformer-based structures. To ameliorate this problem, we propose Della, a novel variational Transformer framework. Della learns a series of layer-wise latent variables with each inferred from those of lower layers and tightly coupled with the hidden states by low-rank tensor product. In this way, Della forces these posterior latent variables to be fused deeply with the whole computation path and hence incorporate more information. We theoretically demonstrate that our method can be regarded as entangling latent variables to avoid posterior information decrease through layers, enabling Della to get higher non-zero KL values even without any annealing or thresholding tricks. Experiments on four unconditional and three conditional generation tasks show that Della could better alleviate KL vanishing and improve both quality and diversity compared to several strong baselines.

---

## Case 5 — [FN] (row 52)

**Title:** Improve Student{'}s Reasoning Generalizability through Cascading Decomposed {C}o{T}s Distillation

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Large language models (LLMs) exhibit enhanced reasoning at larger scales, driving efforts to distill these capabilities into smaller models via teacher-student learning.Previous works simply fine-tune student models on teachers' generated Chain-of-Thoughts (CoTs) data. Although these methods enhance in-domain (IND) reasoning performance, they struggle to generalize to out-of-domain (OOD) tasks.We believe that the widespread spurious correlations between questions and answers may lead the model to preset a specific answer which restricts the diversity and generalizability of its reasoning process.In this paper, we propose \textbf{Cas}cading Decomposed \textbf{Co}Ts \textbf{D}istillation (CasCoD) to address these issues by decomposing the traditional single-step learning process into two cascaded learning steps. Specifically, by restructuring the training objectives{---}removing the answer from outputs and concatenating the question with the rationale as input{---}CasCoD{'}s two-step learning process ensures that students focus on learning rationales without interference from the preset answers, thus improving reasoning generalizability. Extensive experiments demonstrate the effectiveness of CasCoD on both IND and OOD benchmark reasoning datasets

---

## Case 6 — [FN] (row 55)

**Title:** {L}im{R}ank: Less is More for Reasoning-Intensive Information Reranking

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Existing approaches typically rely on large-scale fine-tuning to adapt LLMs for information reranking tasks, which is computationally expensive. In this work, we demonstrate that modern LLMs can be effectively adapted using only minimal, high-quality supervision. To enable this, we design LIMRANK-SYNTHESIZER, a reusable and open-source pipeline for generating diverse, challenging, and realistic reranking examples. Using this synthetic data, we fine-tune our reranker model, LIMRANK. We evaluate LIMRANK on two challenging benchmarks, i.e., BRIGHT for reasoning-intensive retrieval and FollowIR for instruction-following retrieval. Our experiments demonstrate that LIMRANK achieves competitive performance, while being trained on less than 5{\%} of the data typically used in prior work. Further ablation studies demonstrate the effectiveness of LIMRANK-SYNTHESIZER and the strong generalization capabilities of LIMRANK across downstream tasks, including scientific literature search and retrieval-augmented generation for knowledge-intensive problem solving.

---

## Case 7 — [FN] (row 74)

**Title:** Bone Soups: A Seek-and-Soup Model Merging Approach for Controllable Multi-Objective Generation

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> User information needs are often highly diverse and varied. A key challenge in current research is how to achieve controllable multi-objective generation while enabling rapid adaptation to accommodate diverse user demands during test time. Existing solutions, such as Rewarded Soup, focus on merging language models individually tuned on single objectives. While easy to implement and widely used, these approaches face limitations in achieving optimal performance due to their disregard for the impacts of competing objectives on model tuning. To address this issue, we propose **Bone Soup**, a novel model merging approach that first seeks a series of back**bone** models by considering the impacts of multiple objectives and then makes the **soup** (i.e., merge the backbone models). Specifically, Bone Soup begins by training multiple backbone models for different objectives using multi-objective reinforcement learning. Each backbone model is guided by a combination of backbone reward signals. To ensure that these models are optimal for the Pareto front, the backbone rewards are crafted by combining standard reward functions into basis vectors, which can then be modified through a rule-based construction method. Bone Soup leverages a symmetric circulant matrix mapping to generate the merging coefficients, which are used to merge the backbone models according to user preferences.Extensive experimental results demonstrate that Bone Soup exhibits strong controllability and Pareto optimality in controllable multi-objective generation, providing a more effective and efficient approach to addressing diverse user needs at test time.

---

## Case 8 — [FN] (row 96)

**Title:** Cross-Lingual Transfer of Debiasing and Detoxification in Multilingual {LLM}s: An Extensive Investigation

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Recent generative large language models (LLMs) show remarkable performance in non-English languages, but when prompted in those languages they tend to express higher harmful social biases and toxicity levels. Prior work has shown that finetuning on specialized datasets can mitigate this behavior, and doing so in English can transfer to other languages. In this work, we investigate the impact of different finetuning methods on the model{'}s bias and toxicity, but also on its ability to produce fluent and diverse text. We reduce biases by finetuning on curated non-harmful text, but find only direct preference optimization to be effective for mitigating toxicity. The mitigation caused by applying these methods in English also transfers to non-English languages. We find evidence that the extent to which transfer takes place can be predicted by the amount of data in a given language present in the model{'}s pretraining data. However, this transfer of bias and toxicity mitigation often comes at the expense of decreased language generation ability in non-English languages, highlighting the importance of developing language-specific bias and toxicity mitigation methods.

---

## Case 9 — [FN] (row 166)

**Title:** Exploring In-context Example Generation for Machine Translation

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Large language models (LLMs) have demonstrated strong performance across various tasks, leveraging their exceptional in-context learning ability with only a few examples.Accordingly, the selection of optimal in-context examples has been actively studied in the field of machine translation.However, these studies presuppose the presence of a demonstration pool with human-annotated pairs, making them less applicable to low-resource languages where such an assumption is challenging to meet.To overcome this limitation, this paper explores the research direction of in-context example generation for machine translation.Specifically, we propose Demonstration Augmentation for Translation (DAT), a simple yet effective approach that generates example pairs without relying on any external resources.This method builds upon two prior criteria, relevance and diversity, which have been highlighted in previous work as key factors for in-context example selection.Through experiments and analysis on low-resource languages where human-annotated pairs are scarce, we show that DAT achieves superior translation quality compared to the baselines.Furthermore, we investigate the potential of progressively accumulating generated pairs during test time to build and reuse a demonstration pool. Our implementation is publicly available at https://github.com/aiclaudev/DAT.

---

## Case 10 — [FN] (row 213)

**Title:** {PERSONA}: A Reproducible Testbed for Pluralistic Alignment

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> The rapid advancement of language models (LMs) necessitates robust alignment with diverse user values. However, current preference optimization approaches often fail to capture the plurality of user opinions, instead reinforcing majority viewpoints and marginalizing minority perspectives. We introduce PERSONA, a reproducible test bed designed to evaluate and improve pluralistic alignment of LMs. We procedurally generate diverse user profiles from US census data, resulting in 1,586 synthetic personas with varied demographic and idiosyncratic attributes. We then generate a large-scale evaluation dataset containing 3,868 prompts and 317,200 feedback pairs obtained from our synthetic personas. Leveraging this dataset, we systematically evaluate LM capabilities in role-playing diverse users, verified through human judges, and the establishment of both a benchmark, PERSONA Bench, for pluralistic alignment approaches as well as an extensive dataset to create new and future benchmarks.

---

## Case 11 — [FP] (row 27)

**Title:** Augmenting Compliance-Guaranteed Customer Service Chatbots: Context-Aware Knowledge Expansion with Large Language Models

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Retrieval-based chatbots leverage human-verified Q{\&}A knowledge to deliver accurate, verifiable responses, making them ideal for customer-centric applications where compliance with regulatory and operational standards is critical. To effectively handle diverse customer inquiries, augmenting the knowledge base with ``similar questions'' that retain semantic meaning while incorporating varied expressions is a cost-effective strategy. In this paper, we introduce the Similar Question Generation (SQG) task for LLM training and inference, proposing context-aware approaches to enable comprehensive semantic exploration and enhanced alignment with source question-answer relationships. We formulate optimization techniques for constructing in-context prompts and selecting an optimal subset of similar questions to expand chatbot knowledge under budget constraints. Both quantitative and human evaluations validate the effectiveness of these methods, achieving a 92{\%} user satisfaction rate in a deployed chatbot system, reflecting an 18{\%} improvement over the unaugmented baseline. These findings highlight the practical benefits of SQG and emphasize the potential of LLMs, not as direct chatbot interfaces, but in supporting non-generative systems for hallucination-free, compliance-guaranteed applications.

---

## Case 12 — [FP] (row 37)

**Title:** ``What is the value of {templates}?'' Rethinking Document Information Extraction Datasets for {LLM}s

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> The rise of large language models (LLMs) for visually rich document understanding (VRDU) has kindled a need for prompt-response, document-based datasets. As annotating new datasets from scratch is labor-intensive, the existing literature has generated prompt-response datasets from available resources using simple templates. For the case of key information extraction (KIE), one of the most common VRDU tasks, past work has typically employed the template ``What is the value for the key?''. However, given the variety of questions encountered in the wild, simple and uniform templates are insufficient for creating robust models in research and industrial contexts. In this work, we present K2Q, a diverse collection of five datasets converted from KIE to a prompt-response format using a plethora of bespoke templates. The questions in K2Q can span multiple entities and be extractive or boolean. We empirically compare the performance of seven baseline generative models on K2Q with zero-shot prompting. We further compare three of these models when training on K2Q versus training on simpler templates to motivate the need of our work. We find that creating diverse and intricate KIE questions enhances the performance and robustness of VRDU models. We hope this work encourages future studies on data quality for generative model training.

---

## Case 13 — [FP] (row 119)

**Title:** {MP}2{D}: An Automated Topic Shift Dialogue Generation Framework Leveraging Knowledge Graphs

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Despite advancements in on-topic dialogue systems, effectively managing topic shifts within dialogues remains a persistent challenge, largely attributed to the limited availability of training datasets. To address this issue, we propose Multi-Passage to Dialogue (MP2D), a data generation framework that automatically creates conversational question-answering datasets with natural topic transitions. By leveraging the relationships between entities in a knowledge graph, MP2D maps the flow of topics within a dialogue, effectively mirroring the dynamics of human conversation. It retrieves relevant passages corresponding to the topics and transforms them into dialogues through the passage-to-dialogue method. Through quantitative and qualitative experiments, we demonstrate MP2D{'}s efficacy in generating dialogue with natural topic shifts. Furthermore, this study introduces a novel benchmark for topic shift dialogues, TS-WikiDialog. Utilizing the dataset, we demonstrate that even Large Language Models (LLMs) struggle to handle topic shifts in dialogue effectively, and we showcase the performance improvements of models trained on datasets generated by MP2D across diverse topic shift dialogue tasks.

---

## Case 14 — [FP] (row 134)

**Title:** {F}uzz{A}ug: Data Augmentation by Coverage-guided Fuzzing for Neural Test Generation

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Testing is essential to modern software engineering for building reliable software.Given the high costs of manually creating test cases,automated test case generation, particularly methods utilizing large language models,has become increasingly popular.These neural approaches generate semantically meaningful tests that are more maintainable compared with traditional automated testing methods such as fuzzing.However, the diversity and volume of unit tests in current datasets are limited, especially for newer but important languages.In this paper, we present a novel data augmentation technique, *FuzzAug*,that brings the benefits of fuzzing to large language models by incorporating valid testing semantics and providing diverse coverage-guided inputs.Doubling the size of training datasets,FuzzAug improves performance over the baselines significantly.This technique demonstrates the potential of introducing prior knowledge from dynamic software analysisto improve neural test generation,offering significant enhancements in this task.Our code is open-sourced at https://github.com/SecurityLab-UCD/FuzzAug.

---

## Case 15 — [FP] (row 135)

**Title:** The Literary Canons of Large-Language Models: An Exploration of the Frequency of Novel and Author Generations Across Gender, Race and Ethnicity, and Nationality

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Large language models (LLMs) are an emerging site for computational literary and cultural analysis. While such research has focused on applying LLMs to the analysis of literary text passages, the probabilistic mechanism used by these models for text generation lends them to also understanding literary and cultural trends. Indeed, we can imagine LLMs as constructing their own ``literary canons'' by encoding particular authors and book titles with high probability distributions around relevant words and text. This paper explores the frequency with which certain literary titles and authors are generated by a selection of popular proprietary and open-source models and compares it to existing conceptions of literary canon. It investigates the diversity of author mentions across gender, ethnicity, nationality as well as LLMs' ability to accurately report such characteristics. We demonstrate that the literary canons of popular large-language models are generally aligned with the Western literary canon in that they slightly prioritize male authors and overwhelmingly prioritize White American and British authors.

---

## Case 16 — [FP] (row 161)

**Title:** Enhanced Data Synthesis for {LLM} through Reasoning Structures Generated by Hierarchical {GF}low{N}et

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Large language models (LLMs) excel in problem-solving but require training data with diverse reasoning processes. Existing methods mainly optimize instruction-response pairs but lack a systematic design for the underlying reasoning structure. This paper proposes RSS: a Reasoning Structure driven data Synthesis method. We first proactively develop a hierarchical GFlowNet to construct reasoning structures efficiently through a coarse-to-fine directed acyclic graph (DAG) growth process. Then reasoning DAGs are leveraged to actively guide the instruction generation via an iterative suggester-editor workflow and enhance response quality using a structure-aware strategy. Experiments show that LLMs trained on our synthetic datasets achieve 48.50{\%}, 84.00{\%}, 79.90{\%} for AlpacaEval2, GSM8K and HumanEval, outperforming existing data synthesis methods.

---

## Case 17 — [FP] (row 168)

**Title:** Many Heads Are Better Than One: Improved Scientific Idea Generation by A {LLM}-Based Multi-Agent System

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> The rapid advancement of scientific progress requires innovative tools that can accelerate knowledge discovery. Although recent AI methods, particularly large language models (LLMs), have shown promise in tasks such as hypothesis generation and experimental design, they fall short of replicating the collaborative nature of real-world scientific practices, where diverse experts work together in teams to tackle complex problems. To address the limitations, we propose an LLM-based multi-agent system, i.e., Virtual Scientists (VIRSCI), designed to mimic the teamwork inherent in scientific research. VIRSCI organizes a team of agents to collaboratively generate, evaluate, and refine research ideas. Through comprehensive experiments, we demonstrate that this multi-agent approach outperforms the state-of-the-art method in producing novel scientific ideas. We further investigate the collaboration mechanisms that contribute to its tendency to produce ideas with higher novelty, offering valuable insights to guide future research and illuminating pathways toward building a robust system for autonomous scientific discovery. The code is available at https://github.com/open-sciencelab/Virtual-Scientists.

---

## Case 18 — [FP] (row 169)

**Title:** Multi-{LLM} Text Summarization

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> In this work, we propose a Multi-LLM summarization framework, and investigate two different multi-LLM strategies including centralized and decentralized. Our multi-LLM summarization framework has two fundamentally important steps at each round of conversation: generation and evaluation. These steps are different depending on whether our multi-LLM decentralized summarization is used or centralized. In both our multi-LLM decentralized and centralized strategies, we have k different LLMs that generate diverse summaries of the text. However, during evaluation, our multi-LLM centralized summarization approach leverages a single LLM to evaluate the summaries and select the best one whereas k LLMs are used for decentralized multi-LLM summarization. Overall, we find that our multi-LLM summarization approaches significantly outperform the baselines that leverage only a single LLM by up to 3x. These results indicate the effectiveness of multi-LLM approaches for summarization.

---

## Case 19 — [FP] (row 177)

**Title:** Self-Instruct: Aligning Language Models with Self-Generated Instructions

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Large ``instruction-tuned'' language models (i.e., finetuned to respond to instructions) have demonstrated a remarkable ability to generalize zero-shot to new tasks. Nevertheless, they depend heavily on human-written instruction data that is often limited in quantity, diversity, and creativity, therefore hindering the generality of the tuned model. We introduce Self-Instruct, a framework for improving the instruction-following capabilities of pretrained language models by bootstrapping off their own generations. Our pipeline generates instructions, input, and output samples from a language model, then filters invalid or similar ones before using them to finetune the original model. Applying our method to the vanilla GPT3, we demonstrate a 33{\%} absolute improvement over the original model on Super-NaturalInstructions, on par with the performance of InstructGPT-001, which was trained with private user data and human annotations. For further evaluation, we curate a set of expert-written instructions for novel tasks, and show through human evaluation that tuning GPT3 with Self-Instruct outperforms using existing public instruction datasets by a large margin, leaving only a 5{\%} absolute gap behind InstructGPT-001. Self-Instruct provides an almost annotation-free method for aligning pre-trained language models with instructions, and we release our large synthetic dataset to facilitate future studies on instruction tuning.

---

## Case 20 — [FP] (row 197)

**Title:** {ACLM}: A Selective-Denoising based Generative Data Augmentation Approach for Low-Resource Complex {NER}

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Complex Named Entity Recognition (NER) is the task of detecting linguistically complex named entities in low-context text. In this paper, we present ACLM Attention-map aware keyword selection for Conditional Language Model fine-tuning), a novel data augmentation approach based on conditional generation, to address the data scarcity problem in low-resource complex NER. ACLM alleviates the context-entity mismatch issue, a problem existing NER data augmentation techniques suffer from and often generates incoherent augmentations by placing complex named entities in the wrong context. ACLM builds on BART and is optimized on a novel text reconstruction or denoising task - we use selective masking (aided by attention maps) to retain the named entities and certain keywords in the input sentence that provide contextually relevant additional knowledge or hints about the named entities. Compared with other data augmentation strategies, ACLM can generate more diverse and coherent augmentations preserving the true word sense of complex entities in the sentence. We demonstrate the effectiveness of ACLM both qualitatively and quantitatively on monolingual, cross-lingual, and multilingual complex NER across various low-resource settings. ACLM outperforms all our neural baselines by a significant margin (1{\%}-36{\%}). In addition, we demonstrate the application of ACLM to other domains that suffer from data scarcity (e.g., biomedical). In practice, ACLM generates more effective and factual augmentations for these domains than prior methods.

---
