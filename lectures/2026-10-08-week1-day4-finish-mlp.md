# Lecture — 2026-10-08 · Upskill week 1, day 4: close the tiny MLP

> **Upskill week 1** (Mon 5 – Sat 10 Oct 2026), day 4. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the inventory rows, and every gold question.

Yesterday’s lecture: [`2026-10-07-week1-day3-neuron-mlp.md`](2026-10-07-week1-day3-neuron-mlp.md). The week targets do not change.

---

## 1. Goal for today

**Morning (09:00–12:00): close the tiny MLP, then one shared weight**
- If Wednesday’s tiny MLP is still open, that is the bar: two inputs, two hidden neurons, one output, one step, one hidden-weight check.
- If that net is already green, do not rebuild it. Add two made-up pairs into one scalar loss, and watch the shared weight collect both contributions. At most one more step, with gradients zeroed.

**Evening (19:00–22:00): validation versus test, two more RAGAS names, inventory, gold**
- Géron **ch.1–2** in more depth: what you fit, what you tune, and the test set you report once. One exercise for that cluster.
- **RAGAS** only: answer relevancy and context precision, and why a judge is not the gold set. Still no scores. Baseline RAG scores are **Upskill week 2**.
- Continue the PDF inventory and the gold set. Week target stays **20 by Sat 10 Oct**.

---

## 2. Where you are

Wednesday’s bar was one neuron whose weight agreed with Tuesday’s finite-difference check, one parameter step that included zeroing `.grad`, and a 2–2–1 MLP only after that check was green. A loss over more than one example was outside Wednesday.

The copy of `01-micrograd/value.py` on `main` is still the forward graph (`+` and `*`) plus a stub where `backward` will live. If your working copy does not yet have a green neuron check and a finished one-step zeroing rule, this morning is still Wednesday’s W3–W4. Do not put a second example on a neuron you have not checked.

This lecture does not re-teach the chain rule, topological order, why `a` must accumulate, the local factor inside `tanh`, or the single-step zeroing demo. Those are Monday through Wednesday.

Upskill week 1 still open: micrograd backprop, Géron ch.1–2, eval basics, PDF inventory, first 20 gold questions.

---

## 3. Concepts to use (you derive anything local; you do not paste it)

**Close the MLP, then share a weight**
- Wednesday’s ceiling is today’s floor when the neuron check is green: two inputs, two hidden neurons, one output. Each hidden neuron keeps its own weights and bias. The hidden outputs are the inputs of the output neuron. Still only `Value` scalars.
- Check one hidden weight with the same finite-difference method as the neuron. The picture of one gradient splitting across the layer is still `slides later`.
- Two made-up pairs are enough after that check. Each pair has its own forward and its own scalar loss, built with the ops you already have. Add the two losses. Call `backward` on that sum.
- A weight both pairs use receives a contribution from each pair. That is Tuesday’s accumulation rule, now across examples. The board picture of those two paths meeting on one weight is `slides later`.
- Zero `.grad` before the backward that belongs to the next step. A second step on the same two pairs is the ceiling. No file of examples, no data loader, no optimizer object.

**Géron ch.1–2, depth (concepts).** Stay inside these two chapters. Tuesday’s G1 placed a question in the taxonomy and walked the eight-step checklist. Wednesday’s G2 chose a measure, named overfit versus underfit, and left the gold file untouched. Today is how those checklist rows are allowed to be used:
- Training rows are what you fit. Validation rows are what you use to choose: a model, a simpler model, a regularizer, or later a chunk size. Test rows are reported once, after those choices are frozen.
- Cross-validation repeats the train/validate cut when the tune set is small. Name it. Do not build folds today.
- Stratified sampling keeps a rare category inside each cut. In this gold file the rare category is an item the corpus should refuse.
- Leakage is a choice that used rows you promised not to look at. Fitting a transform on the full table is the ch.2 picture. Reading a gold answer while you design a chunker is the same mistake on text.
- Data mismatch means the rows you fit do not look like what you will ship. No Free Lunch means no single measure wins on every problem. Name both. Stay out of ch.3.

