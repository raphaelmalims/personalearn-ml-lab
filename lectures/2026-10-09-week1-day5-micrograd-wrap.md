# Lecture — 2026-10-09 · Upskill week 1, day 5: micrograd wrap

> **Upskill week 1** (Mon 5 – Sat 10 Oct 2026), day 5. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the inventory rows, and every gold question.

Yesterday’s lecture: [`2026-10-08-week1-day4-finish-mlp.md`](2026-10-08-week1-day4-finish-mlp.md). The week targets do not change. Saturday is the lighter catch-up, not a new topic.

---

## 1. Goal for today

**Morning (09:00–12:00): a micrograd you can run again**
- If Thursday’s 2–2–1 or the shared-weight check is still open, that is the bar. Finish it.
- If both are green, do not rebuild them. Wrap the same net so a short list of pairs you type can take a handful of steps, with `.grad` zeroed every step. Write what this engine can do, and what you will not build.

**Evening (19:00–22:00): one ch.2 close, a RAGAS card, gold toward 20**
- Géron **ch.1–2** only: how you would present the system, and what data drift and model rot mean. One exercise for that cluster.
- **RAGAS** vocabulary only: a four-line card you can use tomorrow. Still no scores. Baseline RAG scores are **Upskill week 2**.
- PDF inventory stays metadata. Gold pushes toward **20 by Sat 10 Oct**. Stop at 20. Stop at 22:00.

---

## 2. Where you are

Thursday’s bar was a 2–2–1 whose hidden weight passed a finite-difference check, then two made-up pairs added into one scalar loss, then one more step with gradients zeroed. A list of pairs and a repeated step were outside Thursday.

The copy of `01-micrograd/value.py` on `main` is still the forward graph (`+` and `*`) plus a stub where `backward` will live. If your working copy does not yet have Thursday’s Th2 and Th3 green, this morning is still Thursday. Do not wrap a net you have not checked.

This lecture does not re-teach the chain rule, topological order, why a shared weight accumulates, `tanh`, or the single zeroing demo. Those are Monday through Thursday.

Upskill week 1 still open: micrograd backprop, Géron ch.1–2, eval basics, PDF inventory, first 20 gold questions.

---

## 3. Concepts to use (you derive anything local; you do not paste it)

**A usable wrap, not a trainer**
- Usable, for this week, means you can call the same 2–2–1 again on pairs you type, take a few steps, and trust one checked weight. It does not mean a data loader, an optimizer object, a file of examples, or a real dataset.
- Each step is the same sequence you already ran once: forward, scalar loss, add the losses, `backward` on the sum, a small step of each parameter against its `.grad`, then zero every `.grad` you own. The new part is that the sequence can run more than once without you retyping the graph.
- Zeroing stays inside the step. A second pass over the same list without a zero stacks on yesterday’s gradients. Say that in one sentence before you write the loop.
- The picture of those repeated paths meeting on one weight is still Thursday’s board, and it stays `slides later`.
- When you stop, write two short lists in `notes/`: what the engine can do today, and what you refused (file loader, optimizer class, moon data, anything past ch.1–2). That note is the week-1 micrograd close. Saturday reads it. Saturday does not extend it.

**Géron ch.1–2, depth (concepts).** Stay inside these two chapters. G1 was the taxonomy and the eight steps. G2 was the measure, fit versus underfit, and the untouched test. G3 was fit, tune, and report-once. Today is the end of that same checklist, still with no system to score:
- Presenting the solution is a description a non-ML teammate can use: what the system is for, what it will refuse, and which number you have not earned yet.
- After launch, ch.2 asks you to watch the data and the model. Data drift is the corpus changing under you (a new edition, a topic your inventory still marks thin, questions that no longer look like the ones you wrote). Model rot is behaviour that used to match the source and no longer does. Name both. Do not measure either.
- Neither one is a licence to run the gold file. The gold file stays the report-once set from G3. This week, “monitor” means the inventory and the gold count, not a RAGAS table.
- Stay out of ch.3.

