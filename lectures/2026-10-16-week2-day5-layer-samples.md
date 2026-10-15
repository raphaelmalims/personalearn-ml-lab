# Lecture — 2026-10-16 · Upskill week 2, day 5: sample the layer

> **Upskill week 2** (Mon 12 – Sat 17 Oct 2026), day 5. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the score rows, and every gold question.

Yesterday’s lecture: [`2026-10-15-week2-day4-one-layer-train.md`](2026-10-15-week2-day4-one-layer-train.md). The week targets do not change. Saturday is the close. Today does not finish it, and it does not open part 2.

---

## 1. Goal for today

**Morning (09:00–12:00): names from the trained layer, next to the count model**
- If N6 did not run, the morning is still those few training steps. Do not sample an untrained matrix.
- If it did, draw a few strings from that same layer and set them beside the count-model strings. Write the loss comparison if it is not already a sentence. No hidden layer. No MLP. Not makemore part 2.

**Evening (19:00–22:00): one open Géron cluster, real scores, gold**
- If any of G6, G7, or G8 is blank, write the earliest blank one. Do not stack a new exercise on top.
- If those three are written, one remaining ch.3 cluster: a confusion matrix you describe and do not fill from a fit. One exercise. Not ch.5.
- **RAGAS** only. Real cells if a run needs no new secret. Not a new tool. Not TruLens.
- Gold keeps moving toward **30 by Sat 17 Oct**. The privacy line gets written if it is still missing.
- No child, nephew, or other private personal data.

---

## 2. Where you are

Thursday’s bar was a few steps on the one matrix, a loss before and after, and one sentence against the count-model loss N2. Sampling from that trained layer was left open. A hidden layer was refused.

G8, if you wrote it, is logistic regression and softmax with no fit. The score table is `dev` cells you have not quoted as the week’s baseline. Gold is still on the way to 30.

`03-makemore-gpt/` is the code home. Part 2 stays shut. The week-1 micrograd net stays closed. Saturday’s lighter block is the catch-up, not a new model.

Upskill week 2, still open after today: gold to 30, a baseline you are willing to leave alone, any Géron note that is still blank, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**Sample the layer you already trained**
- The draw is the same shape as the count-model sample: start at the start marker, take the row for the current character, draw the next one, stop at the end marker. The row now comes from the layer’s probabilities, not from the count table.
- You already turned scores into that row. Do not derive softmax again. The picture of the draw stays `slides later`.
- Put the new strings next to the count-model strings. Say, in words, which set looks closer to the strings you trained on. That is not a metric.
- The loss comparison is two numbers you already have, or that you compute if the sentence is missing: N2, and the layer’s loss after the last step. Closer is interesting. Equal is not required.
- More steps are allowed only to finish N6 if it never ran. A longer training run is not today’s slice.
- A hidden layer, an embedding, and more than one previous character are part 2. Not today.
- New strings are still from made-up or public training text. Not a child, a nephew, or anyone private.

**Géron, the cluster that is still open (concepts).** G5 through G8, when written, already covered the measure, the step, the learning curve, and softmax. What ch.3 still has not asked you to write is how you would look at the errors:
- A confusion matrix is four cells for a two-class decision: the positive you catch, the positive you miss, the negative you call positive, the negative you correctly leave. You name the cells. You do not fill them from a fitted model.
- The cell you would inspect first is the one your G5 choice already called the worse miss. Say which, and why, in one sentence.
- Not ch.5. Not a hidden layer.

**Baseline scores (RAGAS).** Real cells: a number that a local RAGAS run actually returned, on a gold id, for a metric you can name. If the run does not happen, the cell stays blank. You do not invent the number, and you do not install a second library. The table stays `dev`. You still do not retune chunk size, prompt, or model from it. Saturday can decide whether this slice is the one you quote. Formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Toward 30 by tomorrow. Under 20, finish 20 first. Do not write a 31st. If the privacy line was never written, write it tonight. No child, nephew, or other sensitive personal data in gold, in the training strings, or in the new samples. Commit text you write, not PDFs, not secrets, not `.env`.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on N6. If it did not run, finish N4–N6 and stop the new work. If it did, sample from the layer. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Set those strings beside the count-model strings. Write the loss comparison. Stop before a hidden layer. |

**Prompts (you write the code):**
- **N7.** In `notes/`, one line: N6 ran, or it did not. If it did not, do N4–N6 and do not start N8.
- **N8.** Draw a few strings from the trained layer, start marker to end marker. Write them next to the count-model strings. One paragraph: N2’s loss, the layer’s latest loss, and which set of strings looks closer to the training text. Then stop. No extra training run. No hidden layer. No part 2. No private names.

Open the makemore repo only after N8, to compare a picture of sampling from the layer. Do not paste its sampler.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | If G6, G7, or G8 is blank, write the earliest one and stop. If all three exist, the confusion matrix, then the exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:15 | RAGAS: real `dev` cells only. Privacy line if it is still missing. |
| 21:15–22:00 | Gold toward **30 by Sat 17 Oct**. Under 20, finish 20 first. Stop at 30. Stop at 22:00. |

**Géron ch.3 — one exercise for the cluster**
- **G9.** Only if G6, G7, and G8 are already written. For the two classes from G5, in your notes: (1) the four cells, named, not filled from a fit; (2) which cell you would read first, tied to the precision or recall choice you already made; (3) why a fitted model is not how you fill that matrix tonight; (4) not ch.5, and not a hidden layer. If an earlier G is blank, G9 waits.

**Scores, privacy, gold (prompts only):**
- **B13.** Where a local RAGAS run needs no new secret, write the number it returned. One cell is a gold id, a metric, and that number, labeled `dev`. Add cells you can actually run. If it does not run, leave the score blank. Do not invent it. Do not add a tool. Do not retune anything. Do not commit a key.
- **B14.** If the privacy line is missing, write it: no child, nephew, or other private personal data in the gold file, the training strings, or N8’s samples. If a row would need that, delete it. If the line already exists, add N8 to it in one sentence.
- **B15.** Append gold items you write yourself until you are closer to 30, or until 22:00. Keep a mix of types, and keep at least one refuse. The week target stays 30 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What did you sample from, and what did you refuse to add?
2. Where does the layer’s latest loss sit next to N2, in one sentence?
3. Which Géron exercise was blank at 19:00, or did you write G9?
4. How many real RAGAS numbers are in the table, and is the privacy line written?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 1, sampling from the trained one-layer model, after N7. Stop before part 2. Saturday does not open part 2 either.
- **Géron:** *Hands-On Machine Learning*, ch.3, the confusion matrix, only if G6–G8 exist. Otherwise the earliest blank exercise. Not ch.5.
- **Evals:** **RAGAS** only. Real cells. Not TruLens. Saturday can freeze what you quote.
- **Gold:** 30 by Sat 17 Oct, then 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 1 (YouTube)](https://www.youtube.com/watch?v=PaCmpygFfXo)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 2 (12–17 Oct):* ☐ Géron ch.3–4 ☐ makemore part 1 ☐ gold 30 by Sat 17 Oct ☐ RAGAS baseline scores ☐ no child/nephew data in trains or gold
