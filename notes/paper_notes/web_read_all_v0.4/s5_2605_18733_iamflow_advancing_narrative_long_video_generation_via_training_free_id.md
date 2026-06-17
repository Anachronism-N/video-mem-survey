# IAMFlow: Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.18733
- URL: https://arxiv.org/abs/2605.18733
- Category: S5 Identity / entity / narrative memory 
- Priority: Must-read
- Training-free: Yes
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

IAMFlow turns narrative video memory from implicit similarity matching into explicit global entity tracking with LLM-extracted IDs and VLM-verified attributes.

## 3. Problem / failure mode

Prompt transitions and shifting references cause identity drift, character duplication and attribute loss when history is compressed or retrieved only with coarse implicit attention.

## 4. Memory object

- entity identity and attributes

## 5. Memory substrate

- LLM global ID table + VLM attribute verification

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | LLM extracts entities and visual attributes from each prompt; generated frames are asynchronously verified by a VLM. |
| Store | Global ID table and identity-aware memory with attribute records. |
| Retrieve | Entity/global-ID matching retrieves identity memory rather than relying on temporal or visual similarity alone. |
| Use | Guides generation across prompt transitions and narrative scripts. |
| Update | VLM verification refines attributes from rendered frames; adaptive prompt transition updates conditioning. |
| Forget | Not mainly a forgetting paper; likely handles changes via attribute update rather than cache decay. |
| Evaluate | Introduces NarraStream-Bench with 324 multi-prompt scripts and MLLM-assisted evaluation. |

## 7. Strengths for this survey

Best representative of explicit identity/entity memory for narrative generation.

## 8. Limitations / second-pass PDF checks

LLM/VLM pipeline is heavier than pure attention/KV intervention and may depend on parser/verifier reliability.

## 9. Recommended placement

- Main category: S5 Identity / entity / narrative memory 
- Role: 显式实体/身份记忆核心论文。
- Priority: Must-read
