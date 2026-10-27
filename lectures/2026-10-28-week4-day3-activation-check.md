# Lecture — 2026-10-28 · Upskill week 4, day 3: activation check

> **Upskill week 4** (Mon 26 – Sat 31 Oct 2026), day 3. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the check, the one exercise, and the one paragraph.

Tuesday’s lecture: [`2026-10-27-week4-day2-first-steps.md`](2026-10-27-week4-day2-first-steps.md). Monday’s lecture: [`2026-10-26-week4-day1-init-loss.md`](2026-10-26-week4-day1-init-loss.md). The week targets do not change. Today is the next slice after the first steps. It does not finish the week.

---

## 1. Goal for today

**Morning (09:00–12:00): look at the hidden mix, do not add a layer**
- If Tuesday’s A4 is missing, those few steps are the morning. Do not diagnose a run you did not take.
- If A4 exists, look at the hidden mix after those steps. Are the values bunched in the middle, or stuck at the ends?
- You write what you see. You do not take another training run. Batch norm stays shut. No second hidden layer.

**Evening (19:00–22:00): the next ch.10 cluster, the kept row, one more paragraph**
- The earliest blank of G10–G15, then G16. If those are written, Géron **ch.10**, one new cluster: one hidden layer versus a deeper stack. One exercise. No Keras fit.
- **RAG polish:** the row you already marked, named in one line. A new score only if a local **RAGAS** run already returned it. Not TruLens.
- **how-i-measure:** one paragraph under a second heading. The third heading stays one line.
- Gold stays at **50**. Fill a missing question only if the file is short of 50 or has no refuse. Do not write a 51st.
- No child, nephew, or other private personal data.

---

## 2. Where you are

Monday’s bar was the initial loss: a fresh network should start near the flat-guess loss, and the knob is the scale of the last layer, which you did not have to set until a step needed it. Tuesday’s bar was a handful of steps. The forward was a looked-up block, one hidden mix, and a loss. You wrote the loss before the first step and after the last. Batch norm was not added.

G16, if you wrote it, is one smooth activation in place of the perceptron’s threshold. It was gated on G15 and on G10–G14. R1, if you wrote it, is one mark: which v1 row you would keep, from two real RAGAS scores, or a line that the polish waits. H3, if you wrote it, is one paragraph under one how-i-measure heading. Gold is at 50, or still short of it.

`03-makemore-gpt/` is still the code home. `evals/` holds v1. `proof/how-i-measure.md` is the one-pager. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.6–7 unless one of G10–G14 is still blank.

Upskill week 4, still open after today: the rest of Géron ch.10, batch norm and the rest of makemore part 3, the rest of the one-pager, and any polish that still has no real score. Gold stays 50 until week 5 freezes the set.

---

## 3. Concepts to use (you do not paste a finished notebook)

**The hidden mix after a few steps**
- The activation you named in G16, if you have it, squashes each hidden value into a range. Values stuck at the ends of that range barely move when the input moves. Values in the middle still have room.
- You look at the hidden values you already computed. You say which of those two pictures you see, in one sentence. You do not plot a library figure, and you do not paste a histogram from the video. The picture stays `slides later`.
- A fix has names: a smaller start, or batch norm. You may name them. You do not apply batch norm. You do not add a second hidden layer. You do not take more steps to “make the picture nicer.”
- Characters stay the ones you already used. Not a child, a nephew, or anyone private.

**Géron ch.10, the next cluster (concepts).** Only if G16 is written and G10–G15 are not blank.
- A deeper net is more than one hidden layer. Tuesday’s step used one. Depth can represent more, and it can also be harder to train. You say that in your own sentence. You do not add the layer.
- For PersonaLearn, one hidden mix is the net you already stepped. You do not retune its width. You do not fit a Keras model, and you do not search over depths.

