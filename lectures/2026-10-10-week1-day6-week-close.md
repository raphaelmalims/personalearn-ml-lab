# Lecture — 2026-10-10 · Upskill week 1, day 6: week close

> **Upskill week 1** (Mon 5 – Sat 10 Oct 2026), day 6. Saturday is the light close: ML **09:00–12:00** EAT only.
> **10-minute break per 90 minutes** inside that block. Hard stop **12:00**. The evening is free. There is no 19:00–22:00 study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write any catch-up code, the inventory row, and every gold question.

Yesterday’s lecture: [`2026-10-09-week1-day5-micrograd-wrap.md`](2026-10-09-week1-day5-micrograd-wrap.md). The week targets do not change. Today is the day they close. Do not open a new topic.

---

## 1. Goal for today

**ML block (09:00–12:00): catch up what is red, then stop**
- Micrograd is closed if Friday’s can/cannot note exists. If it does, reread it. Do not extend the net.
- Géron **ch.1–2** only. One exercise, and only if one of G1–G4 was never written. If all four exist, do not add a fifth.
- **RAGAS** vocabulary only. The four-line card, if it is missing. Still no scores. Baseline RAG scores are **Upskill week 2**.
- PDF inventory: one verified row, or one thin-topic line, and only if the gold file is already at 20.
- Gold reaches **20 today**. Stop at 20. Stop at 12:00.

---

## 2. Where you are

Friday’s bar was a checked 2–2–1 you can call again on a short list of pairs you type, a handful of steps with `.grad` zeroed every step, and a note of what that engine can do and what you refused. Géron G4 was present, data drift, and model rot. The RAGAS card was four lines and no numbers.

The copy of `01-micrograd/value.py` on `main` is still the forward graph (`+` and `*`) plus a stub where `backward` will live. If your working copy does not yet have Friday’s F2 and F3, the first ML hour finishes those and does not go past them.

This lecture does not re-teach the chain rule, a shared weight, `tanh`, zeroing, drift versus rot, or the four metric names. Those are Monday through Friday. Saturday uses them.

Upskill week 1 closes today: micrograd backprop, Géron ch.1–2, eval basics, PDF inventory, 20 gold questions.

---

## 3. Concepts to use (nothing new to derive)

**Spaced review, not a new engine**
- Usable still means the Friday note: the same 2–2–1, a list you type, a few steps, one checked weight, gradients zeroed inside every step. A data loader, an optimizer object, a file of examples, and a real dataset stay refused.
- If that note is missing, write it by doing Friday’s F2 and F3. If it exists, the review is one fuzzy point from the week, in a short paragraph, and then you leave the code alone.
- The repeated-step picture stays Friday’s board. It stays `slides later`. You do not redraw it today.

**Géron ch.1–2, close (concepts).** Stay inside these two chapters. The four exercises already issued are the cluster:
- G1: taxonomy and the eight-step checklist.
- G2: the measure you would ship, overfit versus underfit, the test set you do not touch.
- G3: fit, tune, report-once, and leakage.
- G4: how you would present it, data drift, model rot, and no score this week.
- If one of those notes is blank, that blank is the only exercise. If none is blank, four lines in your own words is the close. Not ch.3. Do not fit anything. Do not score anything.

**Eval basics (RAGAS).** The card is the close. Context recall, faithfulness, answer relevancy, context precision: one line each, the failure and the inputs, no numbers. If Friday’s R12 exists, do not add a metric. An LLM judge is still not the gold set. Do not write a judge prompt. The metric formulas stay `slides later`.

**PDF inventory and gold.** Same columns as Monday. Commit the inventory, not the PDFs. Leave a cell blank rather than guess. The gold file hits 20 today. One item the corpus should refuse stays in the set. Do not write a 21st. The later targets (30 by Sat 17 Oct, 50 by Sat 24 Oct) are not today’s work.

---

## 4. ML block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | S1, then S2. If F3 is missing, finish F2–F3. If F3 exists, one fuzzy paragraph and do not touch the net. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–11:05 | S3 and S4. One blank Géron exercise, or four recap lines. The RAGAS card only if it is missing. |
| 11:05–12:00 | S5. Gold until the file has 20. Inventory only after that, if minutes remain. Hard stop 12:00. |

**Prompts (you write anything that is still missing):**
- **S1.** In `notes/`, four lines: gold count; F3 written or not; which of G1–G4 is blank, or “none”; R12 written or not.
- **S2.** If F3 is missing, do Friday’s F2 and F3 and stop. If F3 exists, do not change the net. One paragraph: the fuzzy point, and the three things you are still refusing (file loader, optimizer class, scores).
- **S3.** If S1 names one blank Géron exercise, do that exercise and no other. If it says “none”, four lines, one per exercise, in your own words. Not ch.3. No scores.
- **S4.** If R12 is missing, write the four lines now. If it exists, leave it. No fifth metric. No numbers. No judge prompt.
- **S5.** Append gold items you write yourself until the file has 20, or until 12:00. Keep a mix of types, and keep at least one item the corpus should refuse. If the count is already 20, do not add another. Then one inventory row you can verify, or one sentence on the thinnest topic, and only if the count is 20 with minutes left. Blank cells stay blank.

---

## 5. Evening

There is no evening block. From 12:00 the day is free. Do not open a 19:00–22:00 study session. 22:00–23:00 is not a Saturday slot.

| Time | Activity |
| --- | --- |
| 12:00 onward | No study. |

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Did you change the net today? If yes, was F3 missing when you started?
2. Which of G1–G4 was blank at 09:00, or were all four already written?
3. Can you name the four RAGAS metrics and one input each, without a number?
4. What is the gold count at 12:00, and is there one item the corpus should refuse?

---

## 7. Pointers

- **micrograd:** Friday’s can/cannot note is the week-1 close. Do not open Karpathy’s training loop to extend it.
- **Géron:** *Hands-On Machine Learning*, ch.1 and ch.2, only to fill a blank G1–G4. Not ch.3.
- **Evals:** **RAGAS** metrics overview, only to fill a blank line on the card. No baseline scores. Not TruLens. First baseline scores are Upskill week 2.
- **Gold:** 20 today. Then 30 by Sat 17 Oct, then 50 by Sat 24 Oct (see `gold/README.md`). Those later counts are not this morning.

## 8. Resources

- [Karpathy — building micrograd (YouTube)](https://www.youtube.com/watch?v=VMj-3S1tku0)
- [karpathy/micrograd (GitHub)](https://github.com/karpathy/micrograd)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [PyTorch — autograd tutorial](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 1 (5–10 Oct):* ☐ micrograd backprop ☐ Géron ch.1–2 ☐ eval basics (RAGAS) ☐ PDF inventory ☐ 20 gold questions by Sat 10 Oct
