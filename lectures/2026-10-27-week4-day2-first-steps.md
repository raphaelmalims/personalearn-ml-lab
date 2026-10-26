# Lecture — 2026-10-27 · Upskill week 4, day 2: first steps

> **Upskill week 4** (Mon 26 – Sat 31 Oct 2026), day 2. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the losses, the paragraph, and the one polish line.

Monday’s lecture: [`2026-10-26-week4-day1-init-loss.md`](2026-10-26-week4-day1-init-loss.md). The week targets do not change. Today advances Monday. It does not finish the week.

---

## 1. Goal for today

**Morning (09:00–12:00): a few steps, once the initial loss is written**
- If Monday’s A2 is missing, write that and stop. No training on a missing sentence.
- If A2 exists, take a few training steps. The hidden layer you build is only the mix those steps need: looked-up vectors in, one hidden mix, a loss out.
- Write the loss before the first step and after the last. The first one should sit near the flat-guess loss. Batch norm stays shut. No long run.

**Evening (19:00–22:00): the next ch.10 cluster, one polish, one paragraph**
- The earliest blank of G10–G14, then G15. If those are written, Géron **ch.10**, one new cluster: a smooth activation in place of the perceptron’s threshold. One exercise. No Keras fit.
- **RAG polish:** one concrete choice, and only from a score a local **RAGAS** run already returned. Not TruLens.
- **how-i-measure:** one paragraph under one heading that is still a single line. The other two stay as they are.
- Gold stays at **50**. Fill a missing question only if the file is short of 50 or has no refuse. Do not write a 51st.
- No child, nephew, or other private personal data.

---

## 2. Where you are

Monday’s bar was two sentences: a fresh network’s first loss should sit near the flat-guess loss, and the knob is the scale of the last layer’s outputs, which you did not set. The hidden layer was still unbuilt. Nothing was trained. Batch norm was named and left shut.

G15, if you wrote it, is the perceptron. It was gated on G10–G14. The how-i-measure page has three headings and one line each, if H1 was written. RAG polish was a sentence that said not tonight. Eval table v1 is unchanged from Saturday. Gold is at 50, or still short of it.

`03-makemore-gpt/` is still the code home. `evals/` holds v1. `proof/how-i-measure.md` is the one-pager. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.6–7 unless one of G10–G14 is still blank.

Upskill week 4, still open after today: the rest of Géron ch.10, the rest of makemore part 3 (batch norm and the rest), the rest of the RAG polish, and the rest of the one-pager. Gold stays 50 until week 5 freezes the set.

---

## 3. Concepts to use (you do not paste a finished notebook)

**A few steps, and only the layer they need**
- A step needs a loss that can move. The lookup you already have is not a loss. The hidden layer is the mix that turns a block of vectors into something a last layer can score. You build that mix. You do not build a second hidden layer, and you do not add batch norm.
- Before the first step, write the loss. It should sit near the flat-guess loss from A2. If it sits far above, the knob from Monday is the thing you would turn. You may turn it enough to land near that loss. You do not go hunting for a smaller number after that.
- A few steps means a handful. Write the loss after the last one. A smaller number is the point of a step. A long curve is not this morning. The picture of those few points stays `slides later`.
- Do not paste a network from the makemore repo. Characters stay the ones you already used. Not a child, a nephew, or anyone private.

**Géron ch.10, the next cluster (concepts).** Only if G15 is already written, and G10–G14 are not blank.
- The perceptron’s threshold has no useful slope. A smooth activation replaces it so a small change in the weights can change the loss. You name one such function. You do not derive its slope, and you do not copy a formula out of the book as your answer.
- That is why Monday’s network could not have taken a step on a bare threshold. You connect the two in a sentence. You do not refit G15.
- Keras, a stack wider than the one you stepped this morning, and a search over activations stay shut. Do not fit a Keras model.

**RAG polish, one choice (RAGAS).** Monday named the pass. Today you make one mark.
- Two v1 rows that differ by chunk size or by embedding, both with scores a local RAGAS run returned: you write which row you would keep, and the two numbers you are looking at. You do not delete the other row. You do not change the system that produced them.
- If you do not have two comparable real scores, you write that the polish waits. You do not invent the missing number. You do not retune the week-2 slice. Not TruLens.

