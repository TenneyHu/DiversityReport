# Output Diversity Classification — 20 Case Studies

Model: `gpt-5.4-mini`  •  Dataset: `test_set_papers_diversity.csv` (219 rows)

Categories: **TP** = gold yes, pred yes  •  **TN** = gold no, pred no  •  **FN** = gold yes, pred no  •  **FP** = gold no, pred yes

---

## Case 1 — [TP] (row 109)

**Title:** Bridging Information Gaps with Comprehensive Answers: Improving the Diversity and Informativeness of Follow-Up Questions

**Gold label:** `yes`  •  **Predicted:** `yes`

**Abstract:**

> Generating diverse follow-up questions that uncover missing information remains challenging for conversational agents, particularly when they run on small, locally hosted models. To tackle this problem, we develop an information-gap{--}driven pipeline that contrasts the initial answer with an LLM-generated comprehensive answer, identifies the information gaps, and formulates gap-bridging follow-up questions. Applying the pipeline, we augment an existing dataset{--}FollowupQG{--}tenfold. Experiments show that models fine-tuned on the augmented dataset achieve significantly higher informativeness and diversity than variations trained on the original dataset. These findings indicate that our pipeline, which mirrors the human cognitive process of information seeking, provides an efficient distillation channel from state-of-the-art LLMs to smaller models, enabling resource-constrained conversational systems to generate more diverse and informative follow-up questions.

---

## Case 2 — [TP] (row 69)

**Title:** One fish, two fish, but not the whole sea: Alignment reduces language models' conceptual diversity

**Gold label:** `yes`  •  **Predicted:** `yes`

**Abstract:**

> Researchers in social science and psychology have recently proposed using large language models (LLMs) as replacements for humans in behavioral research. In addition to arguments about whether LLMs accurately capture population-level patterns, this has raised questions about whether LLMs capture human-like conceptual diversity. Separately, it is debated whether post-training alignment (RLHF or RLAIF) affects models' internal diversity. Inspired by human studies, we use a new way of measuring the conceptual diversity of synthetically-generated LLM ``populations'' by relating the internal variability of simulated individuals to the population-level variability. We use this approach to evaluate non-aligned and aligned LLMs on two domains with rich human behavioral data. While no model reaches human-like diversity, aligned models generally display less diversity than their instruction fine-tuned counterparts. Our findings highlight potential trade-offs between increasing models' value alignment and decreasing the diversity of their conceptual representations.

---

## Case 3 — [TP] (row 120)

**Title:** Best Student Forcing: A Simple Training Mechanism in Adversarial Language Generation

**Gold label:** `yes`  •  **Predicted:** `yes`

**Abstract:**

> Language models trained with Maximum Likelihood Estimation (MLE) have been considered as a mainstream solution in Natural Language Generation (NLG) for years. Recently, various approaches with Generative Adversarial Nets (GANs) have also been proposed. While offering exciting new prospects, GANs in NLG by far are nevertheless reportedly suffering from training instability and mode collapse, and therefore outperformed by conventional MLE models. In this work, we propose techniques for improving GANs in NLG, namely Best Student Forcing (BSF), a novel yet simple adversarial training mechanism in which generated sequences of high quality are selected as temporary ground-truth to further train the generator. We also use an ensemble of discriminators to increase training stability and sample diversity. Evaluation shows that the combination of BSF and multiple discriminators consistently performs better than previous GAN approaches over various metrics, and outperforms a baseline MLE in terms of Fr ́ech ́et Distance, a recently proposed metric capturing both sample quality and diversity.

---

## Case 4 — [TP] (row 97)

**Title:** Benchmarking and Improving Text-to-{SQL} Generation under Ambiguity

**Gold label:** `yes`  •  **Predicted:** `yes`

**Abstract:**

