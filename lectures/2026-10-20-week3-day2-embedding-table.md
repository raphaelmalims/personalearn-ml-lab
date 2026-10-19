# Lecture — 2026-10-20 · Upskill week 3, day 2: embedding table

> **Upskill week 3** (Mon 19 – Sat 24 Oct 2026), day 2. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the table, the rows, and every gold question.

Monday’s lecture: [`2026-10-19-week3-day1-context-start.md`](2026-10-19-week3-day1-context-start.md). The week targets do not change. Today advances Monday. It does not finish the week.

---

## 1. Goal for today

**Morning (09:00–12:00): the lookup becomes a tiny table**
- If Monday’s paper example or the two lookup sentences are missing, write the earliest blank of K1–K3 and stop. No code on an empty page.
- If K1–K3 exist, build a tiny embedding table for the characters in that one example and look the block up. You fill the rows. You do not train them.
- The hidden layer that would mix those vectors stays unbuilt. Makemore part 3 stays shut.

**Evening (19:00–22:00): the next ch.6 cluster, and the first table rows**
- If G10 is blank, write G10. That closes yesterday’s split. Do not add a second exercise on the same cluster.
- If G10 is written, Géron **ch.6**, one new cluster: the impurity a split tries to reduce (Gini or entropy). One exercise. Ch.7 stays shut. You still do not fit a tree.
- **Eval table v1:** two rows, one per chunk size you already named. A score is written only when a local **RAGAS** run returned it. Not TruLens.
- Gold keeps moving from 30 toward **50 by Sat 24 Oct**. A few items, not the rest of the twenty.
- No child, nephew, or other private personal data in the table, the rows, or the gold file.

---

## 2. Where you are

Monday’s bar was a block size, one (previous characters → next character) example on paper, and two sentences on an embedding lookup. The hidden layer was named and not built. The loss was not recomputed.

G10 is the ch.6 note: one split, two branches, and why a deep tree memorizes. The eval table has a header and two chunk sizes in words, with scores left blank. Gold is on the way from 30 to 50, not at 50. If the count is under 30, the first evening minutes finish 30, then you add toward 50.

`03-makemore-gpt/` is still the code home. `evals/` is where v1 lives. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.3–4 unless one of G5–G9 is still blank.

Upskill week 3, still open after today: the rest of Géron ch.6, then ch.7, the hidden layer later in makemore part 2, gold to 50, more real RAGAS cells on this table, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**A tiny embedding table, lookup only**
- The table has one row per character in Monday’s example. The row is a short vector. You choose the length. Two numbers is enough.
- An index says which row a character reads. Looking up the block means reading one row per character, in the order of the block.
- You fill the rows yourself this morning (by hand, or one untrained draw). Training would move those numbers later. You do not take that step.
- A few extra (block → next character) rows, counted by hand from made-up or already-public strings, are optional and only after the lookup is written. They are not a full training set.
- The hidden layer would flatten those rows and mix them. Name that, if you want one sentence. Do not code it. Do not sample from a new net.
- Part 3 of the series (the later training tricks) stays shut. The picture of the stacked rows is `slides later`.
- Characters come from K1. Made-up, or already-public strings you already used. Not a child, a nephew, or anyone private.

**Géron ch.6, the next cluster (concepts).** Only if G10 is already in your notes. Stay inside decision trees.
- A useful split leaves the two branches purer than the node it split. Two common scores for “how mixed is this node” are Gini impurity and entropy. You pick one to describe, in your own sentence.
- A pure leaf holds a single class. For PersonaLearn that class is still answer or refuse.
- The training rule that tries questions and keeps the one that reduces the score the most has a name, CART. You can name it. You do not run it, and you do not copy a formula out of the book as your answer.
- Class probabilities at a leaf, regression trees, and instability are the rest of ch.6. They stay shut. Not ch.7. Not a forest, not boosting, not stacking. No fitted tree.

