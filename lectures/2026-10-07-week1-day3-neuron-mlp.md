# Lecture — 2026-10-07 · Upskill week 1, day 3: neuron and a tiny MLP

> **Upskill week 1** (Mon 5 – Sat 10 Oct 2026), day 3. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the inventory rows, and every gold question.

Yesterday’s lecture: [`2026-10-06-week1-day2-micrograd-geron-gold.md`](2026-10-06-week1-day2-micrograd-geron-gold.md). The week targets do not change.

---

## 1. Goal for today

**Morning (09:00–12:00): one neuron you can trust, then one training step**
- A neuron built from your `Value` ops, with a non-linearity, whose weight gradients agree with Tuesday’s finite-difference check.
- One manual parameter step, including zeroing `.grad`.
- A tiny MLP only if that check is already green.

**Evening (19:00–22:00): Géron depth, RAGAS failure modes, inventory, gold**
- Géron **ch.1–2** in more depth: the performance measure, overfit versus underfit, and the test set you do not touch. One exercise for that cluster.
- **RAGAS** only: how a retrieval miss differs from a hallucination. Still no scores. Baseline RAG scores are **Upskill week 2**.
- Continue the PDF inventory and the gold set. Week target stays **20 by Sat 10 Oct**.

---

## 2. Where you are

Tuesday’s bar was `Value.backward()` in reverse topological order, gradients accumulated on the `explore.py` graph, a finite-difference check, and the missing scalar ops. The neuron was stretch, and only after that check passed.

The copy of `01-micrograd/value.py` on `main` is still the forward graph (`+` and `*`) plus a stub where `backward` will live. If your working copy already has Tuesday’s T2–T4, start at the neuron. If `backward()` is still empty or the numerical check is red, this morning is still Tuesday’s T2–T4. Do not stack a neuron on an unchecked backward pass.

This lecture does not re-teach the chain rule, topological order, or why `a` must accumulate. Those are Monday and Tuesday.

Upskill week 1 still open: micrograd backprop, Géron ch.1–2, eval basics, PDF inventory, first 20 gold questions.

---

## 3. Concepts to use (you derive the local derivatives; you do not paste them)

**Neuron**
- Inputs, weights, and a bias. Weights and bias are `Value` leaves you will step. Inputs are data leaves: they get gradients, and you do not step them.
- The pre-activation is a weighted sum plus the bias, built with the `+` and `*` you already have.
- The activation is `tanh`, or an `exp` you implement on `Value` and then shape into `tanh`. The output is one `Value`.
- `tanh` saturates: when the pre-activation is large in magnitude, the local slope flattens, so a large incoming gradient can arrive at the weights almost gone. Derive that local factor yourself. The board-length algebra is `slides later`.
- One training step is forward, backward from a scalar loss, a small step of each parameter against its `.grad`, then zero every `.grad` you own. Zeroing is part of the step. Say why, in one sentence, before you code it.
- The picture of one gradient splitting across a whole layer of neurons is `slides later`.

**Layer and MLP (stretch, not the bar)**
- A layer is several neurons that read the same inputs and each keep their own weights and bias.
- An MLP stacks layers. The outputs of one layer are the inputs of the next. Still only `Value` scalars.
- Today’s ceiling, if the neuron check is green: two inputs, two hidden neurons, one output. One forward, one backward, one parameter step, and the finite-difference check on a single hidden weight.
- A loss summed over a dataset, minibatches, and an optimizer object are outside today.

**Géron ch.1–2, depth (concepts).** Stay inside these two chapters. Tuesday’s G1 already placed a question in the taxonomy and walked the eight-step checklist. Today is three ideas from that same cluster:
- The performance measure is chosen with the decision, before any fit. Accuracy is a poor default when one outcome dominates, or when “a number came out” is not the decision you ship.
- Overfit means the model fits noise, including a sentence that appears once in a PDF. Underfit means the model is too weak for the signal you have. Ch.1 remedies to be able to name: more data, fewer or better features, a simpler model, regularization. You are not implementing a regularizer today.
- Ch.2 cuts the test set before exploration so later choices are not tuned to it (data snooping). This week the gold file is that test set. Adding questions you write is the work. Running a system on those questions and treating the number as a result is not.

