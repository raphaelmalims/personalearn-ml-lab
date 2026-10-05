# personalearn-ml-lab

Q4 Study / PersonaLearn ML lab (practice + proof artifacts). **Not** the product Ship repo.

- **Plan source of truth:** Notion Upskill — **Option A, 10 weeks** (Mon 5 Oct → Sat 12 Dec 2026; buffer 14–19 Dec)
- **This repo:** code, notebooks, notes, lectures, and proof that a hiring manager can skim
- **Guardrail:** no job applications or LinkedIn content in this lane

## Study schedule — Option A (EAT)

| Time | Mon–Fri | Sat (lighter) |
| --- | --- | --- |
| 08:00–09:00 | Java | Study 08:00–12:00 |
| 09:00–12:00 | **ML block 1** | |
| 13:30–17:30 | Hunt | — |
| 19:00–22:00 | **ML block 2** | — |
| 22:00–23:00 | Review / planning (no new study) | — |

- No study after 22:00.
- Week 1 starts **Mon 5 Oct 2026**. 10 weeks end **Sat 12 Dec 2026**. Buffer week **14–19 Dec**.
- Daily lectures (notes + exercise prompts only, no solutions) go in [`lectures/`](lectures/).

## Week 1 (5–10 Oct 2026)

Karpathy **micrograd backprop** + Géron **ch.1–2** + **eval basics** + **PDF inventory** + **first 20 gold questions**.

| Day | Focus |
| --- | --- |
| Mon 5 | [Lecture](lectures/2026-10-05-week1-micrograd-geron-gold.md): micrograd backward pass · Géron ch.1–2 · gold set + PDF inventory start |
| Tue–Fri | Finish micrograd (neuron/MLP stretch) · Géron ch.2 depth · RAGAS eval concepts · inventory complete · gold Qs toward 20 |
| Sat 10 | Lighter 08–12: catch-up / spaced review · gold to 20 |

<details><summary>Previous plan (superseded): Week 1 of 22 Sep, Study mornings Mon–Sat 08:00–12:00</summary>

| Day | Focus |
| --- | --- |
| Tue | Micrograd: scalars → computation graph |
| Wed | Micrograd: backprop + Géron ch.1 |
| Thu | Géron ch.2 end-to-end |
| Fri | Eval basics + gold-set start |
| Sat | Catch-up / spaced review · or gold Qs if ahead |

</details>

## Layout

| Path | Purpose |
| --- | --- |
| `01-micrograd/` | Autograd from scratch (scalars → graph → backprop) |
| `02-geron/` | Hands-On ML chapters |
| `03-makemore-gpt/` | Later: tiny GPT + loss |
| `04-rag-evals/` | RAG baseline + eval harness |
| `05-lora-serve/` | Later: adapter + serve |
| `gold/` | Gold questions (~30 target) |
| `evals/` | Eval tables / scripts |
| `lectures/` | Daily lecture notes + exercise prompts (no solutions) |
| `notes/` | Daily study notes (markdown) |
| `proof/` | Skimmable artifacts for applications |

## micrograd quick start

```bash
cd 01-micrograd
python3 explore.py
```

The forward graph is done. Week 1 next step: implement `backward()` yourself (see today's lecture).

Optional: add `01-micrograd/scalars_graph.ipynb` for cell-by-cell exploration; keep `value.py` as the durable core.

## Phase proofs (high level)

Option A (10 weeks): W1–2 gold + RAG scores → W3–4 eval table → … → W9–10 capstone README. Java has its own 08:00–09:00 slot. It is not part of the ML blocks.