> Research in Text-to-SQL conversion has been largely benchmarked against datasets where each text query corresponds to one correct SQL. However, natural language queries over real-life databases frequently involve significant ambiguity about the intended SQL due to overlapping schema names and multiple confusing relationship paths. To bridge this gap, we develop a novel benchmark called AmbiQT with over 3000 examples where each text is interpretable as two plausible SQLs due to lexical and/or structural ambiguity. When faced with ambiguity, an ideal top-$k$ decoder should generate all valid interpretations for possible disambiguation by the user. We evaluate several Text-to-SQL systems and decoding algorithms, including those employing state-of-the-art LLMs, and find them to be far from this ideal. The primary reason is that the prevalent beam search algorithm and its variants, treat SQL queries as a string and produce unhelpful token-level diversity in the top-$k$. We propose LogicalBeam, a new decoding algorithm that navigates the SQL logic space using a blend of plan-based template generation and constrained infilling. Counterfactually generated plans diversify templates while in-filling with a beam-search that branches solely on schema names provides value diversity. LogicalBeam is up to 2.5 times more effective than state-of-the-art models at generating all candidate SQLs in the top-$k$ ranked outputs. It also enhances the top-5 Exact and Execution Match Accuracies on SPIDER and Kaggle DBQA.

---

## Case 5 — [TP] (row 64)

**Title:** One world, one opinion? The superstar effect in {LLM} responses

**Gold label:** `yes`  •  **Predicted:** `yes`

**Abstract:**

> As large language models (LLMs) are shaping the way information is shared and accessed online, their opinions have the potential to influence a wide audience. This study examines who is predicted by the studied LLMs as the most prominent figures across various fields, while using prompts in ten different languages to explore the influence of linguistic diversity. Our findings reveal low diversity in responses, with a small number of figures dominating recognition across languages (also known as the ``superstar effect''). These results highlight the risk of narrowing global knowledge representation when LLMs are used to retrieve subjective information.

---

## Case 6 — [TN] (row 138)

**Title:** {D}iv{L}ogic{E}val: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models

**Gold label:** `no`  •  **Predicted:** `no`

**Abstract:**

> Logic reasoning in natural language has been recognized as an important measure of human intelligence for Large Language Models (LLMs). Popular benchmarks may entangle multiple reasoning skills and thus provide unfaithful evaluations on the logic reasoning skill. Meanwhile, existing logic reasoning benchmarks are limited in language diversity and their distributions are deviated from the distribution of an ideal logic reasoning benchmark, which may lead to biased evaluation results. This paper thereby proposes a new classical logic benchmark DivLogicEval, consisting of natural sentences composed of diverse statements in a counterintuitive way. To ensure a more reliable evaluation, we also introduce a new evaluation metric that mitigates the influence of bias and randomness inherent in LLMs. Through experiments, we demonstrate the extent to which logical reasoning is required to answer the questions in DivLogicEval and compare the performance of different popular LLMs in conducting logical reasoning.

---

## Case 7 — [TN] (row 199)

**Title:** {F}a{MTEB}: Massive Text Embedding Benchmark in {P}ersian Language

**Gold label:** `no`  •  **Predicted:** `no`

**Abstract:**

> In this paper, we introduce a comprehensive benchmark for Persian (Farsi) text embeddings, built upon the Massive Text Embedding Benchmark (MTEB). Our benchmark includes 63 datasets spanning seven different tasks: classification, clustering, pair classification, reranking, retrieval, summary retrieval, and semantic textual similarity. The datasets are a combination of existing, translated, and newly generated (synthetic) data, offering a diverse and robust evaluation framework for Persian language models. All newly translated and synthetic datasets were rigorously evaluated by both humans and automated systems to ensure high quality and reliability. Given the growing adoption of text embedding models in chatbots, evaluation datasets are becoming an essential component of chatbot development and Retrieval-Augmented Generation (RAG) systems. As a contribution, we include chatbot evaluation datasets in the MTEB benchmark for the first time. Additionally, we introduce the novel task of summary retrieval, which is not included in the standard MTEB tasks. Another key contribution of this work is the introduction of a substantial number of new Persian-language NLP datasets for both training and evaluation, many of which have no existing counterparts in Persian. We evaluate the performance of several Persian and multilingual embedding models across a wide range of tasks. This work presents an open-source benchmark with datasets, accompanying code, and a public leaderboard.

