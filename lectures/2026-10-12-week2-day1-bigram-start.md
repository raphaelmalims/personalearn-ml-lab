# Lecture — 2026-10-12 · Upskill week 2, day 1: bigram start

> **Upskill week 2** (Mon 12 – Sat 17 Oct 2026), day 1. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the code, the score row, and every gold question.

Saturday’s lecture: [`2026-10-10-week1-day6-week-close.md`](2026-10-10-week1-day6-week-close.md). Week 1 is closed. Today opens week 2. It does not finish it.

---

## 1. Goal for today

**Morning (09:00–12:00): the first slice of makemore part 1**
- A character-level model predicts the next character. A bigram is one pair of characters.
- You can say what one cell of a count table means, including a start and an end. You do not normalize the row, sample, or build a neural net.

**Evening (19:00–22:00): ch.3 opens, and a score is allowed**
- Géron **ch.3** only, one cluster: a classification decision, and precision versus recall. One exercise. Ch.4 stays shut.
- **RAGAS** scores are allowed from this week. Tonight you open the table. One number is the door, not the baseline. Not TruLens.
- Gold moves from 20 toward **30 by Sat 17 Oct**. A few items, not all ten.
- No child, nephew, or other private personal data in a training file or in the gold set.

---

## 2. Where you are

Week 1 left a micrograd you can run on a short list, Géron ch.1–2 (G1–G4), a four-line RAGAS card with no numbers, an inventory of metadata, and a gold file aimed at 20. Do not extend that net. Do not reopen ch.1–2 unless a G1–G4 note is still blank. If the gold count is under 20, the first evening minutes finish 20, then you add toward 30.

`03-makemore-gpt/` is the week-2 code home. `04-rag-evals/` and `evals/` are where a score table may live. The copy of `01-micrograd/value.py` on `main` is still the forward stub. Leave it.

Upskill week 2, still open after today: Géron ch.3–4, makemore part 1, gold to 30, a RAGAS baseline with scores, the privacy line.

---

## 3. Concepts to use (you do not paste a finished notebook)

**Makemore part 1, the opening only**
- The unit is a character, not a word. The training question is: given this character, what tends to come next?
- A bigram is an ordered pair of characters. You invent a start marker and an end marker so a name has a beginning and a stop.
- A count table has one row and one column per character in the vocabulary, markers included. A cell is how often that pair occurred in the strings you typed. Today the cell is a count. A probability is that count divided by its row, and you are not required to divide yet.
- Sampling will draw the next character from one row. The picture from counts to a draw is `slides later`.
- The loss you will meet later in part 1 has a name: negative log likelihood. Do not derive it today.
- A one-layer network that replaces the table is still part 1, and it is not this morning.
- Strings you type are made-up, or a public list you add later. They are not the name of a child, a nephew, or anyone private.

**Géron ch.3, one cluster (concepts).** Ch.1–2 already chose a measure and left the gold file as the untouched test. Ch.3 is classification:
- The output is a class, not a quantity. For PersonaLearn the class can be “answer” versus “refuse”, or “in the corpus” versus “not”.
- Accuracy is still a poor default when one class is rare. Ch.3’s names for the two errors: precision (of the cases you called positive, how many were) and recall (of the true positives, how many you caught). You pick which miss is worse before you fit.
- A threshold moves you along that tradeoff. Name it. Do not tune one.
- Error analysis, multiclass, and a confusion matrix you fill in are later this week. Ch.4 (fitting a line, gradient descent, regularization as a training tool) stays shut. Not ch.5.

**Baseline scores (RAGAS).** Week 1 forbade numbers. Week 2 allows them, on a slice you label as dev, not as the final report.
- One row is: gold id, metric name, the number, and which of question, answer, contexts, and reference you passed in.
- One item and one metric is enough to prove the path. The baseline for the week is more than that, and it is not tonight’s job.
- You do not change chunk size, prompt, or model because of that single number. The gold file as a whole stays the report-once set from G3.
- RAGAS only. The metric formulas and the judge prompt stay `slides later`.

**Gold and privacy.** Schema unchanged. Toward 30 by Saturday, with a mix of types and at least one refuse. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data in gold or in anything you would train.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Bigram on paper: vocabulary, markers, what one cell means. A few made-up strings. No neural net. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Say what sampling will be, name the loss, and stop. If gold is under 20, note the count for tonight. Do not start ch.4. |

**Prompts (you write the code):**
- **P1.** In `notes/`, five made-up strings, a vocabulary list, and the two markers. State what a bigram is in one sentence. No downloaded names. No private names.
- **P2.** Draw the count table’s axes. Label one cell in words (which pair, what the integer will mean). Leave the integers blank or fill only the pairs you can see in P1 by counting yourself. Do not copy a matrix from the makemore repo.
- **P3.** Two sentences: how a later sample would use one row, and the name of the loss you are not deriving today. Then stop. No network. No training loop.

Open the makemore repo only after P2, and only to compare a picture. Do not paste its counts.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Géron ch.3, classification and precision versus recall, then the single exercise below. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | RAGAS: the score-table header, and at most one number. Privacy line on the gold file and on P1. |
| 21:20–22:00 | Gold toward **30 by Sat 17 Oct**. If the count is under 20, this slot finishes 20 first. Stop at 22:00. |

**Géron ch.3 — one exercise for the cluster**
- **G5.** Pick one PersonaLearn decision that is a class, using a gold item you already have or one you will add tonight. In your notes: (1) the classes, and which one is the positive; (2) why accuracy fails if that positive is rare; (3) which of precision or recall you refuse to drop, in a sentence a non-ML teammate would accept; (4) the line you will not cross tonight — no fit, no threshold search, no use of the full gold file to choose the threshold. Not ch.4.

**Scores, privacy, gold (prompts only):**
- **B1.** Create the score-table header in `evals/` or `notes/`: gold id, metric, score, inputs used. Leave the score blank, or, if RAGAS already runs locally without a new secret, write one number for one gold item and one metric. Label the row `dev`. Do not retune anything from it. Do not add TruLens. Do not commit a key.
- **B2.** One line in `notes/`: the gold file and P1 contain no child, nephew, or other private personal data. If a row would need that, delete the row.
- **B3.** Append gold items you write yourself. If you are under 20, reach 20 before you count toward 30. A few new items is enough. Keep a mix of types, and keep at least one refuse. The week target stays 30 by Saturday.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What does one cell of the bigram table mean, and what three things did you refuse to build this morning?
2. For your G5 positive class, which error is precision about, and which is recall about?
3. If you wrote a score, why is that row not a licence to change chunk size?
4. What personal data is banned from gold and from the strings you train on?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 1, the bigram section, after P2. Stop before the neural net.
- **Géron:** *Hands-On Machine Learning*, ch.3, classification measures. One exercise (G5). Not ch.4 today. Ch.4 is later this week.
- **Evals:** **RAGAS** only. First scores are allowed in week 2. Tonight is at most one dev number. Not TruLens.
- **Gold:** 30 by Sat 17 Oct, then 50 by Sat 24 Oct (see `gold/README.md`). Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 1 (YouTube)](https://www.youtube.com/watch?v=PaCmpygFfXo)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 2 (12–17 Oct):* ☐ Géron ch.3–4 ☐ makemore part 1 ☐ gold 30 by Sat 17 Oct ☐ RAGAS baseline scores ☐ no child/nephew data in trains or gold
