# Lecture — 2026-10-22 · Upskill week 3, day 4: same loss

> **Upskill week 3** (Mon 19 – Sat 24 Oct 2026), day 4. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the loss lines, the one exercise, and every gold question.

Wednesday’s lecture: [`2026-10-21-week3-day3-lookup-rows.md`](2026-10-21-week3-day3-lookup-rows.md). The week targets do not change. Today advances Wednesday. It does not finish the week.

---

## 1. Goal for today

**Morning (09:00–12:00): the flat guess, beside every row**
- If the one-block lookup is missing, write the earliest blank of K1–K5 and stop.
- If you still have only one looked-up block, Wednesday’s extra rows (K8) are the morning. If the rows exist and the flat-guess loss does not, K9 is the morning. One of those, then stop.
- If the rows and the flat-guess loss both exist, put that same loss beside each looked-up block. One sentence on why the block does not change the number.
- The hidden layer stays unbuilt. Makemore part 3 stays shut.

**Evening (19:00–22:00): the next blank Géron prompt, and more eval rows**
- One exercise. The earliest blank of G10, then G11, then G12. If all three are written, Géron **ch.6**, one new cluster: a regression leaf holds a number. Ch.7 stays shut until that note exists.
- **Eval table v1:** more rows. A score is written only when a local **RAGAS** run returned it. Not TruLens.
- Gold keeps moving from 30 toward **50 by Sat 24 Oct**. A few items, not the rest of the twenty.
- No child, nephew, or other private personal data in the loss lines or the gold file.

---

## 2. Where you are

Wednesday’s bar was a handful of (block → next character) rows looked up on Tuesday’s untrained table, or, if those rows were already there, the loss of a flat guess over the characters in the table. The vectors were not trained. The hidden layer was not built.

G10 is the split. G11 is Gini or entropy. G12, if you wrote it, is an invented class share at a leaf. The eval table has the header, two chunk-size rows, and two rows for a second metric, scores blank unless a run returned them. Gold is on the way from 30 to 50, not at 50. If the count is under 30, the first evening minutes finish 30, then you add toward 50.

`03-makemore-gpt/` is still the code home. `evals/` is where v1 lives. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.3–4 unless one of G5–G9 is still blank.

Upskill week 3, still open after today: the rest of ch.6, then ch.7, the hidden layer later in makemore part 2, gold to 50, more real RAGAS cells on this table, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**The same loss on every row**
- The flat guess gives every character in the table the same probability. It never reads the block, so the loss does not change when the block changes. You write that loss beside each row you already looked up. You use the number from K9. You do not calculate a new kind of loss.
- A length-2 vector is still not a probability. You do not turn the looked-up rows into one.
- The hidden layer would be what lets the block change the probability of the next character. Name that in one sentence. Do not build it. Do not train. Do not change the vectors.
- The picture of a loss that ignores its input stays `slides later`. Part 3 stays shut.
- The blocks stay the ones you already wrote. Made-up, or already-public. Not a child, a nephew, or anyone private.

**Géron ch.6, the next cluster (concepts).** Only if G10, G11, and G12 are already in your notes. Stay inside decision trees.
- A regression tree predicts a number. The leaf holds a summary of the target numbers that landed there. The usual summary is their mean. You invent a few target numbers. You say what the leaf would report. You do not copy a formula out of the book as your answer.
- This is a different job from answer versus refuse. One sentence on the difference is enough. You do not refit G12.
- Instability is the rest of ch.6. It stays shut. Not ch.7. Not a forest, not boosting, not stacking. No fitted tree.

**Eval table v1, more rows (RAGAS).** Yesterday’s second-metric rows are the door. Today the embedding choice is what changes.
- Two new rows. Pick one chunk size you already named. Two embedding names, in words: the one already on the table, and a different one you might compare. The metric is one you already used. The gold slice is a few ids you already have.
- A score cell stays blank unless a local RAGAS run returned that number. One returned number may be written on the row you actually ran. Do not invent the other. Do not retune the week-2 slice.
- Not TruLens. The metric formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 50 by Saturday. Under 30, finish 30 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate. Earliest blank of the one-block lookup, then K8, then K9. If all three exist, write the flat-guess loss beside each row. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | One sentence: the block does not change the loss. Name the hidden layer. Stop before you build it. |

**Prompts (you write the notes):**
- **K10.** In `notes/`, one line: K8 exists, K9 exists, or the earliest that does not. If the one-block lookup is missing, do the earliest blank of K1–K5 and stop. If K8 is missing, do K8 and stop. If K9 is missing, do K9 and stop. Do not start K11 on a blank.
- **K11.** Only if K8 and K9 are both written. Beside each looked-up block, the flat-guess loss from K9. Then two sentences: (1) the number does not change when the block changes, because the guess never read the vectors; (2) the hidden layer would be what lets the block change the next-character probability, and you are not building it. Do not train. Do not change the vectors. Do not call the number a trained loss. No private names.

Open the makemore part 2 video only after K11, and only for the picture of a loss that ignores the block. Do not paste the hidden layer.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | The earliest blank of G10, then G11, then G12. If all three exist, the regression leaf and G13. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | Eval table v1: two rows where the embedding name changes. A score only if RAGAS returned it. |
| 21:20–22:00 | Gold toward **50 by Sat 24 Oct**. If the count is under 30, finish 30 first. Stop at 22:00. |

**Géron — one exercise, the next blank only**
- **G13.** Only if G10, G11, and G12 are already written. If one of those is blank, that blank is the exercise and you do not start G13. If all three exist: invent three target numbers. In your notes: (1) what a regression leaf would report (their mean), in a sentence you calculate; (2) one sentence on how this differs from the answer-versus-refuse leaf in G12; (3) the line that the numbers are invented, not the output of a fitted tree; (4) the line you will not cross — no ch.7.

**Table, privacy, gold (prompts only):**
- **V4.** If V3’s two rows are missing, write V3 and stop. If they exist, add two rows in `evals/`. One chunk size you already named. Two embedding names in words (the one already on the table, and a different one). One RAGAS metric you already used. A few gold ids you already have. Leave each score blank unless a local RAGAS run returned it. One real number is enough. Do not invent the other. Do not retune the week-2 slice. Not TruLens. Do not commit a key.
- **B22.** One line: today’s loss lines and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would. If B20 was never written, write that line first.
- **B23.** Append gold items you write yourself. If you are under 30, reach 30 before you count toward 50. A few new items is enough. Keep a mix of types, and keep at least one refuse. The week target stays 50 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What did you write beside each block this morning, and which layer did you leave unbuilt?
2. Which Géron prompt did you actually write — the earliest blank, or G13 — and if G13, what did the leaf report?
3. What changes between the two new eval rows, and which score cells did you leave blank on purpose?
4. What personal data is banned from the loss lines and from the gold file?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 2, after K11, the picture of a loss that does not see the block. Stop before the hidden layer. Not part 3.
- **Géron:** *Hands-On Machine Learning*, ch.6. The earliest blank of G10, G11, or G12; otherwise one exercise (G13, a regression leaf). Not ch.7 today. Ch.7 is later this week, after this note.
- **Evals:** **RAGAS** only. The week-2 slice stays frozen. Table v1 grows by two embedding rows tonight. Not TruLens.
- **Gold:** 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 2 (YouTube)](https://www.youtube.com/watch?v=TCH_1BHY58I)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 3 (19–24 Oct):* ☐ Géron ch.6–7 ☐ makemore part 2 ☐ gold 50 by Sat 24 Oct ☐ eval table v1 (RAGAS) ☐ no child/nephew data in trains or gold
