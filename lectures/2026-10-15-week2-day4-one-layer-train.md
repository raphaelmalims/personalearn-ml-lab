# Lecture — 2026-10-15 · Upskill week 2, day 4: train the one layer

> **Upskill week 2** (Mon 12 – Sat 17 Oct 2026), day 4. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the score rows, and every gold question.

Yesterday’s lecture: [`2026-10-14-week2-day3-bigram-nll.md`](2026-10-14-week2-day3-bigram-nll.md). The week targets do not change. Today does not finish them.

---

## 1. Goal for today

**Morning (09:00–12:00): train the one layer, and stop there**
- If N2 is not a number, the morning is still the count-model loss. Do not train.
- If the forward in N3 is missing, do that forward, then train only if it runs.
- A few steps on that same matrix: scores, then probabilities, then the same kind of loss as N2. No hidden layer. No MLP. Not makemore part 2.

**Evening (19:00–22:00): the next ch.4 cluster only if the last one is written**
- If G7 is blank, write the earliest blank of G6 or G7. Do not start a new exercise on top.
- If G7 exists, one cluster: logistic regression and softmax as the way a score becomes a class probability. One exercise. Not ch.5.
- **RAGAS** only. More `dev` numbers if a run needs no new secret. You still do not quote the table. Not TruLens.
- Gold keeps moving toward **30 by Sat 17 Oct**.
- No child, nephew, or other private personal data in the training strings or the gold file.

---

## 2. Where you are

Wednesday’s bar was a count-model negative log likelihood (N2), and one forward of a single matrix (N3) only after that number existed. Softmax was a name. Training was a later sitting. A hidden layer was refused.

G6 is the step against the gradient. G7, if you wrote it, is the learning curve and the penalty. The score table is a growing set of `dev` cells, not the number you would quote. Gold is still short of 30 unless you already arrived.

`03-makemore-gpt/` is the code home. Part 2 (a hidden layer, several previous characters) stays shut. The week-1 micrograd net stays closed.

Upskill week 2, still open after today: anything in ch.4 you did not reach, sampling from this trained layer if you did not get there, gold to 30, a baseline you would actually quote, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**Train the one layer**
- The matrix is the one from N3: one character in, one score per next character. A score is not a probability. Softmax is the step that makes a row of scores into a row that is non-negative and adds to one. You implement that step. The picture of it is `slides later`.
- The loss is the same idea as N2: how little probability the model gave the next character that actually occurred, brought together with a log so the number stays usable. Use the same sum-or-average choice you already wrote down. Derive it. Do not paste it.
- One training step is a forward, that loss, a step of the matrix against its gradient, then a zero of that gradient. A handful of steps is the bar. Write the loss before the first and after the last.
- The count-model loss from N2 is the comparison, not a target you must hit today. One sentence on whether the layer’s loss moved toward it.
- A hidden layer, an embedding, and a window of more than one previous character are part 2. Not today.
- The strings are still the made-up or public ones. Not a child, a nephew, or anyone private.

**Géron ch.4, logistic and softmax (concepts).** Only if G7 is already written. This is the classification end of the same chapter:
- Logistic regression takes a score and squashes it into a probability for one class. That is the training-model version of the positive class you named in G5. You do not fit it tonight.
- Softmax is the same idea when there are more than two classes. It is also what your layer does for “which character is next.”
- The threshold that turns a probability into a hard decision is still not tuned on the full gold file.
- Not ch.5. Not a second hidden layer in the name of this chapter.

**Baseline scores (RAGAS).** Add cells. Do not invent a number if the run did not happen. The table is still `dev`. Quoting it as the week’s baseline is a later sitting, once you have decided the slice and left it alone. Do not change chunk size, prompt, or model from today’s new cells. Formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Toward 30 by Saturday. Under 20, finish 20 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on N2 and N3. Loss first if N2 is missing. Forward if N3 is missing. Then softmax and the layer’s loss. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | A few training steps on that one matrix. Compare to N2 in one sentence. Stop before a hidden layer. |

**Prompts (you write the code):**
- **N4.** In `notes/`, two lines: N2 is a number, or it is not; N3 ran, or it did not. If N2 is not a number, do N2 and stop. If N3 did not run, do N3 before N5.
- **N5.** Turn the layer’s scores into probabilities. Compute one loss on the same bigrams as N2, with the same sum-or-average choice. Write the number. Do not paste the makemore loss.
- **N6.** A handful of steps. Zero the gradient each step. Write the loss before the first step and after the last, the step size you chose, and one sentence against N2. Then stop. No hidden layer. No wider context. No part 2. No private names.

Open the makemore repo only after N6, to compare the shape of the training step. Do not paste its loop.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | If G7 is blank, write the earliest blank of G6 or G7 and stop. If G7 exists, logistic regression and softmax, then the exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | RAGAS: more `dev` numbers if a run is ready. Privacy line on the training strings and on gold. |
| 21:20–22:00 | Gold toward **30 by Sat 17 Oct**. Under 20, finish 20 first. Stop at 22:00. |

**Géron ch.4 — one exercise for the cluster**
- **G8.** Only if G7 is already written. In your notes: (1) logistic regression in one sentence, for the positive class from G5, with no fit; (2) softmax in one sentence, and how it is the same step as N5; (3) why you will not pick the decision threshold from the full gold file; (4) the line you will not cross — no fitted logistic model, no ch.5, no hidden layer. If G7 is blank, G8 waits.

**Scores, privacy, gold (prompts only):**
- **B10.** If RAGAS runs locally without a new secret, add `dev` numbers on ids or metrics you did not already score. If it does not run, do not invent a number. Do not retune anything. Do not quote the table as the week’s baseline. Do not add TruLens. Do not commit a key.
- **B11.** One line: N6’s strings and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would.
- **B12.** Append gold items you write yourself. A few toward 30. Keep a mix of types, and keep at least one refuse. The week target stays 30 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What did one training step change, and why is there still no hidden layer?
2. What are you comparing when you put N6’s loss next to N2’s?
3. If G7 was blank at 19:00, which exercise did you write, and which one did you leave waiting?
4. What is banned from the training strings, and what will you not retune from today’s RAGAS cells?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 1, the one-layer network, after N4. Stop before part 2.
- **Géron:** *Hands-On Machine Learning*, ch.4, logistic regression and softmax. One exercise (G8), or the earliest blank of G6 or G7. Not ch.5.
- **Evals:** **RAGAS** only. More dev numbers when a run is ready. Not TruLens. The baseline you would quote is still later this week.
- **Gold:** 30 by Sat 17 Oct, then 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 1 (YouTube)](https://www.youtube.com/watch?v=PaCmpygFfXo)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 2 (12–17 Oct):* ☐ Géron ch.3–4 ☐ makemore part 1 ☐ gold 30 by Sat 17 Oct ☐ RAGAS baseline scores ☐ no child/nephew data in trains or gold
