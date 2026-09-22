# personalearn-ml-lab

Q4 Study / PersonaLearn ML lab (practice + proof artifacts). **Not** the product Ship repo.

- **Plan source of truth:** Notion Upskill — progressive 14 weeks (Sep–Dec 2026)
- **This repo:** code, notebooks, notes, and hire-manager-skimmable proof
- **Cadence:** Study mornings Mon–Sat 08:00–12:00 EAT
- **Guardrail:** no job applications or LinkedIn content in this lane

## Week 1 (week of 22 Sep 2026)

Karpathy **micrograd** + Géron **ch.1–2** + eval basics.

| Day | Focus |
| --- | --- |
| Tue | Micrograd: scalars → computation graph |
| Wed | Micrograd: backprop + Géron ch.1 |
| Thu | Géron ch.2 end-to-end |
| Fri | Eval basics + gold-set start |
| Sat | Catch-up / spaced review · or gold Qs if ahead |

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
| `notes/` | Daily study notes (markdown) |
| `proof/` | Skimmable artifacts for applications |

## Today (Tue)

```bash
cd 01-micrograd
python3 explore.py
```

Stop at scalars → graph. Leave `backward()` for Wed.

Optional: add `01-micrograd/scalars_graph.ipynb` for cell-by-cell exploration; keep `value.py` as the durable core.

## Phase proofs (high level)

W1–2 gold + RAG scores → W3–4 eval table → … → W13–14 capstone README. Java/Spring is **not** Study priority this quarter.