**RAG polish, the mark you already made.** Today you do not pick a new winner.
- If R1 names a kept row, you write that chunking, that embedding, and the metric, in one line. The score stays the number already in the table. You do not compute a new one.
- If R1 said the polish waits, it still waits. You do not invent a score to unlock it. Not TruLens. The week-2 slice stays frozen.

**how-i-measure, the second paragraph.** One heading that is still a single line gets one short paragraph. One heading stays a single line, so the page is not finished. No new score inside the paragraph.

**Gold and privacy.** The set stays at 50. Under 50, finish 50. If a refuse is missing, fix that inside the 50. At 50 with a refuse already in the file, add nothing. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on A4. If it is missing, do those steps and stop. If it exists, read the hidden values. Do not train again. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | One sentence: middle or stuck at the ends. Name batch norm. Do not apply it. |

**Prompts (you write the notes):**
- **A5.** In `notes/`, one line: A4 exists, or it does not. If it does not, do A4 (and A2 first if that sentence is also missing) and stop. No activation check on a missing run.
- **A6.** If A4 exists: look at the hidden-mix values after those steps. One sentence: bunched in the middle, or stuck at the ends. One sentence naming a fix you are not applying (batch norm, or a second hidden layer). Do not take more steps. Do not add that fix. Do not paste a figure. No private names.

Open the makemore part 3 video only after A6, and only for the picture of activations stuck at the ends. Do not paste the batch-norm section.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Earliest blank of G10–G15, then G16. If those exist, the depth cluster and G17. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | The kept RAG row, in one line. One paragraph under a second how-i-measure heading. |
| 21:20–22:00 | Gold stays at 50. Privacy line if it is missing. Stop at 22:00. |

**Géron ch.10 — one exercise for the next cluster**
- **G17.** Only if G16 is written and none of G10–G15 is blank. If one of those is blank, that blank is the exercise and you do not start G17. If G17 is open: in your notes, (1) how many hidden layers Tuesday’s step used; (2) one sentence on what a second hidden layer could add, and why you are not adding it; (3) the line that this is not a search over depths; (4) the line you will not cross — no Keras fit, no new training run.

**Polish, page, privacy, gold (prompts only):**
- **R2.** If R1 is missing, write R1 and stop. If R1 kept a row, one line in `notes/` or on the one-pager: that chunking, that embedding, that RAGAS metric. The score is the number already written. Do not invent another. If R1 said the polish waits, repeat that in one line and do not unlock it. Not TruLens. Do not retune the week-2 slice. Do not commit a key.
- **H4.** If H3 is missing, write H3 and stop. If it exists, one paragraph under a heading that is still a single line. Leave one heading as a single line. No new RAGAS number in the paragraph.
- **B30.** One line: today’s check, the polish line, and the paragraph contain no child, nephew, or other private personal data. If B28 was never written, write that line first.
- **B31.** If the gold count is under 50, append items you write yourself until it is 50. If a refuse is missing, fix that without going past 50. If the file is already 50 and already has a refuse, do not add another.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. Were the hidden values in the middle or at the ends, and what fix did you leave unapplied?
2. Which Géron prompt did you actually write — a blank of G10–G16, or G17?
3. What did the polish line say, and which how-i-measure heading is still one line?
4. What is the gold count, and what personal data is banned from the check?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 3, the activation picture, after A6. Stop before batch norm.
- **Géron:** *Hands-On Machine Learning*, ch.10. The earliest blank of G10–G16; otherwise one exercise (G17, one hidden layer versus a deeper stack). Not a Keras fit today.
- **Evals:** **RAGAS** only. The mark from R1, not a new score. The week-2 slice stays frozen. Not TruLens.
- **Gold:** stays 50 (see `gold/README.md`). Week 5 freezes the set. Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 3 (YouTube)](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 4 (26–31 Oct):* ☐ Géron ch.10 ☐ makemore part 3 ☐ polish RAG ☐ how-i-measure one-pager ☐ gold stays 50 ☐ no child/nephew data
