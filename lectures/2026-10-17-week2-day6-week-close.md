# Lecture — 2026-10-17 · Upskill week 2, day 6: week close

> **Upskill week 2** (Mon 12 – Sat 17 Oct 2026), day 6. Saturday is the light close: ML **09:00–12:00** EAT only.
> **10-minute break per 90 minutes** inside that block. Hard stop **12:00**. The evening is free. There is no 19:00–22:00 study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write any catch-up code, the score cells, and every gold question.

Yesterday’s lecture: [`2026-10-16-week2-day5-layer-samples.md`](2026-10-16-week2-day5-layer-samples.md). The week targets do not change. Today is the day they close. Do not open part 2.

---

## 1. Goal for today

**ML block (09:00–12:00): catch up what is red, then write the proof lines**
- The one-layer net is closed if Friday’s N8 exists: layer samples next to the count model, and the two losses in one paragraph. If it does, do not train again. If it does not, N8 is the catch-up. No hidden layer. No makemore part 2.
- Géron **ch.3–4** only. One exercise, and only the earliest blank among G5–G9. If none is blank, do not add another.
- **RAGAS** baseline: real numbers already in the table, or a local run that returns them. Not TruLens. Do not invent a score.
- Gold reaches **30 today**. Stop at 30. Stop at 12:00.
- The privacy line, if it was never written: no child, nephew, or other private personal data.

---

## 2. Where you are

Friday’s bar was a few strings from the trained one-layer net, set beside the count-model strings, plus N2 next to the layer’s latest loss. A hidden layer was refused. G9 was the confusion matrix, and only if G6–G8 were already written.

The score table is `dev` cells. Today you either keep the real numbers you have or fill blanks from a run. Gold is whatever count you carried in. The target is 30 before noon.

`03-makemore-gpt/` stays the code home. Part 2 stays shut. The week-1 micrograd net stays closed.

This lecture does not re-teach softmax, the count-model loss, or the ch.4 step. Monday through Friday did that. Saturday uses them.

Upskill week 2 closes today: Géron ch.3–4, makemore part 1 at the one-layer net, 30 gold questions, a RAGAS baseline with real scores, the privacy line.

---

## 3. Concepts to use (nothing new to derive)

**The one-layer close**
- Usable, for this week, means one matrix, a few training steps, a loss you can set next to the count model, and a few strings drawn from the layer. That is part 1. It is not a hidden layer, not an embedding, and not a window of more than one previous character.
- If N8 is missing, write it by doing Friday’s N8, and only after N6 has run. If N8 exists, leave the code alone.
- The proof paragraph is three things: N2, the layer’s latest loss, and which set of strings you are willing to keep. The picture of the draw stays Friday’s board. It stays `slides later`.

**Géron ch.3–4, close (concepts).** The exercises already issued are the clusters. Do not invent another:
- G5: precision versus recall on a class.
- G6: a step against the gradient.
- G7: a learning curve and a penalty.
- G8: logistic regression and softmax, with no fit.
- G9: four cells of a confusion matrix, named and not filled from a fit.
- If one of those notes is blank, that earliest blank is the only exercise. If none is blank, one line each is the close. Not ch.5. Do not fit a new model.

**RAGAS baseline.** A real cell is a number a local RAGAS run returned, with a gold id and a metric name. If you have those, the proof line names the slice and says you will not retune chunk size, prompt, or model from it. If you have none, one run this morning is the catch-up. A blank stays blank. Not TruLens. The formulas and the judge prompt stay `slides later`.

**Gold and privacy.** The file hits 30 today. One item the corpus should refuse stays in the set. Do not write a 31st. The later target (50 by Sat 24 Oct) is not this morning. If the privacy line is missing, write it: no child, nephew, or other sensitive personal data in gold or in the training strings. Commit text you write, not PDFs, not secrets, not `.env`.

---

## 4. ML block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | C1, then C2. If N8 is missing, do it. If it exists, the proof paragraph and do not touch the net. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–11:05 | C3 and C4. The earliest blank Géron exercise, or one line each. RAGAS proof, or one real run if the table has no number. Privacy line if it is missing. |
| 11:05–12:00 | C5. Gold until the file has 30. Hard stop 12:00. |

**Prompts (you write anything that is still missing):**
- **C1.** In `notes/`, five lines: gold count; N8 written or not; the earliest blank of G5–G9, or “none”; whether any RAGAS cell is a real number; privacy line written or not.
- **C2.** If N8 is missing, do N8 (and N6 first if that never ran) and stop. If N8 exists, do not change the net. One paragraph: the two losses, which strings you keep, and the three refusals (hidden layer, part 2, private names).
- **C3.** If C1 names one blank exercise, do that exercise and no other. If it says “none”, one line each for G5–G9, in your own words. Not ch.5. No new exercise.
- **C4.** If the table has no real RAGAS number, one local run, and write only numbers it returns. If numbers exist, one line: the slice you will leave alone, and that you will not retune from it. Do not invent a score. Not TruLens. Do not commit a key. If the privacy line is missing, write it.
- **C5.** Append gold items you write yourself until the file has 30, or until 12:00. Keep a mix of types, and keep at least one item the corpus should refuse. If the count is already 30, do not add another.

---

## 5. Evening

There is no evening block. From 12:00 the day is free. Do not open a 19:00–22:00 study session. 22:00–23:00 is not a Saturday slot.

| Time | Activity |
| --- | --- |
| 12:00 onward | No study. |

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Did you change the net today? If yes, was N8 missing when you started?
2. Which of G5–G9 was blank at 09:00, or were all five already written?
3. Is every RAGAS number in the close table one a run returned?
4. What is the gold count at 12:00, and is the privacy line written?

---

## 7. Pointers

- **makemore:** Friday’s N8 is the week-2 close. Do not open part 2. Do not open Karpathy’s hidden layer to extend it.
- **Géron:** *Hands-On Machine Learning*, ch.3 and ch.4, only to fill the earliest blank of G5–G9. Not ch.5.
- **Evals:** **RAGAS** only. Real scores. Not TruLens. The slice you name in C4 is the one you leave alone.
- **Gold:** 30 today. Then 50 by Sat 24 Oct (see `gold/README.md`). That later count is not this morning.

## 8. Resources

- [Karpathy — makemore part 1 (YouTube)](https://www.youtube.com/watch?v=PaCmpygFfXo)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 2 (12–17 Oct):* ☐ Géron ch.3–4 ☐ makemore part 1 ☐ gold 30 by Sat 17 Oct ☐ RAGAS baseline scores ☐ no child/nephew data in trains or gold