---

## Case 8 — [TN] (row 59)

**Title:** Inverse Reinforcement Learning Meets Large Language Model Alignment

**Gold label:** `no`  •  **Predicted:** `no`

**Abstract:**

> In the era of Large Language Models (LLMs), alignment has emerged as a fundamental yet challenging problem in the pursuit of more reliable, controllable, and capable machine intelligence. The recent success of reasoning models and conversational AI systems has underscored the critical role of reinforcement learning (RL) in enhancing these systems, driving increased research interest at the intersection of RL and LLM alignment.This tutorial will provide a comprehensive review of recent advances in LLM alignment through the lens of inverse reinforcement learning (IRL), emphasizing the distinctions between RL techniques employed in LLM alignment and those in conventional RL tasks. In particular, we highlight the necessity of constructing neural reward models from human data and discuss the formal and practical implications of this paradigm shift. The tutorial will begin with fundamental concepts in RL to provide a foundation for the audience unfamiliar with the field. We then examine recent advances in this research agenda, discussing key challenges and opportunities in conducting IRL for LLM alignment. Beyond methodological considerations, we explore practical aspects, including datasets, benchmarks, evaluation metrics, infrastructure, and computationally efficient training and inference techniques.Finally, we draw insights from the literature on sparse-reward RL to identify open questions and potential research directions. By synthesizing findings from diverse studies, we aim to provide a structured and critical overview of the field, highlight unresolved challenges, and outline promising future directions for improving LLM alignment through RL and IRL techniques.

---

## Case 9 — [TN] (row 98)

**Title:** Cross-Cultural Transfer of Commonsense Reasoning in {LLM}s: Evidence from the {A}rab World

**Gold label:** `no`  •  **Predicted:** `no`

**Abstract:**

> Large language models (LLMs) often reflect Western-centric biases, limiting their effectiveness in diverse cultural contexts. Although some work has explored cultural alignment, the potential for cross-cultural transfer, using alignment in one culture to improve performance in others, remains underexplored. This paper investigates cross-cultural transfer of commonsense reasoning within the Arab world, where linguistic and historical similarities coexist with local cultural differences. Using a culturally grounded commonsense reasoning dataset covering 13 Arab countries, we evaluate lightweight alignment methods such as in-context learning (ICL) and demonstration-based reinforcement (DITTO), alongside baselines like supervised fine-tuning (SFT) and direct preference Optimization (DPO). Our results show that merely 12 culture-specific examples from one country can improve performance in others by 10{\%} on average, within multilingual models. In addition, we demonstrate that out-of-culture demonstrations from Indonesia and US contexts can match or surpass in-culture alignment for MCQ reasoning, highlighting cultural commonsense transferability beyond Arab world. These findings demonstrate that efficient cross-cultural alignment is possible and offer a promising approach to adapt LLMs to low-resource cultural settings.

---

## Case 10 — [TN] (row 15)

**Title:** Culture is Everywhere: A Call for Intentionally Cultural Evaluation

**Gold label:** `no`  •  **Predicted:** `no`

**Abstract:**

