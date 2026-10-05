# Lecture — 2026-10-05 · ML Week 1: micrograd + Géron + gold start

> **Option A, Week 1 of 10** (Mon 5 – Sat 10 Oct 2026). Today covers the **09:00–12:00** and **19:00–22:00** EAT ML blocks.
> **Notes and prompts only. No solutions.** You write all the exercise code and every gold question yourself.

---

## 1. Goal for today

**Morning (09–12): understand backprop and build it**
- Take the forward-only `Value` graph in `01-micrograd/` to a working `backward()`, and know *why* each step is correct.
- By 12:00 you should be able to explain on a whiteboard how a gradient moves from the root `e` back to the leaves `a` and `b`.

**Evening (19–22): see the ML landscape and start the eval set**
- Géron ch.1 (the ML landscape) and ch.2 (the end-to-end project checklist) at concept level, mapped to PyTorch.
- Learn what a gold set is and why RAG evals (RAGAS-style) need one.
- Start the **PDF inventory** for the PersonaLearn domain and draft the **first gold questions**. The week target is 20; tonight aim for 5–10.

---

## 2. Concepts

### (a) micrograd: from the `Value` graph to backprop (Karpathy path)

You've already built the **forward graph**. Every `Value` keeps `data`, its parents (`_prev`), and the op that made it (`_op`). Backprop adds the reverse pass.

- **Computation graph (DAG).** Nodes are scalars and edges are operations. The forward pass computes `data` from the leaves to the root.
- **Gradient (`grad`).** This is ∂(root)/∂(this node): how much the final output changes if you nudge this node a tiny bit. The root's own gradient is 1 by definition. Spend a minute on *why* that is.
- **Local derivative.** Each op only needs to know how its output changes with respect to its *direct* inputs. It knows nothing about the rest of the graph.
- **Chain rule.** Global gradient = (gradient flowing into the node from above) × (local derivative). Backprop applies this over and over, from the root back to the leaves.
- **`_backward` closure.** Each op node stores a small function that takes the node's `grad` and pushes the right amount into its parents' `grad`. You'll write these yourself.
- **Topological order.** You can only run a node's `_backward` once *all* the nodes that depend on it have finished. A topological sort of the DAG, run in reverse, gives you that order.
- **Accumulation.** If one node feeds into more than one place (e.g. `a` is used in both `c` and `d` in `explore.py`), its gradient is the **sum** of the contributions from each path. Think about what goes wrong if you assign instead of add.
- **Numerical check.** You can sanity-check any analytic gradient with a finite difference: nudge one leaf by a small h, re-run the forward pass, and compare. This is how you trust your own `backward()`.
- **From scalars to neurons.** A neuron is just a weighted sum plus a non-linearity, built from `Value` ops. Training is forward, then backward, then a small step against the gradient, then zeroing the gradients, then repeat. (Neuron/MLP is stretch work for later this week.)

**PyTorch mapping:** `Value` ≈ a 0-d `torch.Tensor` with `requires_grad=True`. `.backward()` and `.grad` mean the same thing. Zeroing gradients ≈ `optimizer.zero_grad()`.

### (b) Géron ch.1–2: concepts only, mapped to PyTorch

The book uses Scikit-Learn plus TensorFlow/Keras. Learn the **ideas**. When code comes up, ask yourself "what's the PyTorch / plain-Python equivalent?" and don't copy the Keras API.

**Ch.1: The ML landscape**
- What ML is: learning from data instead of hand-coding rules. When ML is the right tool, and when it isn't.
- Types of systems:
  - **Supervised / unsupervised / semi-supervised / self-supervised / reinforcement** learning.
  - **Batch vs online** learning.
  - **Instance-based vs model-based** learning.
- Main challenges:
  - **Data:** too little data, non-representative data, poor-quality data, irrelevant features.
  - **Model:** **overfitting** and **underfitting**.
- **Testing and validation:** train/validation/test splits, hyperparameter tuning, data mismatch, and the **No Free Lunch** idea.

