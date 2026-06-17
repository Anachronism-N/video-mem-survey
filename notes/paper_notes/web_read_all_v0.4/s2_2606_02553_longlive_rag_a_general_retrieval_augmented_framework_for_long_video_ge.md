# LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.02553
- URL: https://arxiv.org/abs/2606.02553
- Category: S2 KV cache / attention memory 
- Priority: High
- Training-free: System / may be training-light
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv/search abstract web-read

## 2. One-sentence takeaway

LongLive-RAG is the cleanest RAG formulation for AR video generation: previously generated latents become a content-addressable searchable history, not just a sliding window.

## 3. Problem / failure mode

Sliding-window attention creates irreversible error accumulation because later blocks condition only on degraded recent trajectory.

## 4. Memory object

- retrieval over long video context

## 5. Memory substrate

- retrieval-augmented historical context

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes self-generated latents into dynamic searchable history. |
| Store | Content-addressable latent memory indexed by query embeddings. |
| Retrieve | At each new block, retrieves relevant historical latents; Window Temporal Delta Loss makes embeddings capture meaningful temporal changes. |
| Use | Conditions generator on non-local historical context to reduce drift. |
| Update | History grows with generated latents; retrieval index updates dynamically. |
| Forget | Not central; retrieval rather than permanent retention handles relevance. |
| Evaluate | Multiple AR backbones/lengths and VBench-Long rank. |

## 7. Strengths for this survey

Core S6 retrieval-memory paper for video generation.

## 8. Limitations / second-pass PDF checks

Retrieval quality depends on embedding/indexing; not explicitly entity-aware.

## 9. Recommended placement

- Main category: S2 KV cache / attention memory 
- Role: 把 RAG 思路引入 LongLive/long video memory。
- Priority: High