**how-i-measure, one paragraph.** One heading that is still a single line gets one short paragraph. The other two headings stay one line each. No new score inside the paragraph.

**Gold and privacy.** The set stays at 50. Under 50, finish 50. If a refuse is missing, fix that inside the 50. At 50 with a refuse already in the file, add nothing. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on A2. If it is missing, write it and stop. If it exists, build only the mix a step needs, and write the loss before the first step. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | A handful of steps. Write the loss after the last one. Stop before batch norm. |

**Prompts (you write the notes):**
- **A3.** In `notes/`, one line: A2 exists, or it does not. If it does not, do A2 (and A1’s catch-up if K13 is also missing) and stop. No steps.
- **A4.** If A2 exists: in `03-makemore-gpt/` or `notes/`, the forward that a step needs. Looked-up block, one hidden mix, a loss. Write the loss before any step. It should sit near the flat-guess loss. If it does not, say so, and you may use Monday’s knob until it does. Then a handful of steps. Write the loss after the last step. Do not add a second hidden layer. Do not add batch norm. Do not paste a network. No private names.

Open the makemore part 3 video only after A4, and only for the picture of those few losses. Do not paste the batch-norm section.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Earliest blank of G10–G14, then G15. If those exist, the activation cluster and G16. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | One RAG-polish mark from real scores. One paragraph under one how-i-measure heading. |
| 21:20–22:00 | Gold stays at 50. Privacy line if it is missing. Stop at 22:00. |

**Géron ch.10 — one exercise for the next cluster**
- **G16.** Only if G15 is written and none of G10–G14 is blank. If one of those is blank, that blank is the exercise and you do not start G16. If G15 is the blank, G15 is the exercise. If G16 is open: name one smooth activation. In your notes, (1) why a threshold cannot take the step you took this morning, in one sentence; (2) the name of the function you would use instead; (3) the line that you are not deriving its slope; (4) the line you will not cross — no Keras fit, no search over activations.

**Polish, page, privacy, gold (prompts only):**
- **R1.** In `evals/` or `notes/`, one mark. If two v1 rows differ by chunk size or embedding and both scores are numbers a local RAGAS run returned, write which row you keep and the two numbers. Do not delete the other row. Do not change the pipeline. If you lack two real scores, one sentence: the polish waits. Do not invent a score. Do not retune the week-2 slice. Not TruLens. Do not commit a key.
- **H3.** If H1’s three headings are missing, write H1 and stop. If they exist, one paragraph under one heading that is still a single line. Leave the other two as one line each. No new RAGAS number in the paragraph.
- **B28.** One line: today’s steps, the polish mark, and the paragraph contain no child, nephew, or other private personal data. If B26 was never written, write that line first.
- **B29.** If the gold count is under 50, append items you write yourself until it is 50. If a refuse is missing, fix that without going past 50. If the file is already 50 and already has a refuse, do not add another.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What was the loss before the first step and after the last, and what did you refuse to add?
2. Which Géron prompt did you actually write — a blank of G10–G15, or G16?
3. Which eval row did you keep, or why did the polish wait? Which how-i-measure heading got the paragraph?
4. What is the gold count, and what personal data is banned from the steps?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 3, the first training steps, after A4. Stop before batch norm.
- **Géron:** *Hands-On Machine Learning*, ch.10. The earliest blank of G10–G15; otherwise one exercise (G16, a smooth activation). Not a Keras fit today.
- **Evals:** **RAGAS** only. One mark from scores you already have. The week-2 slice stays frozen. Not TruLens.
- **Gold:** stays 50 (see `gold/README.md`). Week 5 freezes the set. Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 3 (YouTube)](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 4 (26–31 Oct):* ☐ Géron ch.10 ☐ makemore part 3 ☐ polish RAG ☐ how-i-measure one-pager ☐ gold stays 50 ☐ no child/nephew data
