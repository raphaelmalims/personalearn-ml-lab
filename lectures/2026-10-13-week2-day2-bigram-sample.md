# Lecture — 2026-10-13 · Upskill week 2, day 2: sample the bigram

> **Upskill week 2** (Mon 12 – Sat 17 Oct 2026), day 2. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the score rows, and every gold question.

Yesterday’s lecture: [`2026-10-12-week2-day1-bigram-start.md`](2026-10-12-week2-day1-bigram-start.md). The week targets do not change. Today does not finish them.

---

## 1. Goal for today

**Morning (09:00–12:00): turn counts into a few sampled names**
- If Monday’s count table is still missing, build that first. Do not sample an empty page.
- If the counts exist, each row becomes a distribution, and you draw a few strings from the start marker until the end marker. Still no neural net.

**Evening (19:00–22:00): ch.4 opens, scores grow by more than one cell**
- If G5 is blank, write it. That closes yesterday’s ch.3 cluster. Do not add a second ch.3 exercise.
- Géron **ch.4**, one cluster: fitting, and a step of gradient descent. One exercise. The rest of the chapter stays shut.
- **RAGAS** only. If a run is ready, more than one dev cell. If it is not, grow the header and stop. Not TruLens.
- Gold keeps moving toward **30 by Sat 17 Oct**.
- No child, nephew, or other private personal data in samples, trains, or gold.

---

## 2. Where you are

Monday’s bar was a bigram count table on paper: vocabulary, start and end markers, and what one cell means. Normalizing a row, sampling, and a neural net were outside Monday. The loss has a name, negative log likelihood, and you did not derive it.

G5 is the ch.3 note on precision versus recall. The score table has a header and at most one dev number. Gold is on the way from 20 to 30, not at 30.

`03-makemore-gpt/` is still the code home. Leave `01-micrograd/value.py` on `main` as the forward stub. The week-1 net is closed.

Upskill week 2, still open after today: the rest of Géron ch.3–4, the rest of makemore part 1, gold to 30, a fuller RAGAS baseline, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**From counts to a draw**
- A probability row is the same counts, each divided by the row sum, so the entries are non-negative and add to one. You do that division. You do not copy a matrix.
- A row that sums to zero cannot be divided. Write what breaks. The usual fix has a name, smoothing. Look it up if you need it. Do not paste a smoothed table.
- Sampling starts at your start marker, draws the next character from that row, and repeats until the end marker. A few strings is the bar. The picture of the draw stays `slides later`.
- Negative log likelihood stays a name. Do not derive it, and do not train.
- The one-layer network that replaces this table is still later in part 1. Not this morning.
- Strings you sample are from made-up counts, or from a public list you already chose. They are not a child, a nephew, or anyone private.

**Géron ch.4, one cluster (concepts).** G5, if you wrote it, already picked a positive class and a precision/recall preference. Ch.4 is how a model is fit:
- Parameters are the numbers you are allowed to change. A loss is a single number that says how bad those parameters are on the rows you fit. Fitting moves the parameters so that number gets smaller.
- For a straight line, a closed form exists. Name it. Do not derive it.
- Gradient descent starts at a guess and takes a small step against the gradient, then repeats. One step is the same idea as the week-1 parameter step. You are not re-deriving the chain rule.
- A learning rate that is too large walks off the bowl. One that is too small barely moves. The bowl picture is `slides later`.
- Batch, stochastic, and mini-batch are three ways to choose which rows enter one step. Name them. Do not code all three.
- Polynomial features, learning curves, and regularization as a training tool are the rest of ch.4. They stay shut. Not ch.5.

**Baseline scores (RAGAS).** Yesterday’s single dev number, if you have it, is the door. Today the table has more than one cell when a local run needs no new secret.
- Another gold id, or a second metric on the same id. Still labeled `dev`. Still not the week’s baseline, and still not a reason to change chunk size, prompt, or model.
- The full gold file stays the report-once set. RAGAS only. Formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 30 by Saturday. If you are under 20, finish 20 before you count the new items. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data in gold, in P1, or in the strings you sample.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on Monday’s table. If it is missing, do P1–P2. If it exists, normalize every row. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Sample a few strings. Stop before a neural net and before the loss derivation. |

**Prompts (you write the code):**
- **Q1.** In `notes/`, one line: P2 exists, or it does not. If it does not, do P1–P2 and only then start Q2.
- **Q2.** Replace each count row with proportions. In one sentence, say what the entries of a finished row add up to, and what you did when a row summed to zero. Do not copy the makemore matrix.
- **Q3.** From the start marker, draw until the end marker. Write down a few strings you actually got. Then stop. No network. No training loop. No private names.

Open the makemore repo only after Q3, to compare a picture of sampling. Do not paste its sampler.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | If G5 is blank, write it first. Then Géron ch.4, fitting and one gradient step, and the single exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | RAGAS: more than one dev cell if a run is ready. Privacy line on the new strings and on gold. |
| 21:20–22:00 | Gold toward **30 by Sat 17 Oct**. If the count is under 20, finish 20 first. Stop at 22:00. |

**Géron ch.4 — one exercise for the cluster**
- **G6.** Use a loss you can describe in one sentence (a line’s error on a few made-up points, or the bigram loss you have not derived). In your notes: (1) which numbers are parameters and which are data; (2) why a step goes against the gradient; (3) what a too-large learning rate does, in words, with no formula copied from the book; (4) the week-1 object that is the same idea (one parameter step, then zero `.grad`). Do not fit a dataset. Do not code three optimizers. Not the rest of ch.4.

**Scores, privacy, gold (prompts only):**
- **B4.** If RAGAS runs locally without a new secret, add at least one more `dev` cell: another gold id, or a second metric on the same id. If it does not run, add the empty cells and leave the scores blank. Do not retune anything. Do not add TruLens. Do not commit a key.
- **B5.** One line: Q3’s strings and any new gold rows contain no child, nephew, or other private personal data. Delete a row that would.
- **B6.** Append gold items you write yourself. Under 20, reach 20 first. A few new items toward 30 is enough. Keep a mix of types, and keep at least one refuse. The week target stays 30 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What do the entries of one normalized row add up to, and what broke if a row was all zeros?
2. What makes a sample stop, and why is there still no neural net?
3. What does one gradient step change, and what does a learning rate that is too large do?
4. How many dev score cells are in the table, and what will you not change because of them?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 1, the sampling section, after Q3. Stop before the neural net.
- **Géron:** *Hands-On Machine Learning*, ch.4, fitting and gradient descent. One exercise (G6). G5 only if it is still blank. Not ch.5. The rest of ch.4 is later this week.
- **Evals:** **RAGAS** only. More than one dev cell when a run is ready. Not the full baseline. Not TruLens.
- **Gold:** 30 by Sat 17 Oct, then 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 1 (YouTube)](https://www.youtube.com/watch?v=PaCmpygFfXo)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 2 (12–17 Oct):* ☐ Géron ch.3–4 ☐ makemore part 1 ☐ gold 30 by Sat 17 Oct ☐ RAGAS baseline scores ☐ no child/nephew data in trains or gold
