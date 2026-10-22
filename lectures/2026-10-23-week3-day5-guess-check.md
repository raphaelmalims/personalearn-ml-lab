# Lecture — 2026-10-23 · Upskill week 3, day 5: guess check

> **Upskill week 3** (Mon 19 – Sat 24 Oct 2026), day 5. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the check, the one exercise, and every gold question.

Thursday’s lecture: [`2026-10-22-week3-day4-same-loss.md`](2026-10-22-week3-day4-same-loss.md). The week targets do not change. Today moves toward Saturday’s close. It does not finish the week.

---

## 1. Goal for today

**Morning (09:00–12:00): the flat guess against the table**
- If the loss is not yet beside the looked-up blocks, write the earliest blank of K8, K9, or K11 and stop.
- If K11 exists, compare the flat guess to the table. For each character, the share the flat guess gives it, and how often that character was the next one in your blocks.
- One concrete check while you are there: a character that shows up twice returned the same vector both times.
- The hidden layer stays unbuilt. Makemore part 3 stays shut.

**Evening (19:00–22:00): the next blank Géron prompt, and a score only if a run returned one**
- One exercise. The earliest blank of G10, then G11, then G12, then G13. If all four are written, Géron **ch.7**, one cluster: a vote. No second cluster.
- **Eval table v1:** a new row only when a local **RAGAS** run returned a score you have not already written. No blank row tonight. Not TruLens.
- Gold keeps moving from 30 toward **50 by Sat 24 Oct**. A few items. Saturday is the day the count reaches 50.
- No child, nephew, or other private personal data in the check or the gold file.

---

## 2. Where you are

Thursday’s bar was the flat-guess loss written beside each looked-up block, and one sentence that the block does not change the number. That was gated on Wednesday’s rows and on K9. The vectors were not trained. The hidden layer was not built.

G10 is the split. G11 is Gini or entropy. G12 is an invented class share. G13, if you wrote it, is a regression leaf and a mean of three invented numbers. Ch.7 has not been opened. The eval table has chunk-size rows, a second metric, and two embedding names, scores blank unless a run returned them. Gold is on the way from 30 to 50, not at 50. If the count is under 30, the first evening minutes finish 30, then you add toward 50.

`03-makemore-gpt/` is still the code home. `evals/` is where v1 lives. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.3–4 unless one of G5–G9 is still blank.

Saturday 24 Oct stays the lighter close: catch-up, and gold to 50. Do not do Saturday’s pass tonight.

Upskill week 3, still open after today: ch.7 beyond one vote, the hidden layer later in makemore part 2, gold to 50, any real RAGAS cell still missing, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**The flat guess next to the counts**
- The flat guess gives every character in the embedding table the same share. Your blocks have a next character each. Those next characters are a count, one per character in the table. The share and the count are different objects. You write both. You do not edit either to make them match.
- Where the counts are uneven, the flat guess and the rows disagree. That is the check. You do not build a model to repair it.
- A lookup is a row read by character. The same character in two blocks is the same row. If one character appears twice, the two vectors match. If none appears twice, you write that and you do not go hunting for a new string.
- The vectors stay as they are. The hidden layer stays unbuilt. Part 3 stays shut. The picture of the two columns stays `slides later`.
- Characters and blocks stay the ones you already wrote. Made-up, or already-public. Not a child, a nephew, or anyone private.

**Géron ch.7, one cluster (concepts).** Only if G10, G11, G12, and G13 are already in your notes.
- A vote asks several predictors for a class and keeps the class that gets more votes. For you the class is still answer or refuse. You invent the votes. You do not train the predictors.
- A hard vote counts labels. A soft vote would average probabilities. You can name the soft vote. You do not compute one.
- Bagging, boosting, and stacking are the rest of ch.7. They stay shut. The ch.6 note on instability stays a name. You do not write it tonight. No fitted forest.

