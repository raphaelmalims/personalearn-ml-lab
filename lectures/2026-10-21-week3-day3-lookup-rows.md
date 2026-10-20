# Lecture — 2026-10-21 · Upskill week 3, day 3: lookup rows

> **Upskill week 3** (Mon 19 – Sat 24 Oct 2026), day 3. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the rows, the loss line, and every gold question.

Tuesday’s lecture: [`2026-10-20-week3-day2-embedding-table.md`](2026-10-20-week3-day2-embedding-table.md). The week targets do not change. Today advances Tuesday. It does not finish the week.

---

## 1. Goal for today

**Morning (09:00–12:00): more rows, or a loss on the lookup**
- If the tiny table or the one-block lookup is missing, write the earliest blank of K1–K5 and stop. No new slice on an empty table.
- If that lookup exists and you only have the one block, add more (block → next character) rows and look each block up with the same table.
- If those rows are already written, do not add another pile. Write the loss of a flat guess over the characters in the table. The vectors stay as they are.
- The hidden layer stays unbuilt. Makemore part 3 stays shut.

**Evening (19:00–22:00): the next cluster, and more eval rows**
- If G10 is blank, write G10 and stop the Géron hour. If G10 exists and G11 is blank, write G11 and stop. One cluster.
- If G10 and G11 are both written, Géron **ch.6**, one new cluster: a leaf can report a class share, not only a hard label. One exercise. Ch.7 stays shut. You still do not fit a tree.
- **Eval table v1:** more rows under the two you already have. A score is written only when a local **RAGAS** run returned it. Not TruLens.
- Gold keeps moving from 30 toward **50 by Sat 24 Oct**. A few items, not the rest of the twenty.
- No child, nephew, or other private personal data in the new rows, the loss note, or the gold file.

---

## 2. Where you are

Tuesday’s bar was a tiny embedding table for the characters in Monday’s one example, and the vectors that came back when you looked that block up. Three extra hand-counted rows were optional. The hidden layer was still unbuilt. Nothing was trained.

G10 is the split. G11, if you wrote it, is Gini or entropy and what a pure leaf means. The eval table has a header and two rows (one per chunk size), scores blank unless a run returned them. Gold is on the way from 30 to 50, not at 50. If the count is under 30, the first evening minutes finish 30, then you add toward 50.

`03-makemore-gpt/` is still the code home. `evals/` is where v1 lives. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.3–4 unless one of G5–G9 is still blank.

Upskill week 3, still open after today: the rest of Géron ch.6, then ch.7, the hidden layer later in makemore part 2, gold to 50, more real RAGAS cells on this table, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**More rows on the same table**
- A row of the training set is still a block of previous characters and the character that followed. Tuesday looked up one. Today a handful more, same block size, same table.
- A character that was not in the table gets one new row, filled by hand the same way as the others. The table does not become a full name list.
- Looking a block up is still reading one vector per character, in order. You write those vectors down. You do not flatten them.
- Strings are made-up, or already-public strings you already used. Not a child, a nephew, or anyone private.

**A loss on the lookup, only once the rows exist**
- The loss you already know by name is how little probability the next character got. The vectors in the table are not probabilities. A length-2 row does not name a probability. Write that down before you write a number.
- The layer that would turn a block of vectors into a distribution over the next character is the hidden layer plus the map after it. You can name that in one sentence. You do not build it, and you do not train.
- What you can score without that layer is a flat guess: every character in your table equally likely, and the loss is how surprised that guess is when the next character arrives. You calculate it for your own table. You label it `flat guess`. You do not change the vectors to make the number smaller.
- That number is not a trained part-2 loss. The picture of the sum stays `slides later`. Part 3 stays shut.

**Géron ch.6, the next cluster (concepts).** Only if G10 and G11 are already in your notes. Stay inside decision trees.
- A leaf can store the share of its rows that fall in each class, not only the class it would predict. The share is a count divided by the number of rows in that leaf. You describe one leaf. You do not copy a formula out of the book as your answer.
- For PersonaLearn the classes are still answer and refuse. A leaf that is mixed has a share for each. A pure leaf, the one from G11, has a share of one for a single class.
- You invent the counts. You do not grow a tree, and you do not tune a threshold on the share.
- Regression trees and instability are the rest of ch.6. They stay shut. Not ch.7. Not a forest, not boosting, not stacking.

