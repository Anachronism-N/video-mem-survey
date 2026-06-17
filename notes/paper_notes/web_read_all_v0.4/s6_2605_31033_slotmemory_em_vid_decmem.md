# SlotMemory / EM-Vid / DecMem

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.31033
- URL: https://arxiv.org/abs/2605.31033
- Category: S6 Retrieval / external memory 
- Priority: High
- Training-free: mixed
- Original status: Verified for SlotMemory and EM-Vid; DecMem to verify
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

SlotMemory shifts memory abstraction from when something happened to what entity is represented, decomposing KV memory into reusable semantic slots.

## 3. Problem / failure mode

Temporal-centric memory organized as frames/chunks/unclustered tokens causes identity drift and semantic inconsistency when entities leave the frame or prompts change.

## 4. Memory object

- entity/global-local memory

## 5. Memory substrate

- slot / patch bank / decoupled memory

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Stores high-fidelity key-value tokens into discrete semantic slots. |
| Store | Object-centric KV slots used as routing addresses. |
| Retrieve | Prompt-aware retrieval addresses semantic slots rather than time windows. |
| Use | Maintains entity-level persistence across long horizons in streaming video diffusion. |
| Update | Slots are reused/updated as entities persist or reappear. |
| Forget | Not highlighted in abstract; budget and slot replacement policy should be checked in PDF. |
| Evaluate | 60-second interactive narratives with Wan2.1-T2V-1.3B; reports SOTA score and dynamic consistency improvement. |

## 7. Strengths for this survey

Key bridge between KV memory and entity memory.

## 8. Limitations / second-pass PDF checks

Need PDF for slot construction, routing loss/algorithm and ablations.

## 9. Recommended placement

- Main category: S6 Retrieval / external memory 
- Role: 作为 retrieval memory 与 entity memory 的交叉。
- Priority: High