**Eval basics (RAGAS).** You already have the four names. Today you put them on one card so Saturday does not depend on the docs:
- Context recall notices a missing passage. Faithfulness notices an answer the passages do not support. Answer relevancy notices a grounded answer to the wrong question. Context precision notices junk that was retrieved anyway.
- Each line on the card says which of question, answer, contexts, and reference that metric reads. You write the line from memory, then check the RAGAS metrics page only if a line is blank.
- An LLM judge is still noisy, and it is still not the gold set. Do not record scores. Do not write a judge prompt. The metric formulas stay `slides later`.

**PDF inventory and gold.** Same inventory columns as Monday. Commit the inventory, not the PDFs. Leave a cell blank rather than guess. The week target is still 20 gold items by Saturday. If you are short, tonight’s writing is the push. Do not write a 21st item.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on Thursday. If Th2 or Th3 is red, finish that and do not start the wrap. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Only if the shared-weight check is green: a short list, a few steps, then the can/cannot note. |

**Prompts (you write the code):**
- **F1.** In `notes/`, two lines: Th2 pass or not; Th3 pass or not. If either is “not”, do that Thursday prompt and stop the new work.
- **F2.** Keep the same 2–2–1. Put at least three made-up pairs in a Python list you type in the file. Do not read them from disk. One function you write runs one step on that whole list: sum of scalar losses, one `backward`, one parameter step, then zero. Call it a handful of times. Write down how many steps you chose, and the loss before the first call and after the last.
- **F3.** In `notes/`, the two lists: what this engine can do, and what you refused to build. This is the week-1 micrograd close.
- **F4 (stretch).** Rebuild one scalar you already checked, in PyTorch, with `requires_grad`. Compare one `.grad`. Write match or not. If it does not match, the bug is yours to find. Do not start a second network.

Open the micrograd repo only to compare after F2 runs. Do not paste its training loop.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Géron ch.1–2, present and maintain, then the single exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:10 | RAGAS card: four lines, no numbers. If R8–R10 are blank, do those instead and skip the card. |
| 21:10–21:25 | PDF inventory: one verified row, or one line on a topic that is still thin. |
| 21:25–22:00 | Gold toward **20 by Sat 10 Oct**. If you are under 20 at 21:10, gold takes the inventory slot too. Stop at 20 items. Stop at 22:00. |

**Géron ch.1–2 — one exercise for the cluster**
- **G4.** Use one PersonaLearn question already in the gold file. In your notes: (1) four lines a non-ML teammate could read — what this is for, what it should refuse, which measure you would ship later, and the score you will not quote this week; (2) one PersonaLearn example of data drift; (3) one PersonaLearn example of model rot, named and not measured; (4) the single Saturday ML task if the gold file is still short of 20, or, if it is already 20, the one fuzzy micrograd point Saturday should reread. Do not fit anything. Do not score anything.

**Eval, inventory, gold (prompts only):**
- **R12.** Four lines, one per RAGAS metric. Each line: the failure it catches in PersonaLearn, and which of question / answer / contexts / reference it reads. No numbers. No judge prompt.
- **R13.** One inventory row you can verify, or one sentence on the thinnest topic. Blank cells stay blank.
- **R14.** Append gold items you write yourself until the file reaches 20 or the clock hits 22:00. Keep a mix of types, and keep at least one item the corpus should refuse. Do not add a 21st.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What can your engine do after F3, and which three things did you refuse to build?
2. Why does every pass over the list need its own zero of `.grad`?
3. For this corpus, what is one data-drift change, and what is one model-rot change?
4. Which of the four RAGAS metrics needs the reference answer, and which one can stay quiet when the answer is grounded but off the question?

---

## 7. Pointers

- **micrograd:** Karpathy, *building micrograd*, only to compare after F2. The week-1 close is your can/cannot note, not his training loop.
- **Géron:** *Hands-On Machine Learning*, ch.1 and ch.2. Present, then drift and rot. One exercise (G4). Not ch.3.
- **Evals:** **RAGAS** metrics overview, only to fill a blank line on the card. Upskill week 1 is eval basics. First baseline scores are Upskill week 2. Not TruLens.
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
