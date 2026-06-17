# Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.05081
- URL: https://arxiv.org/abs/2512.05081
- Category: S2 KV cache / attention memory 
- Priority: Must-read
- Training-free: Yes
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

Deep Forcing shows that naively importing attention sinks into video diffusion can harm fidelity and motion; its deep sink and participative compression preserve useful history without over-freezing the rollout.

## 3. Problem / failure mode

AR video diffusion still suffers temporal repetition, drift and motion deceleration; naive StreamingLLM-style sinks cause fidelity degradation and motion stagnation.

## 4. Memory object

- global context + active recent tokens

## 5. Memory substrate

- deep sink + participative compression

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes persistent sink tokens from history and records recently active attention participants. |
| Store | Half sliding window as persistent sink tokens plus compressed active KV history. |
| Retrieve | Attention reuses deep sink context and recently active compressed tokens. |
| Use | Stabilizes global context while maintaining dynamic degree for 12x horizon extrapolation. |
| Update | Participative compression updates retained history according to recent attention participation. |
| Forget | Prunes redundant/degraded tokens and discards inactive history. |
| Evaluate | Reports 5s-trained to 60s+ generation, real-time setting, image/aesthetic quality, consistency and dynamic degree. |

## 7. Strengths for this survey

Important corrective to “more sink is always better.” Useful in evaluation discussion about frozen-video traps.

## 8. Limitations / second-pass PDF checks

Still implicit token memory; no explicit entity/scene semantics.

## 9. Recommended placement

- Main category: S2 KV cache / attention memory 
- Role: 说明 attention sink 不是越强越好；过强会 motion stagnation。
- Priority: Must-read
