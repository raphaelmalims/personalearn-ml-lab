# Lecture — 2026-10-06 · Upskill week 1, day 2: micrograd + Géron + gold

> **Upskill week 1** (Mon 5 – Sat 10 Oct 2026), day 2. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **Notes and prompts only. No solutions.** You write the code, the inventory rows, and every gold question.

Yesterday’s lecture: [`2026-10-05-week1-micrograd-geron-gold.md`](2026-10-05-week1-micrograd-geron-gold.md). Continue from wherever that left `01-micrograd/value.py`. The week targets do not change.

---

## 1. Goal for today

**Morning (09:00–12:00): finish a trustworthy backward pass**
- `Value.backward()` runs in reverse topological order, accumulates gradients, and agrees with a finite-difference check on the graph in `explore.py`.
- If that already works, add the missing scalar ops and, only if time remains, one neuron.

**Evening (19:00–22:00): landscape, one Géron exercise, eval basics, inventory, gold**
- Géron **ch.1–2** at concept level (one exercise for the cluster).
- **RAGAS** only: what each metric needs, still no scores. Baseline RAG scores are **Upskill week 2**.
- Continue the PDF inventory and the gold set. Week target stays **20 by Sat 10 Oct**.

---

## 2. Where you are

`value.py` already builds a forward graph (`data`, `_prev`, `_op`) for `+` and `*`. `explore.py` builds `e = (a + b) * (a * b)` with `a = 2`, `b = 3`. `grad` exists and stays 0 until you fill the reverse pass.

Upskill week 1 still open after today: micrograd backprop, Géron ch.1–2, eval basics, PDF inventory, first 20 gold questions.

---

## 3. Concepts to use (do not look up the derivatives in a finished micrograd)

**Backprop, continued**
- Root gradient is 1 before any parent is updated. Say why, in one sentence, before you code.
- Each op’s `_backward` applies only the local derivative, multiplied by the gradient already sitting on that node.
- Visit nodes only after every consumer has pushed its contribution (reverse topological order).
- A node used twice (as `a` is) must **add** incoming gradients.
- A finite-difference check re-runs the forward pass with one leaf nudged. You choose `h` and the tolerance, and you write down why.
- A neuron is a weighted sum of `Value`s plus a non-linearity. Training one step is forward, backward, a small step against `grad`, then zero `grad`. That is stretch, not the bar for today.

**Géron ch.1–2 (concepts).** The book’s stack is Scikit-Learn and Keras. Keep the checklist; name a PyTorch or plain-Python stand-in when an API appears. Ch.1 is the taxonomy and the failure modes (data, overfit, underfit, the split). Ch.2 is the eight-step project checklist, especially a test set created early.

**Eval basics (RAGAS).** A gold item is a question, a reference answer, and the source passage. RAGAS-style checks you should be able to name by 22:00: context precision, context recall, faithfulness, answer relevancy. Each one needs a specific subset of question, answer, retrieved contexts, and reference. Week 1 is that vocabulary plus the gold set. Do not record scores tonight.

**PDF inventory.** One row per document: title, path, source, licence, pages, topic, extractable vs scanned, tables or figures, language, version, quality note. Commit the inventory, not the PDFs.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Backward pass on the `explore.py` graph, then a numerical check. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Missing scalar ops, then the neuron only if the check is green. |

If `backward()` is still empty at 09:00, stay on it through the break. Do not start the neuron until the numerical check matches.

**Prompts (you write the code):**
- **T1.** On paper, list an order in which `_backward` may run on `e`, `c`, `d`, `a`, and `b`. Mark the node that receives two contributions.
- **T2.** Implement `_backward` for `+` and `*` and `Value.backward()`. Compare `.grad` on `a` and `b` with the paper gradients from Monday’s M1. Fix your code until they match.
- **T3.** Write a finite-difference check for one leaf at a time. Record `h`, the tolerance, and one case that would make the check lie (step too large, or a non-smooth op).
- **T4.** Add negation, subtraction, power by a constant, and the reflected forms so a bare float can sit on the left. Re-run T3.
- **T5 (stretch).** One neuron: two inputs, two weights, one bias, `tanh` or an `exp` you built from `Value`. One manual training step. Check the weight gradients with T3 before you trust the step.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Géron ch.1–2, concepts only, then the single cluster exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:15 | RAGAS docs: metrics only. No install rabbit-hole, no second eval library. |
| 21:15–21:40 | PDF inventory: add rows for documents you actually have. |
| 21:40–22:00 | Gold questions toward **20 by Sat 10 Oct**. Stop at 22:00. |

**Géron ch.1–2 — one exercise for the cluster**
- **G1.** Pick one PersonaLearn question you might later put in the gold set. In your notes, place it in Géron’s ch.1 taxonomy (supervised or not, batch or online, instance-based or model-based) and say which ch.1 failure mode is the real risk. Then walk the same question down the ch.2 checklist in eight short lines: frame it, where the untouched test lives, what you would plot, how text becomes model input, what you would train, how you would know it failed, what you would tune, and what you would watch after launch. For each line, name the PyTorch, RAG, or gold-set object that plays that role. The gold set is the test set. Do not fit anything tonight.

**Eval, inventory, gold (prompts only):**
- **R1.** For context precision, context recall, faithfulness, and answer relevancy, write one line each: what it punishes in a PersonaLearn answer, and which of question / answer / contexts / reference it needs. Source: RAGAS docs.
- **R2.** Add inventory rows. Leave a row blank rather than guessing a licence or a page count.
- **R3.** Append gold items you write yourself. Mix at least two question types, and include one item the corpus should refuse. Keep the week target at 20 by Saturday; do not raise it.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Why does `a` in `explore.py` need its gradients added, and what number do you get if you assign instead?
2. What does your finite-difference check compare, and when would a passing check still hide a chain-rule bug?
3. In the G1 checklist, which step is the gold set, and why is that step early?
4. Which RAGAS metric can look fine when retrieval missed the passage, and which one catches that miss?

---

## 7. Pointers

- **micrograd:** continue Karpathy, *building micrograd*. Type the backward pass yourself. Open the micrograd repo only after T3 passes.
- **Géron:** *Hands-On Machine Learning*, ch.1 and ch.2. Concepts, one exercise (G1).
- **Evals:** **RAGAS** metrics overview. Upskill week 1 is eval basics. First baseline scores are Upskill week 2.
- **Gold:** 20 by Sat 10 Oct, then 30 by Sat 17 Oct, then 50 by Sat 24 Oct (see `gold/README.md`).

## 8. Resources

- [Karpathy — building micrograd (YouTube)](https://www.youtube.com/watch?v=VMj-3S1tku0)
- [karpathy/micrograd (GitHub)](https://github.com/karpathy/micrograd)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [PyTorch — autograd tutorial](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 1 (5–10 Oct):* ☐ micrograd backprop ☐ Géron ch.1–2 ☐ eval basics (RAGAS) ☐ PDF inventory ☐ 20 gold questions by Sat 10 Oct