**Ch.2: The end-to-end project checklist.** This is your mental template for every project, including PersonaLearn.
1. Look at the big picture: frame the problem, choose a performance measure, check your assumptions.
2. Get the data and **create a test set early, then leave it alone** (data snooping bias). Stratified sampling.
3. Explore and visualise to gain insight (correlations, attribute combinations).
4. Prepare the data: cleaning, handling text/categorical data, feature scaling, transformation pipelines.
5. Select and train a model. Evaluate with **cross-validation**, not just one split.
6. Fine-tune: grid or random search, ensembles, error analysis.
7. Present the solution.
8. Launch, monitor, and maintain (data drift, model rot).

**PyTorch mapping table**

| Géron idea | PyTorch / Python equivalent to look up yourself |
| --- | --- |
| `Pipeline` / transformers | plain functions, or `torchvision.transforms`-style composition |
| `fit` / `predict` | your own training loop: forward → loss → `backward()` → `optimizer.step()` |
| train/test split | `torch.utils.data.random_split` or a manual index split |
| Keras `Dataset` | `torch.utils.data.Dataset` + `DataLoader` |
| loss / metric | `torch.nn` losses; metrics computed by you or a small library |

### (c) Gold sets and why RAG evals matter

- **Gold set:** a small, carefully written set of questions, each with a reference answer and the source passage(s) that support it. It's your **fixed test set** for a RAG system, the Ch.2 "test set" idea applied to retrieval and generation.
- **Why it matters:** without a fixed set, every change to chunking, the embedding model, the prompt, or the LLM is just judged by feel. With one, every change produces a score you can compare.
- **What a good gold item has:** the question, a reference answer, the source document plus its page/section, and a question type (factual lookup, multi-hop, comparison, "not in corpus"/should-refuse) and difficulty.
- **RAG eval dimensions (RAGAS-style):**
  - **Retrieval quality:** context precision and context recall. Did you fetch the right passages, and did you fetch all of them?
  - **Generation quality:** faithfulness (is the answer grounded in the retrieved context?) and answer relevancy (does it actually answer the question?).
  - Reference-based checks compare against your gold answer.
- **LLM-as-judge caveat:** many metrics use an LLM to grade. They're useful but noisy. Your hand-written gold set is the anchor that keeps them honest.
- **Week 1 scope:** the first 20 gold questions plus an understanding of the metrics. Wiring up the harness comes in later weeks (`04-rag-evals/`, `evals/`).

### (d) PDF inventory for the PersonaLearn domain

- **Why:** you can't write gold questions, or build retrieval, until you know exactly what's in the corpus.
- **What to record per document:** title, file path, source/URL, licence or usage rights, page count, topic area, whether it's text-extractable or scanned (needs OCR), whether it has tables or figures, language, date/version, and a quality note.
- **Coverage thinking:** which PersonaLearn topics are well covered, which are thin, and which are missing? Gold questions should cover the whole spread, not just the easy PDF.
- **Hygiene:** don't commit copyrighted PDFs to a public repo. Commit the **inventory** (metadata) and keep the files local or in private storage.

---

## 3. Key terms glossary

| Term | Meaning (in your own words later) |
| --- | --- |
| Computation graph / DAG | Directed acyclic graph of ops, from leaves to root |
| Leaf node | An input or parameter, not produced by an op |
| Forward pass | Computing values from the leaves to the root |
| Backward pass / backprop | Computing gradients from the root to the leaves using the chain rule |
| Gradient | ∂(output)/∂(node) |
| Local derivative | Derivative of one op's output with respect to its direct inputs |
| Chain rule | Composes local derivatives into global ones |
| Topological sort | An ordering where each node comes after all of its inputs |
| Gradient accumulation | Summing gradient contributions over multiple paths |
| Finite-difference check | Numerical gradient estimate used to verify the analytic one |
| Supervised / unsupervised | Learning with labels vs without |
| Overfitting / underfitting | Too complex and memorises noise / too simple and misses the signal |
| Generalisation | How well the model performs on unseen data |
| Train / validation / test set | Fit / tune / final honest estimate |
| Data snooping bias | Peeking at the test set and making biased choices because of it |
| Cross-validation | Repeated train/validate over folds for a more stable estimate |
| Stratified sampling | A split that keeps the proportions of key categories |
| Gold set | Fixed, human-curated eval questions + reference answers + sources |
| Faithfulness | The answer is supported by the retrieved context |
| Answer relevancy | The answer addresses the question |
| Context precision / recall | Retrieved passages are relevant / all needed passages were retrieved |
| LLM-as-judge | Using an LLM to score outputs |
| Corpus inventory | Metadata catalogue of the source documents |