> The prevailing ``trivia-centered paradigm'' for evaluating the cultural alignment of large language models (LLMs) is increasingly inadequate as these models become more advanced and widely deployed. Existing approaches typically reduce culture to static facts or values, testing models via multiple-choice or short-answer questions that treat culture as isolated trivia. Such methods neglect the pluralistic and interactive realities of culture, and overlook how cultural assumptions permeate even ostensibly ``neutral'' evaluation settings.In this position paper, we argue for intentionally cultural evaluation: an approach that systematically examines the cultural assumptions embedded in all aspects of evaluation, not just in explicitly cultural tasks. We systematically characterize the what, how, and circumstances by which culturally contingent considerations arise in evaluation, and emphasize the importance of researcher positionality for fostering inclusive, culturally aligned NLP research. Finally, we discuss implications and future directions for moving beyond current benchmarking practices, discovering important applications that we don{'}t know exist, and involving communities in evaluation design through HCI-inspired participatory methodologies.

---

## Case 11 — [FN] (row 55)

**Title:** {L}im{R}ank: Less is More for Reasoning-Intensive Information Reranking

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Existing approaches typically rely on large-scale fine-tuning to adapt LLMs for information reranking tasks, which is computationally expensive. In this work, we demonstrate that modern LLMs can be effectively adapted using only minimal, high-quality supervision. To enable this, we design LIMRANK-SYNTHESIZER, a reusable and open-source pipeline for generating diverse, challenging, and realistic reranking examples. Using this synthetic data, we fine-tune our reranker model, LIMRANK. We evaluate LIMRANK on two challenging benchmarks, i.e., BRIGHT for reasoning-intensive retrieval and FollowIR for instruction-following retrieval. Our experiments demonstrate that LIMRANK achieves competitive performance, while being trained on less than 5{\%} of the data typically used in prior work. Further ablation studies demonstrate the effectiveness of LIMRANK-SYNTHESIZER and the strong generalization capabilities of LIMRANK across downstream tasks, including scientific literature search and retrieval-augmented generation for knowledge-intensive problem solving.

---

## Case 12 — [FN] (row 213)

**Title:** {PERSONA}: A Reproducible Testbed for Pluralistic Alignment

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> The rapid advancement of language models (LMs) necessitates robust alignment with diverse user values. However, current preference optimization approaches often fail to capture the plurality of user opinions, instead reinforcing majority viewpoints and marginalizing minority perspectives. We introduce PERSONA, a reproducible test bed designed to evaluate and improve pluralistic alignment of LMs. We procedurally generate diverse user profiles from US census data, resulting in 1,586 synthetic personas with varied demographic and idiosyncratic attributes. We then generate a large-scale evaluation dataset containing 3,868 prompts and 317,200 feedback pairs obtained from our synthetic personas. Leveraging this dataset, we systematically evaluate LM capabilities in role-playing diverse users, verified through human judges, and the establishment of both a benchmark, PERSONA Bench, for pluralistic alignment approaches as well as an extensive dataset to create new and future benchmarks.

---

## Case 13 — [FN] (row 46)

**Title:** What did you say? Generating Child-Directed Speech Questions to Train {LLM}s

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Child-Directed Speech (CDS) holds unique linguistic properties that distinguish it from other types of textual corpora. Language models trained using CDS often obtain superior results compared with the same size of different types of data. Several studies have aimed at modifying non-CDS data to mimic its linguistic properties to match the hypothesized advantageous aspects of CDS. Here, we propose to adapt the non-CDS portions of the training data to include questions similar to CDS interaction. We modify the data by adding artificially generated questions to the data and methodically analyzing the change in performance using each modified dataset. Our results show that artificial question generation strongly depends on the properties of the original dataset. While the performance improves for question-related measures, the overall performance is negatively affected as a result of the reduced syntactic diversity.

---

## Case 14 — [FN] (row 0)

**Title:** {MURI}: High-Quality Instruction Tuning Datasets for Low-Resource Languages via Reverse Instructions

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> Instruction tuning enhances large language models (LLMs) by aligning them with human preferences across diverse tasks. Traditional approaches to create instruction tuning datasets face serious challenges for low-resource languages due to their dependence on data annotation. This work introduces a novel method, Multilingual Reverse Instructions (MURI), which generates high-quality instruction tuning datasets for low-resource languages without requiring human annotators or pre-existing multilingual models. Utilizing reverse instructions and a translation pipeline, MURI produces instruction-output pairs from existing human-written texts in low-resource languages. This method ensures cultural relevance and diversity by sourcing texts from different native domains and applying filters to eliminate inappropriate content. Our dataset, MURI-IT, includes more than 2 million instruction-output pairs across 200 languages. Evaluation by native speakers and fine-tuning experiments with mT5 models demonstrate the approach{'}s effectiveness for both NLU and open-ended generation. We publicly release datasets and models at https://github.com/akoksal/muri.

---

## Case 15 — [FN] (row 74)

**Title:** Bone Soups: A Seek-and-Soup Model Merging Approach for Controllable Multi-Objective Generation

**Gold label:** `yes`  •  **Predicted:** `no`

**Abstract:**

> User information needs are often highly diverse and varied. A key challenge in current research is how to achieve controllable multi-objective generation while enabling rapid adaptation to accommodate diverse user demands during test time. Existing solutions, such as Rewarded Soup, focus on merging language models individually tuned on single objectives. While easy to implement and widely used, these approaches face limitations in achieving optimal performance due to their disregard for the impacts of competing objectives on model tuning. To address this issue, we propose **Bone Soup**, a novel model merging approach that first seeks a series of back**bone** models by considering the impacts of multiple objectives and then makes the **soup** (i.e., merge the backbone models). Specifically, Bone Soup begins by training multiple backbone models for different objectives using multi-objective reinforcement learning. Each backbone model is guided by a combination of backbone reward signals. To ensure that these models are optimal for the Pareto front, the backbone rewards are crafted by combining standard reward functions into basis vectors, which can then be modified through a rule-based construction method. Bone Soup leverages a symmetric circulant matrix mapping to generate the merging coefficients, which are used to merge the backbone models according to user preferences.Extensive experimental results demonstrate that Bone Soup exhibits strong controllability and Pareto optimality in controllable multi-objective generation, providing a more effective and efficient approach to addressing diverse user needs at test time.

---

## Case 16 — [FP] (row 2)

**Title:** {F}air{C}o{T}: Enhancing Fairness in Text-to-Image Generation via Chain of Thought Reasoning with Multimodal Large Language Models

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> In the domain of text-to-image generative models, biases inherent in training datasets often propagate into generated content, posing significant ethical challenges, particularly in socially sensitive contexts. We introduce FairCoT, a novel framework that enhances fairness in text-to-image models through Chain-of-Thought (CoT) reasoning within multimodal generative large language models. FairCoT employs iterative CoT refinement to systematically mitigate biases, and dynamically adjusts textual prompts in real time, ensuring diverse and equitable representation in generated images. By integrating iterative reasoning processes, FairCoT addresses the limitations of zero-shot CoT in sensitive scenarios, balancing creativity with ethical responsibility. Experimental evaluations across popular text-to-image systems{---}including DALL-E and various Stable Diffusion variants{---}demonstrate that FairCoT significantly enhances fairness and diversity without sacrificing image quality or semantic fidelity. By combining robust reasoning, lightweight deployment, and extensibility to multiple models, FairCoT represents a promising step toward more socially responsible and transparent AI-driven content generation.

---

## Case 17 — [FP] (row 178)

**Title:** Automated Progressive Red Teaming

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Ensuring the safety of large language models (LLMs) is paramount, yet identifying potential vulnerabilities is challenging. While manual red teaming is effective, it is time-consuming, costly and lacks scalability. Automated red teaming (ART) offers a more cost-effective alternative, automatically generating adversarial prompts to expose LLM vulnerabilities. However, in current ART efforts, a robust framework is absent, which explicitly frames red teaming as an effectively learnable task. To address this gap, we propose Automated Progressive Red Teaming (APRT) as an effectively learnable framework. APRT leverages three core modules: an Intention Expanding LLM that generates diverse initial attack samples, an Intention Hiding LLM that crafts deceptive prompts, and an Evil Maker to manage prompt diversity and filter ineffective samples. The three modules collectively and progressively explore and exploit LLM vulnerabilities through multi-round interactions. In addition to the framework, we further propose a novel indicator, Attack Effectiveness Rate (AER) to mitigate the limitations of existing evaluation metrics. By measuring the likelihood of eliciting unsafe but seemingly helpful responses, AER aligns closely with human evaluations. Extensive experiments with both automatic and human evaluations, demonstrate the effectiveness of APRT across both open- and closed-source LLMs. Specifically, APRT effectively elicits 54{\%} unsafe yet useful responses from Meta{'}s Llama-3-8B-Instruct, 50{\%} from GPT-4o (API access), and 39{\%} from Claude-3.5 (API access), showcasing its robust attack capability and transferability across LLMs (especially from open-source LLMs to closed-source LLMs). The code and seed data are available at \url{https://github.com/tjunlp-lab/APRT}.

---

## Case 18 — [FP] (row 177)

**Title:** Self-Instruct: Aligning Language Models with Self-Generated Instructions

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Large ``instruction-tuned'' language models (i.e., finetuned to respond to instructions) have demonstrated a remarkable ability to generalize zero-shot to new tasks. Nevertheless, they depend heavily on human-written instruction data that is often limited in quantity, diversity, and creativity, therefore hindering the generality of the tuned model. We introduce Self-Instruct, a framework for improving the instruction-following capabilities of pretrained language models by bootstrapping off their own generations. Our pipeline generates instructions, input, and output samples from a language model, then filters invalid or similar ones before using them to finetune the original model. Applying our method to the vanilla GPT3, we demonstrate a 33{\%} absolute improvement over the original model on Super-NaturalInstructions, on par with the performance of InstructGPT-001, which was trained with private user data and human annotations. For further evaluation, we curate a set of expert-written instructions for novel tasks, and show through human evaluation that tuning GPT3 with Self-Instruct outperforms using existing public instruction datasets by a large margin, leaving only a 5{\%} absolute gap behind InstructGPT-001. Self-Instruct provides an almost annotation-free method for aligning pre-trained language models with instructions, and we release our large synthetic dataset to facilitate future studies on instruction tuning.

---

## Case 19 — [FP] (row 114)

**Title:** Diversity is the Key: Enhancing {LLM}-based Post-processing for Automated Audio Captioning

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Automated Audio Captioning (AAC) is a multimodal task aimed at generating natural language descriptions of audio content. Previous studies have shown that LLMs can improve AAC performance by summarizing audio events based on a list of candidate captions, which are selected by an external reranker from those generated using Nucleus Sampling. However, the reranking process often selects overly similar captions, disregarding the original diversity of the sampled captions. In this work, we show that this diversity reflects the AAC model{'}s level of certainty and propose a lightweight candidate selection approach that preserves the initial diversity of the generated captions. This, in turn, enables an LLM to summarize the captions while considering the AAC model{'}s certainty in a few-shot setting. Experimental results demonstrate that our method outperforms previous post-processing techniques while being significantly faster.

---

## Case 20 — [FP] (row 149)

**Title:** Learning and Enforcing Context-Sensitive Control for {LLM}s

**Gold label:** `no`  •  **Predicted:** `yes`

**Abstract:**

> Controlling the output of Large Language Models (LLMs) through context-sensitive constraints has emerged as a promising approach to overcome the limitations of Context-Free Grammars (CFGs) in guaranteeing generation validity. However, such constraints typically require manual specification{---}a significant barrier demanding specialized expertise. We introduce a framework that automatically learns context-sensitive constraints from LLM interactions through a two-phase process: syntactic exploration to gather diverse outputs for constraint learning, followed by constraint exploitation to enforce these learned rules during generation. Experiments demonstrate that our method enables even small LLMs (1B parameters) to learn and generate with perfect constraint adherence, outperforming larger counterparts and state-of-the-art reasoning models. This work represents the first integration of context-sensitive grammar learning with LLM generation, eliminating manual specification while maintaining generation validity.

---

