# Lecture — 2026-10-30 · Upskill week 4, day 5: stuck count

> **Upskill week 4** (Mon 26 – Sat 31 Oct 2026), day 5. ML blocks **09:00–12:00** and **19:00–22:00** EAT.
> **10-minute break per 90 minutes.** Hard stop **22:00**. 22:00–23:00 is review/planning, not study.
> **08:00–09:00 is Java** (java-spring-lab). Do not open this lecture in that hour.
> **Notes and prompts only. No solutions.** You write the count, the one exercise, and the one line.

Thursday’s lecture: [`2026-10-29-week4-day4-gradient-note.md`](2026-10-29-week4-day4-gradient-note.md). The week targets do not change. Today moves toward Saturday’s close. It does not write that close. Batch norm stays shut.

---

## 1. Goal for today

**Morning (09:00–12:00): how many hidden units are stuck**
- If Thursday’s A8 is missing, that gradient note is the morning. Do not count units you have not described.
- If A8 exists, count how many hidden units sit at the ends, and how many units the mix has.
- You write the two numbers. You do not revive the stuck ones. You do not train again. You do not apply batch norm, and you do not add a second hidden layer.

**Evening (19:00–22:00): the next ch.10 cluster, and the page still waits for Saturday**
- The earliest blank of G10–G17, then G18. If those are written, Géron **ch.10**, one new cluster: which loss goes with which head. One exercise. No Keras fit. No new steps.
- **RAG polish:** the kept row, or the waiting line, copied onto the one-pager. No new **RAGAS** score. Not TruLens.
- **how-i-measure:** one line naming the heading that is still short. You do not fill it. Saturday is the close.
- Gold stays at **50**. Fill a missing question only if the file is short of 50 or has no refuse. Do not write a 51st.
- No child, nephew, or other private personal data.

---

## 2. Where you are

Thursday’s bar was one sentence: hidden values stuck at the ends leave a small gradient, and values in the middle still have room. You named a fix (an init that scales with the number of inputs, or batch norm) and you did not apply it. You did not train again.

Wednesday’s check said middle or ends. Tuesday’s handful of steps is still the only training: one hidden mix, a loss near the flat-guess loss at the start, a loss after those steps. G18, if you wrote it, is a distribution over characters versus G13’s single number. R3, if you wrote it, says you will not retune without a new RAGAS score. H5, if you wrote it, is one sentence under the last short heading. The page is unfinished. Gold is at 50, or still short of it.

`03-makemore-gpt/` is still the code home. `evals/` holds v1. `proof/how-i-measure.md` is the one-pager. The week-2 RAGAS slice stays frozen. Do not retrain the week-2 one-layer net. Do not reopen ch.6–7 unless one of G10–G14 is still blank.

Saturday 31 Oct stays the lighter close. Do not do Saturday’s pass tonight.

Upskill week 4, still open after today: Saturday’s proof lines, any blank of G10–G18, batch norm still unopened, and the last of the one-pager. Gold stays 50 until week 5 freezes the set.

---

## 3. Concepts to use (you do not paste a finished notebook)

**A count of stuck units**
- A unit at the end of its activation is the one Thursday said has a small gradient. You count those units. You also write how many units the hidden mix has, so the count has a denominator you can say in words.
- If A6 said the values were in the middle, the stuck count can be zero. You write zero. You do not go looking for a worse picture.
- You do not revive a stuck unit. You do not change the init. You do not add batch norm. You do not take another step. The picture of a dead unit stays `slides later`.
- Characters stay the ones you already used. Not a child, a nephew, or anyone private.

**Géron ch.10, the next cluster (concepts).** Only if G18 is written and G10–G17 are not blank.
- The head that ends in a distribution is trained by how little probability the right class got. That is the next-character loss you already have. You name it in your own words. You do not copy a formula.
- The head that ends in one number is trained by how far the guess sits from a target number. G13’s mean is the leaf, not this loss. You do not derive either loss, and you do not train tonight.

**RAG polish, cited and not rerun.** If a row was kept, that chunking, embedding, and metric go on the one-pager as the measurement you will point at. The score stays the number already written. If the polish was waiting, the one-pager says so. No new run. Not TruLens. The week-2 slice stays frozen.

**how-i-measure, still short on purpose.** You name the heading that is still a sentence or a single line. You do not expand it tonight. Saturday writes the close.

**Gold and privacy.** The set stays at 50. Under 50, finish 50. If a refuse is missing, fix that inside the 50. At 50 with a refuse already in the file, add nothing. Commit text you write, not PDFs, not secrets, not `.env`. No child, nephew, or other sensitive personal data.