**Eval basics (RAGAS).** Wednesday separated a retrieval miss from a hallucination: context recall versus faithfulness. The other two names from Tuesday’s list:
- Answer relevancy asks whether the answer addresses the question. A grounded answer to a nearby question can leave faithfulness quiet and still fail relevancy.
- Context precision asks whether the retrieved passages were on the question. The right passage plus junk can still support a faithful answer. Precision is what notices the junk.
- An LLM judge is noisy. The hand-written gold items are the anchor. Week 1 is still that vocabulary plus the gold set. Do not record scores. The metric formulas and the judge prompts stay `slides later`.

**PDF inventory.** Same columns as Monday: title, path, source, licence, pages, topic, extractable vs scanned, tables or figures, language, version, quality note. Commit the inventory, not the PDFs. Leave a cell blank rather than guess.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on Wednesday. If the neuron check is red, finish W3–W4 and stop there. If it is green and the MLP is open, close the 2–2–1. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Only if the MLP check is green: two pairs, one summed loss, one shared-weight check, at most one more step. |

**Prompts (you write the code):**
- **Th1.** In `notes/`, three lines: Wednesday’s neuron check is green or not; the zeroing rule from W4 is written or not; the 2–2–1 exists or not. If the first line is “not”, do W3–W4 and do not start Th2.
- **Th2.** If the 2–2–1 is missing, build it. One forward, one backward, one parameter step, gradients zeroed. Check one hidden weight with Wednesday’s finite-difference method. Record `h`, the tolerance, and pass or fail. If Th2 fails, the rest of the morning is that check.
- **Th3.** Two made-up pairs you choose. A scalar loss on each, added into one scalar. Backward once. In notes, say whether the shared weight’s `.grad` matches what you get by treating each pair alone and combining those contributions yourself. Check that weight with Th2’s method.
- **Th4.** One more step on the same two pairs. Zero before that backward. Write the two loss values you observed, before and after the step, and stop. No loop over a file.

Open the micrograd repo only after Th2 passes. Do not paste its MLP.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Géron ch.1–2 depth (fit, tune, report once), then the single exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:15 | RAGAS: answer relevancy and context precision. No install, no second eval library. |
| 21:15–21:40 | PDF inventory: add rows for documents you actually have. Note one topic that is still thin. |
| 21:40–22:00 | Gold questions toward **20 by Sat 10 Oct**. If you have fewer than 15, this slot is writing items. Stop at 22:00. Do not write past 20 tonight. |

**Géron ch.1–2 — one exercise for the cluster**
- **G3.** Use one PersonaLearn question already in the gold file, or one you will add tonight. In your notes: (1) three lines for fit, tune, and report-once, and which of those the gold file is this week; (2) one later RAG choice (chunk size, how many passages, or the prompt) and the small set of questions you would tune it on, which is not the gold file; (3) one leakage path, a choice you could make by reading a gold answer, and the line you will not cross; (4) two sentences on whether a stratified cut matters for your question types, including refuse. Do not build folds. Do not fit anything. Do not score anything.

**Eval, inventory, gold (prompts only):**
- **R8.** Two PersonaLearn answers, both grounded in the same retrieved passage. One addresses the question. One addresses a nearby question. Which of faithfulness or answer relevancy separates them, and which stays quiet? No numbers.
- **R9.** One retrieved set: the right passage plus one irrelevant passage. Which metric notices the junk, and which of question / answer / contexts / reference it needs. No numbers.
- **R10.** One sentence on why an LLM judge does not replace the 20 gold items. Do not write a judge prompt.
- **R11.** Add inventory rows you can verify. Append gold items you write yourself until the file is moving toward 20. Keep a mix of types, and keep at least one item the corpus should refuse. The week target stays 20 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. When two pairs share a weight, what should that weight’s `.grad` be after one backward on the summed loss, and what does a second backward without zeroing do to it?
2. Why is the gold file the wrong place to choose a chunk size?
3. What is one leakage path in a text pipeline that peeks at a gold answer?
4. Which RAGAS metric can stay quiet when a grounded answer addresses the wrong question, and which one catches that?

---

## 7. Pointers

- **micrograd:** Karpathy, *building micrograd*, the MLP section, only after Th2. Type it yourself. Stop before any dataset training loop.
- **Géron:** *Hands-On Machine Learning*, ch.1 and ch.2. Depth on train, validation, and the untouched test. One exercise (G3). Not ch.3.
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
