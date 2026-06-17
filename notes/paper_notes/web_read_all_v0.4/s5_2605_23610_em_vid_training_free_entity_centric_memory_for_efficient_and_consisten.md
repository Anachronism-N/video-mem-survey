# EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.23610
- URL: https://arxiv.org/abs/2605.23610
- Category: S5 Identity / entity / narrative memory 
- Priority: Must-read
- Training-free: Yes
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

EM-Vid argues full-frame memory entangles persistent entity information with transient scene context; it stores entity-indexed latent patches and conditions sparsely on entity-relevant tokens.

## 3. Problem / failure mode

Multi-shot videos need recurring entities to stay consistent while following shot-specific prompts; reusing full frames leaks irrelevant context and is costly.

## 4. Memory object

- recurring entity appearance

## 5. Memory substrate

- entity-indexed sparse latent patch bank

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes entity-relevant latent patches into an entity-indexed memory bank. |
| Store | Sparse latent patch bank keyed by entity. |
| Retrieve | Sparse token conditioning restricts attention to entity-relevant tokens. |
| Use | Improves subject consistency, prompt adherence and efficiency in multi-shot generation. |
| Update | Budgeted memory update maintains compact evolving memory. |
| Forget | Budgeted update likely evicts less useful entity evidence; exact policy needs PDF. |
| Evaluate | Multi-shot script format; evaluates prompt adherence, efficiency and subject consistency. |

## 7. Strengths for this survey

Clean argument for why memory units should be entity patches, not full frames.

## 8. Limitations / second-pass PDF checks

Requires reliable entity indexing and may need PDF for exact patch selection/noise injection details.

## 9. Recommended placement

- Main category: S5 Identity / entity / narrative memory 
- Role: entity-centric latent patch memory 的核心代表。
- Priority: Must-read