**Eval table v1, first rows (RAGAS).** Yesterday’s header is the door. Today you fill two rows under it.
- Each row is a chunking choice, an embedding choice, the gold slice, a RAGAS metric, and a score cell. Use the two chunk sizes you already wrote. The same embedding name on both rows is enough, so the chunk size is what differs.
- The gold slice is a few ids you already have, not the whole file. The metric is one you already know (answer relevancy, or context precision).
- A score cell stays blank unless a local RAGAS run returned that number. One returned number may be written on the row you actually ran. Do not invent the other. Do not retune the week-2 slice.
- Not TruLens. The metric formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 50 by Saturday. Under 30, finish 30 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on K1–K3. If one is blank, write that and stop. If all three exist, build the tiny table and look up the block. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Write down the vectors the lookup returned. Optional: three hand-counted (block → next) rows. Stop before a hidden layer. |

**Prompts (you write the notes):**
- **K4.** In `notes/`, one line: K1, K2, and K3 exist, or the earliest that does not. If one is missing, write that Monday prompt and stop. No code.
- **K5.** If K1–K3 exist: in `03-makemore-gpt/` or `notes/`, a tiny embedding table for the characters in the K1 example only. Vector length 2 is enough. You fill each row. Look up the block and write the vectors that came back, in order. One sentence on how many characters the table has. Do not extend it to a full name list. Do not flatten the vectors into a hidden layer. Do not take a gradient step. Do not paste a table from the makemore repo.
- **K6.** Only if K5 is written and you are still inside this block: three extra (block → next character) rows, counted by hand from made-up or already-public strings. If the clock is gone, skip K6. Not a training set. Not part 3. No private names.

Open the makemore part 2 video only after K5, and only for the picture of the lookup table. Do not paste the layer that follows it.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | If G10 is blank, write G10 and stop the Géron hour. If G10 exists, read the impurity cluster and do G11. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | Eval table v1: two rows. A score only if RAGAS returned it. |
| 21:20–22:00 | Gold toward **50 by Sat 24 Oct**. If the count is under 30, finish 30 first. Stop at 22:00. |

**Géron ch.6 — one exercise for the next cluster**
- **G11.** Only if G10 is already written. Otherwise G10 is the evening exercise and you do not start this one. Pick Gini or entropy. In your notes: (1) your own one-sentence meaning of that score; (2) what a pure leaf would mean for answer versus refuse; (3) the name of the rule that keeps the split which reduces the score, and the line that you are not running it; (4) the line you will not cross — no fitted tree, no copied formula, no ch.7.

**Table, privacy, gold (prompts only):**
- **V2.** If V1’s header is missing, write V1 and stop. If it exists, add two rows in `evals/`, one per chunk size you named on Monday. Each row: chunking, embedding (words are enough; the same name on both rows is fine), gold slice (a few ids you already have), one RAGAS metric you already know, and a score cell. Leave the score blank unless a local RAGAS run returned it. One real number is enough. Do not invent the other. Do not retune the week-2 slice. Not TruLens. Do not commit a key.
- **B18.** One line: the K5 table, any K6 rows, and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would. If B16 was never written, write that line first.
- **B19.** Append gold items you write yourself. If you are under 30, reach 30 before you count toward 50. A few new items is enough. Keep a mix of types, and keep at least one refuse. The week target stays 50 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What did the lookup return this morning, and which layer did you leave unbuilt?
2. If G10 was blank, what did you write instead of G11? If G10 existed, what does a pure leaf mean in your G11 note?
3. What is filled in the two eval rows, and which score cells did you leave blank on purpose?
4. What personal data is banned from the embedding table and from the gold file?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 2, the embedding-table section, after K5. Stop before the hidden layer. Not part 3.
- **Géron:** *Hands-On Machine Learning*, ch.6. G10 if it is blank; otherwise one exercise (G11, Gini or entropy). Not ch.7 today. Ch.7 is later this week.
- **Evals:** **RAGAS** only. The week-2 slice stays frozen. Table v1 grows by two rows tonight. Not TruLens.
- **Gold:** 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 2 (YouTube)](https://www.youtube.com/watch?v=TCH_1BHY58I)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 3 (19–24 Oct):* ☐ Géron ch.6–7 ☐ makemore part 2 ☐ gold 50 by Sat 24 Oct ☐ eval table v1 (RAGAS) ☐ no child/nephew data in trains or gold
