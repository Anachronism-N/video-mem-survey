# Closed-Loop Triplet Synergistic Generation for Long-Form Video / CoTriSyGen

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.16184
- URL: https://arxiv.org/abs/2606.16184
- Category: S5 Identity / entity / narrative memory 
- Priority: High
- Training-free: Agentic pipeline
- Original status: Verified by web, added in v0.2
- Reading status: web-read
- Source basis: arXiv/search abstract web-read

## 2. One-sentence takeaway

CoTriSyGen treats long-video generation as a closed-loop visual-text-memory synergy, where generated visuals update future prompts and mutable entity memory.

## 3. Problem / failure mode

Storyboard pipelines are often feed-forward and cannot feed generated evidence back into later conditioning, causing cross-shot identity and composition inconsistencies.

## 4. Memory object

- entity/narrative memory

## 5. Memory substrate

- closed-loop visual-text-memory synergy + mutable visual state

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes newly manifested/evolved entities, multi-view evidence, and generated visual evidence into mutable visual state. |
| Store | Entity-centric mutable visual-state memory. |
| Retrieve | VLM analyzer reasons over planned intent, persistent memory and generated visuals. |
| Use | Intra-shot regeneration/refinement and inter-shot prompt rewriting propagate entity attributes and cinematic continuity. |
| Update | Closed-loop analyzer updates prompts and memory after observing generated results. |
| Forget | Not the focus; conflict resolution/update policy should be checked in PDF. |
| Evaluate | StoryBench; cross-shot consistency, prompt adherence and cinematic continuity. |

## 7. Strengths for this survey

Strong narrative-memory example for Update/closed-loop memory lifecycle.

## 8. Limitations / second-pass PDF checks

Agentic/VLM loop may be slow and complex; not a low-level KV method.

## 9. Recommended placement

- Main category: S5 Identity / entity / narrative memory 
- Role: 补充 narrative memory：把生成结果反馈到 memory/prompt，体现 memory update 生命周期。
- Priority: High