**Eval table v1, more rows (RAGAS).** Yesterday’s two rows are the door. Today you add rows beside them.
- A new row is another RAGAS metric you already know, on a chunk size you already named, with the embedding choice already on that row. Two new rows is enough.
- The gold slice stays a few ids you already have. A score cell stays blank unless a local RAGAS run returned that number. One returned number may be written on the row you actually ran. Do not invent the other. Do not retune the week-2 slice.
- Not TruLens. The metric formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 50 by Saturday. Under 30, finish 30 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on the tiny table. If the one-block lookup is missing, finish it and stop. If it exists, add more rows and look them up. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | If the extra rows were already written before today, the flat-guess loss. If you just wrote them and time remains, the same loss. Stop before a hidden layer. |

**Prompts (you write the notes):**
- **K7.** In `notes/`, one line: K5 exists, or it does not. If it does not, do the earliest blank of K1–K5 and stop. No new rows, no loss.
- **K8.** If K5 exists and you do not yet have several looked-up blocks: a handful of further (block → next character) rows. Same block size as K1. Same table as K5. A new character gets one hand-filled row. Look each block up and write the vectors in order. Made-up or already-public strings only. Do not grow a name list. Do not train. No private names. If this is the work you started the morning with, it is the morning. Do not also force the loss if the clock is gone.
- **K9.** If several lookups are already written (K6 or K8): one sentence that the vectors are not probabilities, then the loss of a flat guess over the characters in your table. You calculate it. Label it `flat guess`. Do not change the vectors. Do not build the hidden layer. Do not call the number a trained loss. If you cannot calculate it, write the sentence and leave the number blank. Do not invent one.

Open the makemore part 2 video only after K8 or K9, and only for the picture of several blocks. Do not paste the hidden layer.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Earliest blank of G10, then G11. If both exist, the class-share cluster and G12. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | Eval table v1: more rows. A score only if RAGAS returned it. |
| 21:20–22:00 | Gold toward **50 by Sat 24 Oct**. If the count is under 30, finish 30 first. Stop at 22:00. |

**Géron ch.6 — one exercise for the next cluster**
- **G12.** Only if G10 and G11 are already written. If G10 is blank, G10 is the exercise. If G11 is blank, G11 is the exercise. You do not start G12 on a blank. If both exist: invent one leaf. In your notes: (1) a small count of rows, how many are answer, and the share, in a sentence you calculate; (2) how that share differs from the pure leaf in G11; (3) the line that these counts are invented, not the output of a fitted tree; (4) the line you will not cross — no threshold you tuned, no ch.7.

**Table, privacy, gold (prompts only):**
- **V3.** If V2’s two rows are missing, write V2 and stop. If they exist, add two rows in `evals/`: a second RAGAS metric you already know, on the same two chunk sizes, same embedding words as those rows. Leave each score blank unless a local RAGAS run returned it. One real number is enough. Do not invent the other. Do not retune the week-2 slice. Not TruLens. Do not commit a key.
- **B20.** One line: today’s new lookup rows, the loss note, and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would. If B18 was never written, write that line first.
- **B21.** Append gold items you write yourself. If you are under 30, reach 30 before you count toward 50. A few new items is enough. Keep a mix of types, and keep at least one refuse. The week target stays 50 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Did this morning add lookup rows or a flat-guess loss, and which layer did you leave unbuilt?
2. Which Géron prompt did you actually write — G10, G11, or G12 — and, if G12, what share did the invented leaf hold?
3. What are the new eval rows, and which score cells did you leave blank on purpose?
4. What personal data is banned from the new rows and from the gold file?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 2, several context blocks, after K8 or K9. Stop before the hidden layer. Not part 3.
- **Géron:** *Hands-On Machine Learning*, ch.6. The earliest blank of G10 or G11; otherwise one exercise (G12, a class share at a leaf). Not ch.7 today. Ch.7 is later this week.
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
