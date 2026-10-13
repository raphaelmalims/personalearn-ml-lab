# Lecture — 2026-10-14 · Upskill week 2, day 3: bigram loss

> **Upskill week 2** (Mon 12 – Sat 17 Oct 2026), day 3. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the score rows, and every gold question.

Yesterday’s lecture: [`2026-10-13-week2-day2-bigram-sample.md`](2026-10-13-week2-day2-bigram-sample.md). The week targets do not change. Today does not finish them.

---

## 1. Goal for today

**Morning (09:00–12:00): the count model’s loss, then one layer only if that loss is a number**
- If yesterday’s samples are missing, finish the normalized rows and the draws first.
- If they exist, put one negative log likelihood on the strings the table was built from. You derive it. You do not paste it.
- A single layer, character in and next-character scores out, starts only after that number exists. No hidden layer. No MLP.

**Evening (19:00–22:00): the rest of ch.4 that is still open, more scores, gold**
- If G6 is blank, write it. That is the open cluster, and you do not start another.
- If G6 is written, one remaining ch.4 cluster: a learning curve, and a penalty on the parameters. One exercise.
- **RAGAS** only. More dev numbers if a run needs no new secret. Still not the Saturday report. Not TruLens.
- Gold keeps moving toward **30 by Sat 17 Oct**.
- No child, nephew, or other private personal data in the strings, the layer, or the gold file.

---

## 2. Where you are

Tuesday’s bar was a normalized bigram row and a few sampled strings. The loss was still only a name. A neural net was refused.

G6, if you wrote it, is the ch.4 note on a step against the gradient. Learning curves, a penalty, and polynomial features were left shut. The score table is a few `dev` cells, not a baseline. Gold is between 20 and 30.

`03-makemore-gpt/` is the code home. Leave the week-1 micrograd net closed.

Upskill week 2, still open after today: whatever of ch.4 you did not reach, the rest of makemore part 1 after this single layer, gold to 30, a fuller RAGAS baseline, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**Negative log likelihood of the count model**
- Each bigram in a training string already has a probability: the entry in that character’s normalized row. The model’s loss is how unsurprised it was, turned into one number you can compare.
- You bring those probabilities together yourself. A product of tiny probabilities underflows. The log is the way through, and the sign is chosen so a better model gets a smaller loss. Derive that. The board of the sum is `slides later`.
- Average or sum, say which, and use the same choice on every string. A lower number means the table assigned more probability to the bigrams that actually occurred.
- This loss is on the count model. It is not a reason to build a network yet. If you cannot name the number, the layer waits.
- Strings stay made-up or public. Not a child, a nephew, or anyone private.

**One layer, only after that number**
- The layer maps one character to a score for each possible next character. One weight matrix. No second layer.
- A score is not yet a probability. The step that turns scores into probabilities has a name, softmax. Name it. If you have not finished the count-model loss, do not implement it.
- Training that layer is a later sitting. Today, if you start it at all, is one forward on one character. No hidden units. No MLP. No full part-1 training loop.

**Géron ch.4, the cluster that is still shut (concepts).** G6 was the step. This cluster is how you tell that a fit is too eager:
- A learning curve plots the training loss and a held-out loss as you add data, or as you take more steps. The training loss falling alone is not the report.
- The held-out slice is not the full gold file. It is a few rows you already set aside, in the same spirit as G3.
- A penalty (regularization) adds something to the loss that grows when parameters grow. The fit then prefers smaller parameters. Name ridge or lasso if you meet them. Do not code either.
- Polynomial features are one way a line becomes flexible enough to need that curve. Name them. Do not expand a feature matrix tonight.
- Not ch.5.

**Baseline scores (RAGAS).** Add numbers, not a new library. A handful of `dev` cells is more baseline than one cell, and it is still not the score you would quote. Do not change chunk size, prompt, or model from today’s table. Formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Toward 30 by Saturday. Under 20, finish 20 first. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on Q3. If the samples are missing, finish Q2–Q3. If they exist, compute the count-model loss. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | The single layer only if N2 is a number you computed. Otherwise stay on the loss. Stop before a hidden layer. |

**Prompts (you write the code):**
- **N1.** In `notes/`, one line: Q3 exists, or it does not. If it does not, do Q2–Q3 and do not start N2.
- **N2.** For the training strings, turn each bigram’s row-entry into one loss. Say whether you summed or averaged, and write the number. One sentence: what a smaller number means. Do not paste a loss function from the makemore repo.
- **N3.** Only if N2 has a number: one matrix, one character in, one score per next character, one forward. Name softmax and do not build a second layer. If N2 has no number, write “layer waiting” and stop.

Open the makemore repo only after N2, to compare the shape of the loss. Do not paste it.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | If G6 is blank, write G6 and stop the new cluster. If G6 exists, learning curves and a penalty, then the exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | RAGAS: more `dev` numbers if a run is ready. Privacy line on N2’s strings and on gold. |
| 21:20–22:00 | Gold toward **30 by Sat 17 Oct**. Under 20, finish 20 first. Stop at 22:00. |

**Géron ch.4 — one exercise for the cluster**
- **G7.** Only if G6 is already written. In your notes: (1) what the two curves are (train, and a held-out slice that is not the full gold file); (2) one sign, in words, that the fit is memorizing; (3) the name of a penalty and what it does to large parameters; (4) the line you will not cross tonight — no fitted penalty, no feature expansion, no ch.5. If G6 is blank, G7 waits and G6 is the evening’s exercise.

**Scores, privacy, gold (prompts only):**
- **B7.** If RAGAS runs locally without a new secret, add dev numbers until the table has several cells (more than one id, or more than one metric). If it does not run, do not invent a number. Do not retune anything. Do not add TruLens. Do not commit a key.
- **B8.** One line: the strings in N2 and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would.
- **B9.** Append gold items you write yourself. A few toward 30. Keep a mix of types, and keep at least one refuse. The week target stays 30 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What does a smaller count-model loss mean, and why did you use a log?
2. Why was the layer not allowed to start before N2, and why is that layer not an MLP?
3. What are the two lines on your learning curve, and what does a penalty push the parameters toward?
4. How many RAGAS numbers are in the dev table, and why is that table not the report you would quote?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 1, the loss section, after N2. The network section only after that number exists. Stop before a hidden layer.
- **Géron:** *Hands-On Machine Learning*, ch.4, learning curves and regularization. One exercise (G7), or G6 if it is still blank. Not ch.5.
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
