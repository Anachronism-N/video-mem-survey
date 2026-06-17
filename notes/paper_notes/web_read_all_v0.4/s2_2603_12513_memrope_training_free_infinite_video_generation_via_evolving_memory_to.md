# MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.12513
- URL: https://arxiv.org/abs/2603.12513
- Category: S2 KV cache / attention memory 
- Priority: Must-read
- Training-free: Yes
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

MemRoPE co-designs content compression and temporal coordinates: long/short EMA memory tokens only make sense if keys are cached before RoPE and positional embeddings are applied online.

## 3. Problem / failure mode

Sliding-window caches discard past context, causing fidelity degradation, identity drift, and motion stagnation; static attention sinks cannot reflect evolving video content.

## 4. Memory object

- identity + recent dynamics compressed memory

## 5. Memory substrate

- dual EMA memory tokens + unrotated KV + online RoPE

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Continuously writes all past keys into dual long-term and short-term EMA streams. |
| Store | Fixed-size memory tokens plus unrotated key cache. |
| Retrieve | Attention retrieves aggregated long/short memory with RoPE applied dynamically at attention time. |
| Use | Provides global identity/history and recent dynamics within fixed cache for unbounded generation. |
| Update | EMA updates long-term and short-term memory streams as video grows. |
| Forget | Forgetting is implicit through EMA decay rather than explicit semantic conflict detection. |
| Evaluate | Minute- to hour-scale generation with temporal coherence, visual fidelity and subject consistency. |

## 7. Strengths for this survey

Key paper for positional memory: content memory cannot be separated from coordinate design.

## 8. Limitations / second-pass PDF checks

EMA memory is still implicit and does not know which entity or attribute is being stored.

## 9. Recommended placement

- Main category: S2 KV cache / attention memory 
- Role: 把 memory compression 和 RoPE phase 解耦联系起来，技术主线非常关键。
- Priority: Must-read