---

## 4. Common pitfalls

**micrograd**
- Setting gradients with `=` instead of accumulating with `+=`, which breaks any node that's used more than once.
- Forgetting to set the root's gradient before the backward pass starts.
- Calling `_backward` in the wrong order (no topological sort, or not reversed).
- Mixing Python floats and `Value`s without wrapping them, or forgetting the reflected ops (`__radd__`, `__rmul__`) when the float is on the left.
- Not zeroing gradients between training steps (they keep accumulating).
- Trusting `backward()` without a numerical check.
- Watching the video passively. Pause and type every step yourself.

**Géron**
- Getting stuck on TF/Keras API details. Focus on concepts and map them to PyTorch.
- Looking at the test set during exploration (data snooping).
- Using accuracy on skewed data. Pick the performance measure deliberately.
- Fitting scalers/transforms on the full dataset instead of on the training data only (leakage).

**Gold / evals / inventory**
- Writing questions only from the easiest PDF, or only simple factual lookups.
- Leaving out source/page references, which makes retrieval impossible to grade.
- Questions that give away exact phrases from the passage, so retrieval looks better than it is.
- No "not answerable from corpus" items, so you never test refusal.
- Committing copyrighted PDFs or any secrets/.env to the public repo.
- Trying to install and configure a whole eval framework in Week 1. Concepts plus gold first.

---

## 5. Morning block plan (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–09:10 | Warm-up: run `01-micrograd/explore.py` and re-read `value.py`. Write a three-line recap of the forward graph in `notes/2026-10-05.md`. |
| 09:10–09:50 | Karpathy micrograd video: the derivative intuition and manual backprop sections. Pause often and work the steps on paper. |
| 09:50–10:00 | Break (stand up, away from the screen). |
| 10:00–10:45 | Implement the backward pass in `value.py` yourself (see prompts M2–M4). |
| 10:45–11:15 | Verify with numerical gradients (M5). Extend the ops (M6). |
| 11:15–11:45 | Stretch: neuron/tanh (M7), or more video if you're behind. |
| 11:45–12:00 | Commit your own code. Write notes: what clicked, what's still fuzzy. |

**Exercise prompts (you write everything):**
- **M1.** On paper, draw the graph for `e = (a + b) * (a * b)` with a=2, b=3. Label each node's `data`. Then, by hand, work out ∂e/∂ every node using only local derivatives and the chain rule.
- **M2.** For `+` and for `*`, work out the local derivatives yourself. Then add a `_backward` closure to each op in `value.py` that pushes gradient into its parents.
- **M3.** Write a function that returns the nodes of the graph in topological order. Decide how to avoid visiting a node twice.
- **M4.** Implement `Value.backward()` using M3 and M2. Run it on the M1 graph and compare the result with your paper answers.
- **M5.** Write a small finite-difference checker. For each leaf, compare the numerical gradient with `.grad`. Decide on a tolerance and justify it in your notes.
- **M6.** Add at least: negation, subtraction, power by a constant, and the reflected ops so that `2 * a` and `1 + a` work. Re-check with M5.
- **M7 (stretch).** Add `tanh` (or `exp` + division) and build a single neuron `o = tanh(w1*x1 + w2*x2 + b)`. Back-propagate through it and check with M5.
- **M8 (stretch).** Rebuild the M1 or M7 expression in PyTorch with `requires_grad=True` and confirm that your gradients match.

