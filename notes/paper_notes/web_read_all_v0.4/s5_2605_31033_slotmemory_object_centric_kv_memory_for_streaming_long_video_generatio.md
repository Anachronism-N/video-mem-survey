# SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.31033
- URL: https://arxiv.org/abs/2605.31033
- Category: S5 Identity / entity / narrative memory 
- Priority: Must-read
- Training-free: Likely yes/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

SlotMemory shifts memory abstraction from when something happened to what entity is represented, decomposing KV memory into reusable semantic slots.

## 3. Problem / failure mode

Temporal-centric memory organized as frames/chunks/unclustered tokens causes identity drift and semantic inconsistency when entities leave the frame or prompts change.

## 4. Memory object

- object/entity persistence

## 5. Memory substrate

- object-centric KV semantic slots

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

- Main category: S5 Identity / entity / narrative memory 
- Role: 从 temporal-centric memory 转向 object-centric memory 的核心代表。
- Priority: Must-read
