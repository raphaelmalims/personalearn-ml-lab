# Lecture — 2026-10-24 · Upskill week 3, day 6: week close

> **Upskill week 3** (Mon 19 – Sat 24 Oct 2026), day 6. Saturday is the light close: ML **09:00–12:00** EAT only.
> **10-minute break per 90 minutes** inside that block. Hard stop **12:00**. The evening is free. There is no 19:00–22:00 study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write any catch-up lines, the proof, and every gold question still needed to reach 50.

Yesterday’s lecture: [`2026-10-23-week3-day5-guess-check.md`](2026-10-23-week3-day5-guess-check.md). The week targets do not change. Today is the day they close. Do not open a hidden layer. Do not open makemore part 3.

---

## 1. Goal for today

**ML block (09:00–12:00): catch up what is red, then write the proof lines**
- Part 2 is closed, for this week, if Friday’s K13 exists: the flat-guess share beside the next-character counts, and the same-vector check. If it does, do not touch the table. If it does not, K13 is the catch-up. No hidden layer. No makemore part 3.
- Géron **ch.6–7** only. One exercise, and only the earliest blank among G10–G14. If none is blank, do not add another.
- **Eval table v1:** the rows you have, and any score a local **RAGAS** run already returned. A blank stays blank. Not TruLens. Do not invent a score.
- Gold reaches **50 today**. Stop at 50. Stop at 12:00.
- One sentence on what is still fuzzy. You do not start that work.
- The privacy line, if it was never written: no child, nephew, or other private personal data.

---

## 2. Where you are

Friday’s bar was the flat guess set beside the counts, and a check that one character in two blocks returned the same vector. A hidden layer was refused. G14 was a hard vote, and only if G10–G13 were already written. A new eval row was allowed only when a run returned a score.

The week, already on the page, not today’s new work: Monday a context window on paper; Tuesday a tiny embedding table and one lookup; Wednesday more rows or a flat-guess loss; Thursday that loss beside each block; Friday the share against the counts. This lecture does not re-teach those.

The eval table is v1. Today you name the real RAGAS numbers you have. Gold is whatever count you carried in. The target is 50 before noon.

`03-makemore-gpt/` stays the code home. The hidden layer stays shut. Part 3 stays shut. The week-2 one-layer net stays closed. The week-2 RAGAS slice stays frozen.

Upskill week 3 closes today: Géron ch.6–7 at the prompts already issued, makemore part 2 at the lookup and the flat-guess loss, 50 gold questions, eval table v1 with real RAGAS scores where a run returned them, the privacy line, and one fuzzy sentence you are not chasing.

---

## 3. Concepts to use (nothing new to derive)

**The lookup close**
- Usable, for this week, means a small embedding table you filled, a few blocks looked up, a flat-guess loss that does not change with the block, and Friday’s two columns (share and count). That is the opening of part 2. It is not a hidden layer, and it is not part 3.
- If K13 is missing, write it by doing Friday’s K13, and only after K11 exists. If K11 is missing, the earliest blank of K8, K9, or K11 is the catch-up instead. If K13 exists, leave the table alone.
- The proof paragraph is four things: the flat-guess share, what the counts did, the same-vector line, and the three refusals (hidden layer, part 3, private names). The picture of the two columns stays Friday’s board. It stays `slides later`.
- One sentence names what is still fuzzy. The usual honest answer is the hidden layer you did not build, or a score cell a run never filled. You write the sentence. You do not start the work.

**Géron ch.6–7, close (concepts).** The exercises already issued are the clusters. Do not invent another:
- G10: one split, two branches, and why a deep tree memorizes.
- G11: Gini or entropy, and a pure leaf.
- G12: a class share at a leaf, invented.
- G13: a regression leaf, the mean of three invented numbers.
- G14: a hard vote, the majority of three invented labels.
- If one of those notes is blank, that earliest blank is the only exercise. If none is blank, one line each is the close. Not bagging, not boosting, not stacking. Do not fit a new model.

**Eval table v1 (RAGAS).** A real cell is a number a local RAGAS run returned, with a chunking choice, an embedding choice, a gold slice, and a metric name. If you have those, the proof line names the table and says you will not retune the week-2 slice from it. If you have none, one run this morning is the catch-up, and you write only numbers it returns. A blank stays blank. Not TruLens. The formulas and the judge prompt stay `slides later`.

**Gold and privacy.** The file hits 50 today. One item the corpus should refuse stays in the set. Do not write a 51st. If the privacy line is missing, write it: no child, nephew, or other sensitive personal data in gold or in the lookup rows. Commit text you write, not PDFs, not secrets, not `.env`.

---

## 4. ML block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | W1, then W2. If K13 is missing, do the catch-up. If it exists, the proof paragraph and do not touch the table. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–11:05 | W3 and W4. The earliest blank Géron exercise, or one line each. RAGAS proof, or one real run if the table has no number. The fuzzy sentence. Privacy line if it is missing. |
| 11:05–12:00 | W5. Gold until the file has 50. Hard stop 12:00. |

**Prompts (you write anything that is still missing):**
- **W1.** In `notes/`, five lines: gold count; K13 written or not; the earliest blank of G10–G14, or “none”; whether any eval-table v1 cell is a real RAGAS number; privacy line written or not.
- **W2.** If K13 is missing, do K13, and if K11 is also missing do the earliest blank of K8, K9, or K11 instead, and stop the makemore slot there. If K13 exists, do not change the table. One paragraph: the flat-guess share, what the counts did, the same-vector line, and the three refusals (hidden layer, part 3, private names). Then one sentence on what is still fuzzy. Do not start it.
- **W3.** If W1 names one blank exercise, do that exercise and no other. If it says “none”, one line each for G10–G14, in your own words. Not bagging, not boosting, not stacking. No new exercise.
- **W4.** If the eval table has no real RAGAS number, one local run, and write only numbers it returns. If numbers exist, one line: the v1 slice you will leave alone, and that you will not retune the week-2 slice from it. Do not invent a score. Do not add a blank row to make the table look finished. Not TruLens. Do not commit a key. If the privacy line is missing, write it.
- **W5.** Append gold items you write yourself until the file has 50, or until 12:00. Keep a mix of types, and keep at least one item the corpus should refuse. If the count is already 50, do not add another.

---

## 5. Evening

There is no evening block. From 12:00 the day is free. Do not open a 19:00–22:00 study session. 22:00–23:00 is not a Saturday slot.

| Time | Activity |
| --- | --- |
| 12:00 onward | No study. |

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Did you change the embedding table today? If yes, was K13 missing when you started?
2. Which of G10–G14 was blank at 09:00, or were all five already written?
3. Is every RAGAS number in the close table one a run returned, and what did you name as still fuzzy?
4. What is the gold count at 12:00, and is the privacy line written?

---

## 7. Pointers

- **makemore:** Friday’s K13 is the week-3 close. Do not open the hidden layer. Do not open part 3.
- **Géron:** *Hands-On Machine Learning*, ch.6 and ch.7, only to fill the earliest blank of G10–G14. Not a new cluster.
- **Evals:** **RAGAS** only. Real scores. Not TruLens. The v1 slice you name in W4 is the one you leave alone.
- **Gold:** 50 today (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 2 (YouTube)](https://www.youtube.com/watch?v=TCH_1BHY58I)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 3 (19–24 Oct):* ☐ Géron ch.6–7 ☐ makemore part 2 ☐ gold 50 by Sat 24 Oct ☐ eval table v1 (RAGAS) ☐ no child/nephew data in trains or gold