---

## 6. Evening block plan (19:00–22:00 EAT)

> Hard stop at 22:00. 22:00–23:00 is review/planning, not study.

| Time | Activity |
| --- | --- |
| 19:00–19:05 | Re-read this morning's notes. Name one fuzzy point to come back to tomorrow. |
| 19:05–19:45 | Géron ch.1: skim, then take notes on the taxonomy, challenges, and test/validation. |
| 19:45–20:30 | Géron ch.2: walk through the 8-step checklist. Fill in the PyTorch mapping in your notes. |
| 20:30–20:40 | Break. |
| 20:40–21:05 | RAGAS quickstart and metric pages: read only, no setup rabbit-holes. Note what each metric needs as input. |
| 21:05–21:35 | PDF inventory: create the inventory table and fill in as many documents as you can. |
| 21:35–21:55 | Draft your first gold questions (aim for 5–10 tonight, toward 20 by Sat). |
| 21:55–22:00 | Commit (no PDFs, no secrets). Write down tomorrow's first task. |

**Exercise prompts (you write everything):**
- **E1.** In your own words, explain supervised vs unsupervised vs self-supervised, giving one PersonaLearn example of each. Where does a RAG system fit?
- **E2.** Pick one PersonaLearn ML problem. Answer Géron's ch.2 "big picture" questions for it: objective, how the output gets used, performance measure, assumptions.
- **E3.** For each of the 8 checklist steps, write one line on what it would look like in PyTorch or in a RAG pipeline.
- **E4.** Design the schema for your PDF inventory (columns of your choosing, informed by §2d). Create it in `gold/` or `notes/` as markdown or CSV and fill in the rows.
- **E5.** Design the schema for a gold item (fields of your choosing, informed by §2c). Write it at the top of your gold file.
- **E6.** Write your first gold questions **yourself** from the inventoried PDFs. Include a mix of types, and at least one that should *not* be answerable from the corpus.
- **E7.** For each RAGAS metric you read about, write one sentence on what it would catch in PersonaLearn and what it needs (question, answer, contexts, reference).

---

## 7. Self-check (answer in your notes; no answers here)

1. Why is a node's gradient the *sum* over all paths to the root, and what bug do you get if you forget that?
2. Why does backprop need the nodes in reverse topological order? What happens if you call `_backward` on a node before its consumers are done?
3. How would you convince a sceptic that your `backward()` is correct without trusting your own derivation?
4. In Géron's checklist, why create the test set so early, and what is data snooping bias?
5. What's the difference between faithfulness and context recall, and why can't either one replace a hand-written gold set?

---

## 8. Pointers

- **micrograd:** Karpathy, *"The spelled-out intro to neural networks and backpropagation: building micrograd"*, plus the micrograd repo. Watch first, type yourself, and only peek at the repo to compare *after* your version works.
- **Géron:** *Hands-On Machine Learning*, ch.1 (The ML Landscape) and ch.2 (End-to-End ML Project). Concepts only, mapped to PyTorch.
- **Evals:** **RAGAS** quickstart plus the metrics overview. (RAGAS only this week, not TruLens.)

## 9. Resources

- [Karpathy — building micrograd (YouTube)](https://www.youtube.com/watch?v=VMj-3S1tku0)
- [karpathy/micrograd (GitHub)](https://github.com/karpathy/micrograd)
- [Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
- [Géron — Hands-On ML, notebooks repo (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [Géron ch.2 notebook — end-to-end project](https://github.com/ageron/handson-ml3/blob/main/02_end_to_end_machine_learning_project.ipynb)
- [PyTorch — autograd tutorial](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics overview](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Week 1 checklist (5–10 Oct):* ☐ micrograd backprop ☐ Géron ch.1–2 ☐ eval basics ☐ PDF inventory ☐ 20 gold questions
