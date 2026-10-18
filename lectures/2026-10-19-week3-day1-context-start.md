# Lecture — 2026-10-19 · Upskill week 3, day 1: context window

> **Upskill week 3** (Mon 19 – Sat 24 Oct 2026), day 1. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the notes, the table header, and every gold question.

Saturday’s lecture: [`2026-10-17-week2-day6-week-close.md`](2026-10-17-week2-day6-week-close.md). Week 2 is closed. Today opens week 3. It does not finish it.

---

## 1. Goal for today

**Morning (09:00–12:00): the first slice of makemore part 2**
- The next character can depend on more than the one character before it. You pick a small window and write one example on paper.
- An embedding is a vector you look up per character. You say what it is. You do not train a hidden layer.

**Evening (19:00–22:00): ch.6 opens, and the eval table gets a header**
- Géron **ch.6** only, one cluster: a decision tree split, and why a deep tree memorizes. One exercise. Ch.7 stays shut.
- **Eval table v1:** columns for a chunking choice and an embedding choice, scored later with **RAGAS** only. Tonight is the header. Not TruLens.
- Gold moves from 30 toward **50 by Sat 24 Oct**. A few items, not all twenty.
- No child, nephew, or other private personal data in the window examples or the gold file.

---

## 2. Where you are

Week 2 left a one-layer bigram net, a loss next to the count model, a few strings from each, Géron ch.3–4 (G5–G9), a RAGAS slice you said you would leave alone, and a gold file aimed at 30. Do not retrain that layer. Do not reopen ch.3–4 unless one of G5–G9 is still blank. If the gold count is under 30, the first evening minutes finish 30, then you add toward 50.

`03-makemore-gpt/` is still the code home. `evals/` is where the new table may live. The week-2 baseline stays the slice you do not retune tonight.

Upskill week 3, still open after today: Géron ch.6–7, the rest of makemore part 2, gold to 50, an eval table with real RAGAS rows, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**Makemore part 2, the opening only**
- Part 1 conditioned on one previous character. Part 2 conditions on a short block of them. You choose the block size and write it down. A small integer is enough.
- One training example is that block, and the character that followed it. The picture of the block entering the model is `slides later`.
- An embedding is a learned vector stored per character. Looking it up is how the block becomes numbers. You describe the lookup. You do not pick a fight with a training loop.
- The hidden layer that mixes those vectors is the rest of part 2. Name it. Do not build it today.
- The loss is still “how little probability the next character got.” What is new is the window, not a new loss.
- Examples you write are made-up, or from the public strings you already used. They are not a child, a nephew, or anyone private.

**Géron ch.6, one cluster (concepts).** Stay inside decision trees. Ensembles are ch.7.
- A split asks one question about one feature and sends rows down two branches. A leaf holds the prediction for the rows that landed there.
- For PersonaLearn the prediction can be the class you already named (answer versus refuse). You are not fitting a tree tonight.
- A deep tree can memorize the rows it was grown on. Depth, and how few rows a leaf is allowed to hold, are the knobs you can name. Do not tune them.
- Not ch.7. Not a forest, not boosting, not stacking.

**Eval table v1 (RAGAS).** Week 2’s slice stays frozen. This week’s table is a comparison you have not run yet.
- A row will be: a chunking choice, an embedding choice, the gold slice, a RAGAS metric, and a score. Tonight you write the header and one sentence on two chunk sizes you might compare later.
- A score, if you write one, has to be a number a local RAGAS run returned. You do not invent it, and you do not need one tonight.
- Not TruLens. The metric formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 50 by Saturday. Under 30, finish 30 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | One training example on paper: a short block of previous characters, and the character that followed. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Say what an embedding lookup is. Name the hidden layer. Stop before you build it. |

**Prompts (you write the notes):**
- **K1.** In `notes/`, the block size you chose, and one example: the previous characters and the next character. Made-up or already-public strings only. No private names.
- **K2.** Two sentences: a vector per character, and how the block becomes the input a later hidden layer would mix. Do not build that layer. Do not train.
- **K3.** One sentence on what is new versus part 1 (the window), and one sentence on the loss you are not recomputing today. Then stop.

Open the makemore part 2 video only after K2, and only for the picture of the window. Do not paste a network.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Géron ch.6, one split and why depth memorizes, then the single exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | Eval table v1: the header, and two chunk sizes you might compare. No new tool. |
| 21:20–22:00 | Gold toward **50 by Sat 24 Oct**. If the count is under 30, finish 30 first. Stop at 22:00. |

**Géron ch.6 — one exercise for the cluster**
- **G10.** Pick one feature you could split on for the answer-versus-refuse decision (question type, or whether a passage was retrieved). In your notes: (1) the question the first split asks; (2) what the two branches mean; (3) why a deep tree is the memorizing fit you already know, in one sentence; (4) the line you will not cross — no fitted tree, no tuned depth, no ch.7.

**Table, privacy, gold (prompts only):**
- **V1.** In `evals/`, the header of the comparison table: chunking, embedding, gold slice, RAGAS metric, score. Under it, two chunk sizes you might compare later this week, in words. Leave scores blank unless a local RAGAS run already returned a number. Do not invent one. Do not retune the week-2 slice. Not TruLens. Do not commit a key.
- **B16.** One line: K1’s example and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would.
- **B17.** Append gold items you write yourself. If you are under 30, reach 30 before you count toward 50. A few new items is enough. Keep a mix of types, and keep at least one refuse. The week target stays 50 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What is in one part-2 training example, and what did you refuse to build this morning?
2. What does the first split of your G10 tree ask, and why is a deep tree a memorizing fit?
3. What are the two chunk sizes on the new table, and why is a blank score still honest?
4. What personal data is banned from K1 and from the gold file?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 2, the context-window section, after K2. Stop before the hidden layer.
- **Géron:** *Hands-On Machine Learning*, ch.6, decision trees. One exercise (G10). Not ch.7 today. Ch.7 is later this week.
- **Evals:** **RAGAS** only. The week-2 slice stays frozen. Table v1 is a header tonight. Not TruLens.
- **Gold:** 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 2 (YouTube)](https://www.youtube.com/watch?v=TCH_1BHY58I)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 3 (19–24 Oct):* ☐ Géron ch.6–7 ☐ makemore part 2 ☐ gold 50 by Sat 24 Oct ☐ eval table v1 (RAGAS) ☐ no child/nephew data in trains or gold