**Eval basics (RAGAS).** Tuesday named context precision, context recall, faithfulness, and answer relevancy, and what each one reads. Today’s distinction: a retrieval miss and a hallucination are different failures. Faithfulness can look fine when the right passage was never retrieved, because the answer only had the passages it was given. Context recall is the check that notices the missing passage. Context precision notices junk that was retrieved even if the answer ignored it. Week 1 is still that vocabulary plus the gold set. Do not record scores. The metric formulas and the judge prompts are `slides later`.

**PDF inventory.** Same columns as Monday: title, path, source, licence, pages, topic, extractable vs scanned, tables or figures, language, version, quality note. Commit the inventory, not the PDFs. Leave a cell blank rather than guess.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on Tuesday’s check. If it is red, finish T2–T4. If it is green, build the neuron and check one weight. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | One training step with gradients zeroed. Tiny MLP only if the neuron check is green. |

**Prompts (you write the code):**
- **W1.** In `notes/`, one line: Tuesday’s finite-difference check is green, or it is not. If it is not, do Tuesday’s T2–T4 and do not start W2.
- **W2.** On paper, two inputs, two weights, one bias, then `tanh`. Mark every leaf you will step and every leaf you will not.
- **W3.** Implement the non-linearity on `Value`. Derive its local derivative yourself. Check one weight with the finite-difference method from Tuesday. Record `h`, the tolerance, and whether saturation would make a sloppy `h` lie.
- **W4.** Pick one made-up `(x, target)` pair. Build a scalar squared error between the neuron output and the target, using only `Value` ops. Take one parameter step. Run backward a second time without zeroing `.grad`, and write what changed. Then zero, and write the rule you will follow on every later step.
- **W5 (stretch).** Two hidden neurons and one output neuron. One forward, one backward, one step. Check one hidden weight with W3’s method. Stop. No data loader, no loop over a dataset.

Open the micrograd repo only after W3 passes. Do not paste its neuron.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Géron ch.1–2 depth (measure, fit, untouched test), then the single exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:15 | RAGAS: retrieval miss versus hallucination. No install, no second eval library. |
| 21:15–21:40 | PDF inventory: add rows for documents you actually have. Note one topic that is still thin. |
| 21:40–22:00 | Gold questions toward **20 by Sat 10 Oct**. If you have fewer than 10, this slot is writing items, not polishing the schema. Stop at 22:00. |

**Géron ch.1–2 — one exercise for the cluster**
- **G2.** Use one PersonaLearn question already in the gold file, or one you will add tonight. In your notes: (1) the performance measure you would ship, in a sentence a non-ML teammate would accept, and the measure you refuse, with the ch.1 reason; (2) whether the live risk is overfit, underfit, or a ch.1 data problem (too little, non-representative, poor quality, irrelevant features); (3) six short lines for the gold file as the ch.2 test set — where it lives, one feature you will not invent, how you would notice a model that memorised a PDF sentence, what you would simplify, what you would add data for, and the one thing you will not use the gold file to tune this week. Do not fit anything. Do not score anything.

**Eval, inventory, gold (prompts only):**
- **R4.** In notes, four cells: retrieval missed the passage, or the passage was there; the answer is grounded, or it is not. For each cell, one PersonaLearn sentence, and which of context recall or faithfulness fires. No numbers.
- **R5.** Write the line you will put above any future score table: no RAGAS scores in Upskill week 1. Under it, list the inputs a later run needs (question, answer, contexts, reference) and leave the judge prompt unread. Source: the RAGAS metrics pages you already opened.
- **R6.** Add inventory rows you can verify. One line on which topic is thin.
- **R7.** Append gold items you write yourself. Keep a mix of types, and keep at least one item the corpus should refuse. The week target stays 20 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Why does a second backward, without zeroing, change the parameter step?
2. What happens to a weight’s gradient when `tanh` is saturated, and how could that fool a finite-difference check?
3. Why is squared error on one made-up pair not the ch.2 test-set estimate?
4. Which RAGAS metric can look fine when retrieval missed the passage, and which one catches that miss?

---

## 7. Pointers

- **micrograd:** Karpathy, *building micrograd*, the neuron section, only after W3. Type it yourself.
- **Géron:** *Hands-On Machine Learning*, ch.1 and ch.2. Depth on the measure, fit, and the early test set. One exercise (G2). Not ch.3.
- **Evals:** **RAGAS** metrics overview. Upskill week 1 is eval basics. First baseline scores are Upskill week 2. Not TruLens.
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