**Eval table v1 (RAGAS).** Tonight a row is earned by a number a local run returned.
- If you have a new returned score, one row: the chunking, the embedding, the gold slice, the metric, and that score. If you have no new number, one sentence that says so, and no new row.
- Do not invent a score. Do not fill a blank to make the table look finished. Do not retune the week-2 slice. Not TruLens. The metric formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 50 by Saturday, not to 50 tonight. Under 30, finish 30 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on K11. If it is missing, the earliest blank of K8, K9, or K11, then stop. If it exists, the share and the count for each character. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | The repeated-character check, if you have one. One sentence on where the flat guess and the counts disagree. Stop before a hidden layer. |

**Prompts (you write the notes):**
- **K12.** In `notes/`, one line: K11 exists, or the earliest blank among K8, K9, and K11. If one is missing, write that prompt and stop. Do not start K13 on a blank.
- **K13.** Only if K11 is written. For each character in the embedding table: the share the flat guess gives it, and the count of looked-up blocks whose next character is that character. One sentence on whether those counts are even. If one character appears in two blocks, the two vectors, and whether they match. If none appears twice, say so. Do not change the vectors. Do not turn the counts into a trained model. Do not build the hidden layer. No private names.

Open the makemore part 2 video only after K13, and only to see that a later layer would use the block. Do not paste that layer.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | The earliest blank of G10, then G11, then G12, then G13. If all four exist, one vote, G14. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | RAGAS: one new row only if a run returned a new score. Otherwise one honest line. |
| 21:20–22:00 | Gold toward **50 by Sat 24 Oct**. A few items. Stop at 22:00. Saturday reaches 50. |

**Géron — one exercise, the next blank only**
- **G14.** Only if G10, G11, G12, and G13 are already written. If one of those is blank, that blank is the exercise and you do not start G14. If all four exist: invent three votes on one made-up question, each vote answer or refuse. In your notes: (1) the majority, in a sentence; (2) what a soft vote would have used instead of a label, and the line that you are not computing it; (3) the line that the votes are invented, not the output of trained models; (4) the line you will not cross — no bagging, no boosting, no stacking.

**Table, privacy, gold (prompts only):**
- **V5.** If a local RAGAS run returned a score you have not already written in `evals/`, add that one row: chunking, embedding, gold slice, metric, and the number. If no new number came back, write one line that says so, and do not add a blank row. Do not invent a score. Do not retune the week-2 slice. Not TruLens. Do not commit a key.
- **B24.** One line: today’s check and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would. If B22 was never written, write that line first.
- **B25.** Append gold items you write yourself. If you are under 30, reach 30 before you count toward 50. A few new items is enough. Keep a mix of types, and keep at least one refuse. Leave the last stretch for Saturday. The week target stays 50 by Sat 24 Oct.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What two numbers did you write for each character, and which layer did you leave unbuilt?
2. Which Géron prompt did you actually write — the earliest blank, or G14 — and if G14, what was the majority?
3. Did a RAGAS run give you a new score tonight, and what did you do when it did not?
4. What personal data is banned from the check and from the gold file?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 2, after K13, only the idea that a later layer would read the block. Stop before the hidden layer. Not part 3.
- **Géron:** *Hands-On Machine Learning*. The earliest blank of G10–G13; otherwise one exercise (G14, a hard vote). Not bagging, boosting, or stacking today.
- **Evals:** **RAGAS** only. A new row only with a returned score. The week-2 slice stays frozen. Not TruLens.
- **Gold:** 50 by Sat 24 Oct (see `gold/README.md`). Tonight a few. Saturday is the close. Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 2 (YouTube)](https://www.youtube.com/watch?v=TCH_1BHY58I)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 3 (19–24 Oct):* ☐ Géron ch.6–7 ☐ makemore part 2 ☐ gold 50 by Sat 24 Oct ☐ eval table v1 (RAGAS) ☐ no child/nephew data in trains or gold
