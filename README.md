# personalearn-ml-lab

Q4 Study / PersonaLearn ML lab (practice + proof artifacts). **Not** the product Ship repo.

- **Plan source of truth:** Notion Upskill — **Option A, 10 weeks** (Mon 5 Oct → Sat 12 Dec 2026; buffer 14–19 Dec)
- **This repo:** code, notebooks, notes, lectures, and proof that a hiring manager can skim
- **Guardrail:** no job applications or LinkedIn content in this lane

## Study schedule — Option A

The clock is **Notion OS Day**. About **33h ML + 6h Java** a week. Mon–Fri ML is 09:00–12:00 and 19:00–22:00 (Java 08:00–09:00; review/planning 22:00–23:00). Saturday 08:00–12:00 is lighter: **1h Java + 3h ML**. A 10-minute break every 90 minutes. No study after 22:00.

Week 1 starts **Mon 5 Oct 2026**. Finish **Sat 12 Dec 2026**. Buffer **14–19 Dec**.

Daily lectures (notes + exercise prompts only, no solutions) go in [`lectures/`](lectures/).

## Week 1 (5–10 Oct 2026)

Karpathy **micrograd backprop** + Géron **ch.1–2** + **eval basics** + **PDF inventory** + **first 20 gold questions**.

| Day | Focus |
| --- | --- |
| Mon 5 | [Lecture](lectures/2026-10-05-week1-micrograd-geron-gold.md): micrograd backward pass · Géron ch.1–2 · gold set + PDF inventory start |
| Tue 6 | [Lecture](lectures/2026-10-06-week1-day2-micrograd-geron-gold.md): continue micrograd backprop · Géron ch.1–2 (one exercise) · RAGAS · inventory · gold toward 20 |
| Wed–Fri | Finish micrograd (neuron/MLP stretch) · Géron ch.1–2 depth · RAGAS concepts · inventory · gold toward 20 |
| Sat 10 | Lighter 08:00–12:00 (1h Java + 3h ML): catch-up / spaced review · gold to 20 |

## Layout

| Path | Purpose |
| --- | --- |
| `01-micrograd/` | Autograd from scratch (scalars → graph → backprop) |
| `02-geron/` | Hands-On ML chapters |
| `03-makemore-gpt/` | Later: tiny GPT + loss |
| `04-rag-evals/` | RAG baseline + eval harness |
| `05-lora-serve/` | Later: adapter + serve |
| `gold/` | Gold questions (20 by 10 Oct → 30 by 17 Oct → 50 by 24 Oct) |
| `evals/` | Eval tables / scripts |
| `lectures/` | Daily lecture notes + exercise prompts (no solutions) |
| `notes/` | Daily study notes (markdown) |
| `proof/` | Skimmable artifacts for applications |

## micrograd quick start

```bash
cd 01-micrograd
python3 explore.py
```

The forward graph is done. Week 1 next step: implement `backward()` yourself (see the Week 1 lectures).

Optional: add `01-micrograd/scalars_graph.ipynb` for cell-by-cell exploration; keep `value.py` as the durable core.

## Phase proofs (high level)

Option A (10 weeks): **W1 = gold 20 + eval basics (no RAG scores yet). RAG baseline scores = Wk 2.** Then W3–4 eval table → … → W9–10 capstone README. Java has its own 08:00–09:00 slot. It is not part of the ML blocks.
