# Lecture — 2026-10-26 · Upskill week 4, day 1: initial loss

> **Upskill week 4** (Mon 26 – Sat 31 Oct 2026), day 1. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the sentences, the headings, and nothing past the first slice.

Saturday’s lecture: [`2026-10-24-week3-day6-week-close.md`](2026-10-24-week3-day6-week-close.md). Week 3 is closed. Today opens week 4. It does not finish it.

---

## 1. Goal for today

**Morning (09:00–12:00): the first slice of makemore part 3**
- If Friday’s K13 is missing, that catch-up is the morning. Do not open part 3 on a missing close.
- If K13 exists, part 3 starts as one idea: a fresh network’s first loss should sit near the flat-guess loss you already wrote. You say that. You name the knob. You do not build the hidden layer.
- Batch norm, dead neurons, and a training run stay later in the week.

**Evening (19:00–22:00): ch.10 opens, and the one-pager gets headings**
- If any of G10–G14 is blank, that earliest blank is the only Géron exercise. Do not add a second.
- If those five are written, Géron **ch.10**, one cluster: a perceptron. One exercise. The Keras fit stays shut.
- **how-i-measure:** three headings and one line under each. The page is not finished tonight.
- RAG polish is named and not done. Eval table v1 stays as Saturday left it. **RAGAS** only. Not TruLens.
- Gold stays at **50**. If the count is under 50, finish 50 and stop. Do not write a 51st.
- No child, nephew, or other private personal data.

---

## 2. Where you are

Week 3 closed on a small embedding table, a few looked-up blocks, a flat-guess loss that does not change with the block, and Friday’s two columns (share and count). The hidden layer was not built. Part 3 was not opened. G10–G14 are the ch.6–7 notes already issued. Eval table v1 holds real RAGAS scores where a run returned them, and blanks where it did not. Gold is aimed at 50. One fuzzy sentence was written and not started.

`03-makemore-gpt/` is still the code home. `evals/` holds v1. `proof/` is where the one-pager may live. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.6–7 unless one of G10–G14 is still blank.

Upskill week 4, still open after today: the rest of Géron ch.10, the rest of makemore part 3, a RAG polish, and the how-i-measure one-pager. Gold stays 50 until week 5 freezes the set.

---

## 3. Concepts to use (you do not paste a finished notebook)

**Makemore part 3, the opening only**
- The flat-guess loss is the loss of a model that is equally unsure about every character. A network that has not learned anything should start near that loss, not far above it.
- The knob people turn is the scale of the last layer’s outputs at the start: small outputs keep the first guess near the flat one. You name the knob. You do not set a number, and you do not code the layer.
- The hidden layer that would sit in front of that last layer is still unbuilt. Part 3’s later slices (a saturated activation, a dead unit, batch norm) stay shut. The picture of the first loss stays `slides later`.
- You do not train. You do not change Saturday’s table. Examples stay made-up or already-public. Not a child, a nephew, or anyone private.

**Géron ch.10, one cluster (concepts).** Only if G10–G14 are already written. Stay on the perceptron.
- A perceptron takes inputs, multiplies each by a weight, adds a bias, and applies a threshold. That is one neuron. You already met the idea in week 1. You are not re-deriving the chain rule.
- For PersonaLearn the threshold can still be thought of as answer versus refuse. You are not fitting it.
- A stack of perceptrons, the Keras Sequential API, and a hyperparameter search are the rest of ch.10. They stay shut. Do not fit.

**how-i-measure, the headings only.** The one-pager is a week target. Tonight is the outline.
- Three headings: what you measure, what you measure it on, what you will not claim.
- One line under each, in your own words. Metric names you already use. The gold slice and the eval table you already have. No new score. No TruLens. No private data.
- The paragraphs that would make it a page are later this week.

**RAG polish, named and not done.** Polish means a later look at the chunking and embedding choices already on v1. Tonight you do not change them. A score you did not get from a RAGAS run stays blank. The week-2 slice stays frozen.

**Gold and privacy.** The set stays at 50. Under 50, finish 50 first. At 50, stop. Week 5 freezes the file. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on K13. If it is missing, do that catch-up and stop. If it exists, write the initial-loss idea. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Name the knob. List the part-3 slices you are not opening. Stop before a hidden layer. |

**Prompts (you write the notes):**
- **A1.** In `notes/`, one line: K13 exists, or it does not. If it does not, do K13 (and the earliest blank of K8, K9, or K11 if that is what K13 still needs) and stop. No part 3.
- **A2.** If K13 exists: two sentences. (1) A fresh network’s first loss should sit near the flat-guess loss you already have. (2) The knob is the scale of the last layer’s outputs at the start, and you are not setting it. Then one line naming two part-3 slices you are leaving shut (a saturated activation, batch norm, or a training step — pick two). Do not build the hidden layer. Do not change Saturday’s table. Do not train. No private names.

Open the makemore part 3 video only after A2, and only for the picture of that first loss. Do not paste a network.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Earliest blank of G10–G14, or the perceptron and G15 if none is blank. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | how-i-measure: three headings and one line each. One sentence that RAG polish is not tonight. |
| 21:20–22:00 | Gold stays at 50. Privacy line if it is missing. Stop at 22:00. |

**Géron ch.10 — one exercise for the cluster**
- **G15.** Only if G10, G11, G12, G13, and G14 are already written. If one is blank, that blank is the exercise and you do not start G15. If all five exist: in your notes, (1) what a perceptron computes, in one sentence of yours; (2) the week-1 object that is the same idea; (3) how you would use it as answer versus refuse, without a fit; (4) the line you will not cross — no Keras model, no fit, no stack of layers.

**Page, polish, privacy, gold (prompts only):**
- **H1.** In `proof/how-i-measure.md`, the title and three headings: what you measure, what you measure it on, what you will not claim. One line under each. No new RAGAS number. Not TruLens. Do not retune eval table v1 or the week-2 slice. The rest of the page waits.
- **H2.** One sentence: RAG polish is a later pass over chunking and embedding choices you already scored, and you are not making that pass tonight. If v1 has no real score, the sentence says there is nothing to polish from yet.
- **B26.** One line: A2 and the one-pager contain no child, nephew, or other private personal data. If the week-3 privacy line was never written, write that line first.
- **B27.** If the gold count is under 50, append items you write yourself until it is 50. If it is 50, do not add another. Keep a mix of types, and keep at least one refuse. The file stays at 50.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. What should a fresh network’s first loss sit near, and which layer did you leave unbuilt?
2. Which Géron prompt did you actually write — the earliest blank of G10–G14, or G15?
3. What are the three how-i-measure headings, and what did you refuse to polish tonight?
4. What is the gold count, and what personal data is banned from the notes?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 3, the initial-loss section, after A2. Stop before the hidden layer, before batch norm, and before a training step.
- **Géron:** *Hands-On Machine Learning*, ch.10, the perceptron, and only if G10–G14 are written. Otherwise the earliest blank of those. Not a Keras fit today.
- **Evals:** **RAGAS** only. Eval table v1 stays as Saturday left it. Not TruLens.
- **Gold:** 50, already the week-3 close (see `gold/README.md`). Week 5 freezes the set. Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 3 (YouTube)](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 4 (26–31 Oct):* ☐ Géron ch.10 ☐ makemore part 3 ☐ polish RAG ☐ how-i-measure one-pager ☐ gold stays 50 ☐ no child/nephew data
