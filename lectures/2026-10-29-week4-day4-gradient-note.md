# Lecture — 2026-10-29 · Upskill week 4, day 4: gradient note

> **Upskill week 4** (Mon 26 – Sat 31 Oct 2026), day 4. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the note, the one exercise, and the one sentence.

Wednesday’s lecture: [`2026-10-28-week4-day3-activation-check.md`](2026-10-28-week4-day3-activation-check.md). The week targets do not change. Today is the next slice after the activation check. It is not the week close. Batch norm stays shut.

---

## 1. Goal for today

**Morning (09:00–12:00): what the hidden values mean for the gradient**
- If Wednesday’s A6 is missing, that check is the morning. Do not write a gradient note about a picture you did not look at.
- If A6 exists, one sentence: values stuck at the ends leave a small gradient; values in the middle still have room.
- You do not compute a slope. You do not train again. You do not apply batch norm, and you do not add a second hidden layer.

**Evening (19:00–22:00): the next ch.10 cluster, and the page stays unfinished**
- The earliest blank of G10–G16, then G17. If those are written, Géron **ch.10**, one new cluster: a classification output versus a single number. One exercise. No Keras fit.
- **RAG polish:** one line that you will not retune from the kept row without a new **RAGAS** run, and you are not running one tonight. Not TruLens.
- **how-i-measure:** one sentence under the heading that is still a single line. The page is not finished. Saturday is the close.
- Gold stays at **50**. Fill a missing question only if the file is short of 50 or has no refuse. Do not write a 51st.
- No child, nephew, or other private personal data.

---

## 2. Where you are

Wednesday’s bar was a look at the hidden mix after Tuesday’s handful of steps: bunched in the middle, or stuck at the ends. You did not train again. You named batch norm, or a second hidden layer, and you did not apply either.

Tuesday’s step is still the only training: one hidden mix, a loss near the flat-guess loss at the start, a loss after a handful of steps. Monday’s knob was the scale of the last layer. G17, if you wrote it, is one hidden layer versus a deeper stack, and you did not add the layer. R2, if you wrote it, names the kept v1 row or says the polish waits. The how-i-measure page has two paragraphs and one heading still at a single line, if H3 and H4 were written. Gold is at 50, or still short of it.

`03-makemore-gpt/` is still the code home. `evals/` holds v1. `proof/how-i-measure.md` is the one-pager. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.6–7 unless one of G10–G14 is still blank.

Upskill week 4, still open after today: the rest of ch.10, batch norm and whatever part 3 still holds, the last of the one-pager, and Saturday’s close. Gold stays 50 until week 5 freezes the set.

---

## 3. Concepts to use (you do not paste a finished notebook)

**A small gradient, said in one sentence**
- A hidden value stuck at the end of its activation barely changes when the weights change. The gradient through that unit is small. A value in the middle can still move. You already wrote which picture you saw. Today you say what that picture means for the gradient.
- You do not derive the slope. You do not copy a formula. The picture of a tiny gradient stays `slides later`.
- An init that scales with how many inputs a unit has is one named fix. Batch norm is another. You may name either. You apply neither. You do not take more steps.
- Characters stay the ones you already used. Not a child, a nephew, or anyone private.

**Géron ch.10, the next cluster (concepts).** Only if G17 is written and G10–G16 are not blank.
- A classification head ends in one score per class. Your next-character loss is that kind of head: one score per character, and the loss is how little probability the right character got.
- A regression head ends in one number. G13’s leaf was that kind of summary. You do not refit it.
- You write the difference. You do not build a Keras model, and you do not train either head tonight.

**RAG polish, left alone.** The kept row, if you have one, stays the kept row. Tonight’s line is that you will not change chunk size or embedding from it without a new RAGAS number, and you are not collecting one. If the polish was waiting, it still waits. Not TruLens. The week-2 slice stays frozen.

**how-i-measure, still unfinished.** The heading that is still one line gets one sentence. You do not expand it into the page’s last paragraph. Saturday closes the week.

**Gold and privacy.** The set stays at 50. Under 50, finish 50. If a refuse is missing, fix that inside the 50. At 50 with a refuse already in the file, add nothing. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on A6. If it is missing, do that check and stop. If it exists, write what it means for the gradient. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Name a fix you are not applying. Stop before batch norm and before another training run. |

**Prompts (you write the notes):**
- **A7.** In `notes/`, one line: A6 exists, or it does not. If it does not, do A6 (and A4 first if those steps are also missing) and stop. No gradient note on a missing check.
- **A8.** If A6 exists: one sentence. If the hidden values were stuck at the ends, the gradient through them is small. If they were in the middle, there is still room to move. Then one sentence naming a fix you are not applying (an init that scales with the number of inputs, or batch norm). Do not derive a slope. Do not take more steps. Do not add a second hidden layer. No private names.

Open the makemore part 3 video only after A8, and only for the picture of a small gradient. Do not paste the batch-norm section.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Earliest blank of G10–G16, then G17. If those exist, the output cluster and G18. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | One line: no retune tonight. One sentence under the last one-line heading. |
| 21:20–22:00 | Gold stays at 50. Privacy line if it is missing. Stop at 22:00. |

**Géron ch.10 — one exercise for the next cluster**
- **G18.** Only if G17 is written and none of G10–G16 is blank. If one of those is blank, that blank is the exercise and you do not start G18. If G18 is open: in your notes, (1) what your next-character loss is a distribution over; (2) what G13’s leaf reports instead, in one sentence; (3) the line that you are not training either head tonight; (4) the line you will not cross — no Keras model, no new steps.

**Polish, page, privacy, gold (prompts only):**
- **R3.** If R2 is missing, write R2 and stop. If it exists, one line: you will not change chunk size or embedding from that mark without a new RAGAS score, and you are not running one tonight. If the polish was waiting, the line says it still waits. Do not invent a score. Not TruLens. Do not retune the week-2 slice. Do not commit a key.
- **H5.** If H4 is missing, write H4 and stop. If it exists, one sentence under the heading that is still a single line. Do not turn that sentence into a full paragraph. The page stays unfinished. No new RAGAS number.
- **B32.** One line: today’s note, the polish line, and the sentence contain no child, nephew, or other private personal data. If B30 was never written, write that line first.
- **B33.** If the gold count is under 50, append items you write yourself until it is 50. If a refuse is missing, fix that without going past 50. If the file is already 50 and already has a refuse, do not add another.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What did A6’s picture mean for the gradient, and which fix did you leave unapplied?
2. Which Géron prompt did you actually write — a blank of G10–G17, or G18?
3. What did the polish line refuse to change, and which how-i-measure heading is still short?
4. What is the gold count, and what personal data is banned from the note?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 3, the gradient picture, after A8. Stop before batch norm. Saturday is the close, not tonight.
- **Géron:** *Hands-On Machine Learning*, ch.10. The earliest blank of G10–G17; otherwise one exercise (G18, a distribution versus one number). Not a Keras fit today.
- **Evals:** **RAGAS** only. No new score tonight. The week-2 slice stays frozen. Not TruLens.
- **Gold:** stays 50 (see `gold/README.md`). Week 5 freezes the set. Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 3 (YouTube)](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 4 (26–31 Oct):* ☐ Géron ch.10 ☐ makemore part 3 ☐ polish RAG ☐ how-i-measure one-pager ☐ gold stays 50 ☐ no child/nephew data