---

## 4. Morning block (09:00–12:00 EAT)

| Time | Activity |
| --- | --- |
| 09:00–10:30 | Gate on A8. If it is missing, write that note and stop. If it exists, count the stuck units. |
| 10:30–10:40 | Break (10 minutes; away from the screen). |
| 10:40–12:00 | Write the count and the size of the mix. Name the fix you are still not applying. |

**Prompts (you write the notes):**
- **A9.** In `notes/`, one line: A8 exists, or it does not. If it does not, do A8 (and A6 first if that check is also missing) and stop. No count on a missing note.
- **A10.** If A8 exists: two numbers. How many hidden units sit at the ends, and how many units the mix has. One sentence tying that count to A8’s gradient line. One sentence naming the fix you are not applying (batch norm, or a new init). Do not change the net. Do not take a step. No private names.

Open the makemore part 3 video only after A10, and only for the picture of a stuck unit. Do not paste the batch-norm section.

---

## 5. Evening block (19:00–22:00 EAT)

| Time | Activity |
| --- | --- |
| 19:00–20:30 | Earliest blank of G10–G17, then G18. If those exist, the loss cluster and G19. One exercise. |
| 20:30–20:40 | Break (10 minutes). |
| 20:40–21:20 | Cite the kept RAG row on the one-pager. Name the heading Saturday still has to finish. |
| 21:20–22:00 | Gold stays at 50. Privacy line if it is missing. Stop at 22:00. |

**Géron ch.10 — one exercise for the next cluster**
- **G19.** Only if G18 is written and none of G10–G17 is blank. If one of those is blank, that blank is the exercise and you do not start G19. If G19 is open: in your notes, (1) the loss that goes with a distribution over characters, in your own words; (2) the loss that would go with a single target number, in your own words; (3) the line that you are not deriving either one; (4) the line you will not cross — no Keras fit, no new steps, no batch norm.

**Polish, page, privacy, gold (prompts only):**
- **R4.** If R3 is missing, write R3 and stop. If a row was kept, one line on `proof/how-i-measure.md`: that chunking, that embedding, that RAGAS metric, and the score already in the table. If the polish was waiting, the line says so. Do not invent a score. Do not run RAGAS tonight. Not TruLens. Do not retune the week-2 slice. Do not commit a key.
- **H6.** If H5 is missing, write H5 and stop. If it exists, one line: which heading is still short of a paragraph. Do not write that paragraph. Saturday is the close.
- **B34.** One line: today’s count, the one-pager line, and the loss note contain no child, nephew, or other private personal data. If B32 was never written, write that line first.
- **B35.** If the gold count is under 50, append items you write yourself until it is 50. If a refuse is missing, fix that without going past 50. If the file is already 50 and already has a refuse, do not add another.

---

## 6. Self-check (answer in `notes/`; no answers here)

1. How many hidden units were stuck, out of how many, and what did you refuse to apply?
2. Which Géron prompt did you actually write — a blank of G10–G18, or G19?
3. What did you cite on the one-pager, and which heading is still short?
4. What is the gold count, and what personal data is banned from the count?

---

## 7. Pointers

- **makemore:** Karpathy, *makemore* part 3, the stuck-unit picture, after A10. Stop before batch norm. Saturday is the close, not tonight.
- **Géron:** *Hands-On Machine Learning*, ch.10. The earliest blank of G10–G18; otherwise one exercise (G19, which loss goes with which head). Not a Keras fit today.
- **Evals:** **RAGAS** only. Cite a score you already have. No new run. The week-2 slice stays frozen. Not TruLens.
- **Gold:** stays 50 (see `gold/README.md`). Week 5 freezes the set. Privacy: no child, nephew, or other sensitive personal data.

## 8. Resources

- [Karpathy — makemore part 3 (YouTube)](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- [karpathy/makemore (GitHub)](https://github.com/karpathy/makemore)
- [Géron — Hands-On ML notebooks (ageron/handson-ml3)](https://github.com/ageron/handson-ml3)
- [RAGAS — Get started](https://docs.ragas.io/en/stable/getstarted/)
- [RAGAS — Metrics](https://docs.ragas.io/en/stable/concepts/metrics/)

---

*Upskill week 4 (26–31 Oct):* ☐ Géron ch.10 ☐ makemore part 3 ☐ polish RAG ☐ how-i-measure one-pager ☐ gold stays 50 ☐ no child/nephew data
