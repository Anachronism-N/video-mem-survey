# Reading Notes Bundle v0.2


---

# ASurvey: Spatiotemporal Consistency in Video Generation

## 1. Metadata

- Year: 2025/2026
- ID: arXiv:2502.17863 / ACM TOG?
- URL: https://arxiv.org/abs/2502.17863
- Category: S0 Existing surveys / 相邻综述
- Priority: High background
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S0 Existing surveys / 相邻综述，核心记忆对象是 spatiotemporal consistency，记忆载体是 representation / generation / post-processing / metrics。在综述中主要作用：说明 consistency survey 与 memory-centric survey 的差异：consistency 是现象层，memory 是机制层。

## 3. Memory object

spatiotemporal consistency

## 4. Memory substrate

representation / generation / post-processing / metrics

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：说明 consistency survey 与 memory-centric survey 的差异：consistency 是现象层，memory 是机制层。 |
| Store | 初步载体：representation / generation / post-processing / metrics |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S0 Existing surveys / 相邻综述
- Role in survey: 说明 consistency survey 与 memory-centric survey 的差异：consistency 是现象层，memory 是机制层。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `spatiotemporal consistency` 与 `representation / generation / post-processing / metrics` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# A Survey on Long-Video Storytelling Generation

## 1. Metadata

- Year: 2025
- ID: arXiv:2507.07202 / ICCVW 2025
- URL: https://arxiv.org/abs/2507.07202
- Category: S0 Existing surveys / 相邻综述
- Priority: High background
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S0 Existing surveys / 相邻综述，核心记忆对象是 story / character / scene consistency，记忆载体是 long storytelling architectures。在综述中主要作用：与 narrative/entity memory 最接近，但它不是 memory lifecycle 综述。

## 3. Memory object

story / character / scene consistency

## 4. Memory substrate

long storytelling architectures

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：与 narrative/entity memory 最接近，但它不是 memory lifecycle 综述。 |
| Store | 初步载体：long storytelling architectures |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S0 Existing surveys / 相邻综述
- Role in survey: 与 narrative/entity memory 最接近，但它不是 memory lifecycle 综述。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `story / character / scene consistency` 与 `long storytelling architectures` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# A Mechanistic View on Video Generation as World Models: State and Dynamics

## 1. Metadata

- Year: 2026
- ID: arXiv:2601.17067
- URL: https://arxiv.org/abs/2601.17067
- Category: S0 Existing surveys / 相邻综述
- Priority: High background
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S0 Existing surveys / 相邻综述，核心记忆对象是 state construction / dynamics，记忆载体是 implicit context / explicit latent compression。在综述中主要作用：和本文的 world-state memory 论点高度相关，可引用其 state/dynamics taxonomy。

## 3. Memory object

state construction / dynamics

## 4. Memory substrate

implicit context / explicit latent compression

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：和本文的 world-state memory 论点高度相关，可引用其 state/dynamics taxonomy。 |
| Store | 初步载体：implicit context / explicit latent compression |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S0 Existing surveys / 相邻综述
- Role in survey: 和本文的 world-state memory 论点高度相关，可引用其 state/dynamics taxonomy。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `state construction / dynamics` 与 `implicit context / explicit latent compression` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Video Generation Models as World Models: Efficient Paradigms, Architectures and Algorithms

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.28489
- URL: https://arxiv.org/abs/2603.28489
- Category: S0 Existing surveys / 相邻综述
- Priority: High background
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S0 Existing surveys / 相邻综述，核心记忆对象是 efficient world modeling，记忆载体是 efficient paradigms / architectures / inference。在综述中主要作用：说明 world-model survey 主要从效率切入，不以 memory object/substrate 为主。

## 3. Memory object

efficient world modeling

## 4. Memory substrate

efficient paradigms / architectures / inference

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：说明 world-model survey 主要从效率切入，不以 memory object/substrate 为主。 |
| Store | 初步载体：efficient paradigms / architectures / inference |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S0 Existing surveys / 相邻综述
- Role in survey: 说明 world-model survey 主要从效率切入，不以 memory object/substrate 为主。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `efficient world modeling` 与 `efficient paradigms / architectures / inference` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Diffusion Forcing

## 1. Metadata

- Year: 2024
- ID: arXiv:2407.01392
- URL: https://arxiv.org/abs/2407.01392
- Category: S1 AR / streaming video generation backbones
- Priority: Core background
- Status: From prior docs / To verify

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 long sequential generation，记忆载体是 per-token independent noise / forcing family。在综述中主要作用：Forcing 家族源头。

## 3. Memory object

long sequential generation

## 4. Memory substrate

per-token independent noise / forcing family

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：Forcing 家族源头。 |
| Store | 初步载体：per-token independent noise / forcing family |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: Forcing 家族源头。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long sequential generation` 与 `per-token independent noise / forcing family` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# CausVid

## 1. Metadata

- Year: 2024/2025
- ID: arXiv:2412.07772
- URL: https://arxiv.org/abs/2412.07772
- Category: S1 AR / streaming video generation backbones
- Priority: Core background
- Status: From prior docs / To verify

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 causal long video rollout，记忆载体是 block-causal + KV cache。在综述中主要作用：因果视频蒸馏和 KV cache baseline。

## 3. Memory object

causal long video rollout

## 4. Memory substrate

block-causal + KV cache

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：因果视频蒸馏和 KV cache baseline。 |
| Store | 初步载体：block-causal + KV cache |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 因果视频蒸馏和 KV cache baseline。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `causal long video rollout` 与 `block-causal + KV cache` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Wan: Open and Advanced Large-Scale Video Generative Models

## 1. Metadata

- Year: 2025
- ID: arXiv:2503.20314
- URL: https://arxiv.org/abs/2503.20314
- Category: S1 AR / streaming video generation backbones
- Priority: Core background
- Status: Mentioned by web; To verify details

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 base T2V/I2V backbone，记忆载体是 large-scale video generative model。在综述中主要作用：很多 2026 memory 方法基于 Wan2.1/2.2，需要作为 backbone 背景引用。

## 3. Memory object

base T2V/I2V backbone

## 4. Memory substrate

large-scale video generative model

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：很多 2026 memory 方法基于 Wan2.1/2.2，需要作为 backbone 背景引用。 |
| Store | 初步载体：large-scale video generative model |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 很多 2026 memory 方法基于 Wan2.1/2.2，需要作为 backbone 背景引用。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `base T2V/I2V backbone` 与 `large-scale video generative model` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# FramePack

## 1. Metadata

- Year: 2025
- ID: arXiv:2504.12626
- URL: https://arxiv.org/abs/2504.12626
- Category: S1 AR / streaming video generation backbones
- Priority: Core background
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 fixed-length historical context，记忆载体是 frame/context packing。在综述中主要作用：说明 context compression 是 memory substrate 之一。

## 3. Memory object

fixed-length historical context

## 4. Memory substrate

frame/context packing

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：说明 context compression 是 memory substrate 之一。 |
| Store | 初步载体：frame/context packing |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 说明 context compression 是 memory substrate 之一。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `fixed-length historical context` 与 `frame/context packing` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Self Forcing

## 1. Metadata

- Year: 2025
- ID: arXiv:2506.08009
- URL: https://arxiv.org/abs/2506.08009
- Category: S1 AR / streaming video generation backbones
- Priority: Core backbone
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 self-generated rollout memory，记忆载体是 KV-cache enabled autoregressive training。在综述中主要作用：后续 training-free memory 方法的重要 backbone。

## 3. Memory object

self-generated rollout memory

## 4. Memory substrate

KV-cache enabled autoregressive training

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：后续 training-free memory 方法的重要 backbone。 |
| Store | 初步载体：KV-cache enabled autoregressive training |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 后续 training-free memory 方法的重要 backbone。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `self-generated rollout memory` 与 `KV-cache enabled autoregressive training` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# LongLive

## 1. Metadata

- Year: 2025
- ID: arXiv:2509.22622
- URL: https://arxiv.org/abs/2509.22622
- Category: S1 AR / streaming video generation backbones
- Priority: Core backbone
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 long-horizon frame-level AR memory，记忆载体是 causal attention / KV recache / frame sink。在综述中主要作用：长视频 AR memory 重要平台；适合做 taxonomy 背景。

## 3. Memory object

long-horizon frame-level AR memory

## 4. Memory substrate

causal attention / KV recache / frame sink

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：长视频 AR memory 重要平台；适合做 taxonomy 背景。 |
| Store | 初步载体：causal attention / KV recache / frame sink |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 长视频 AR memory 重要平台；适合做 taxonomy 背景。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-horizon frame-level AR memory` 与 `causal attention / KV recache / frame sink` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Rolling Forcing

## 1. Metadata

- Year: 2025
- ID: arXiv:2509.25161
- URL: https://arxiv.org/abs/2509.25161
- Category: S1 AR / streaming video generation backbones
- Priority: Core backbone
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 rolling historical context，记忆载体是 rolling-window joint denoising + frame-0 attention sink。在综述中主要作用：主流 streaming AR backbone；attention sink 是全局锚点记忆。

## 3. Memory object

rolling historical context

## 4. Memory substrate

rolling-window joint denoising + frame-0 attention sink

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：主流 streaming AR backbone；attention sink 是全局锚点记忆。 |
| Store | 初步载体：rolling-window joint denoising + frame-0 attention sink |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 主流 streaming AR backbone；attention sink 是全局锚点记忆。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `rolling historical context` 与 `rolling-window joint denoising + frame-0 attention sink` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Infinity-RoPE

## 1. Metadata

- Year: 2025/2026
- ID: arXiv:2511.20649
- URL: https://arxiv.org/abs/2511.20649
- Category: S1 AR / streaming video generation backbones
- Priority: Core related
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 infinite action-controllable rollout，记忆载体是 Block-Relativistic RoPE / KV Flush / RoPE Cut。在综述中主要作用：同时属于 positional memory；适合作为 long action rollout 的位置策略。

## 3. Memory object

infinite action-controllable rollout

## 4. Memory substrate

Block-Relativistic RoPE / KV Flush / RoPE Cut

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：同时属于 positional memory；适合作为 long action rollout 的位置策略。 |
| Store | 初步载体：Block-Relativistic RoPE / KV Flush / RoPE Cut |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 同时属于 positional memory；适合作为 long action rollout 的位置策略。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `infinite action-controllable rollout` 与 `Block-Relativistic RoPE / KV Flush / RoPE Cut` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Causal-Forcing

## 1. Metadata

- Year: 2026
- ID: arXiv:2602.02214
- URL: https://arxiv.org/abs/2602.02214
- Category: S1 AR / streaming video generation backbones
- Priority: Core backbone
- Status: From prior docs / To verify

## 2. One-sentence takeaway

该论文归入 S1 AR / streaming video generation backbones，核心记忆对象是 block-causal AR video，记忆载体是 framewise/chunkwise causal generation。在综述中主要作用：与 Self/Rolling Forcing 并列的 AR backbone。

## 3. Memory object

block-causal AR video

## 4. Memory substrate

framewise/chunkwise causal generation

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：与 Self/Rolling Forcing 并列的 AR backbone。 |
| Store | 初步载体：framewise/chunkwise causal generation |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S1 AR / streaming video generation backbones
- Role in survey: 与 Self/Rolling Forcing 并列的 AR backbone。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `block-causal AR video` 与 `framewise/chunkwise causal generation` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.05081
- URL: https://arxiv.org/abs/2512.05081
- Category: S2 KV cache / attention memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

Deep Sink + Participative Compression 代表。核心价值是指出 attention sink 不是越强越好，过强 sink 会造成 motion stagnation；需要选择真正参与近期生成的 token。

## 3. Memory object

global context + active recent tokens

## 4. Memory substrate

deep sink + participative compression

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：说明 attention sink 不是越强越好；过强会 motion stagnation。 |
| Store | 初步载体：deep sink + participative compression |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 说明 attention sink 不是越强越好；过强会 motion stagnation。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `global context + active recent tokens` 与 `deep sink + participative compression` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# MAG: Memorize-and-Generate for Long Video Generation

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.18741
- URL: https://arxiv.org/html/2512.18741v1
- Category: S2 KV cache / attention memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S2 KV cache / attention memory，核心记忆对象是 history scene consistency，记忆载体是 memory compression model + generation model。在综述中主要作用：将 memory compression 和 generation 解耦，适合 retrieval memory 章节。

## 3. Memory object

history scene consistency

## 4. Memory substrate

memory compression model + generation model

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：将 memory compression 和 generation 解耦，适合 retrieval memory 章节。 |
| Store | 初步载体：memory compression model + generation model |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 将 memory compression 和 generation 解耦，适合 retrieval memory 章节。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `history scene consistency` 与 `memory compression model + generation model` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.12513
- URL: https://arxiv.org/abs/2603.12513
- Category: S2 KV cache / attention memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

位置-记忆协同代表。Dual EMA memory tokens 同时保长期身份/场景和近期动态；Online RoPE Indexing 缓存未旋转 key，在 attention 时再施加位置编码，避免 EMA 聚合不同相位 key。适合第五章精讲。

## 3. Memory object

identity + recent dynamics compressed memory

## 4. Memory substrate

dual EMA memory tokens + unrotated KV + online RoPE

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：把 memory compression 和 RoPE phase 解耦联系起来，技术主线非常关键。 |
| Store | 初步载体：dual EMA memory tokens + unrotated KV + online RoPE |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 把 memory compression 和 RoPE phase 解耦联系起来，技术主线非常关键。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `identity + recent dynamics compressed memory` 与 `dual EMA memory tokens + unrotated KV + online RoPE` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.27469
- URL: https://arxiv.org/abs/2603.27469
- Category: S2 KV cache / attention memory
- Priority: High
- Status: Verified by web, added in v0.2

## 2. One-sentence takeaway

系统记忆代表。系统比较 33 种 KV 量化/压缩策略，说明 nominal compression 不等于实际显存/质量收益。

## 3. Memory object

system memory / KV budget

## 4. Memory substrate

KV-cache quantization and compression policies

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：补充系统维度：量化/压缩不只是省显存，也会影响 drift、fidelity 与实际部署。 |
| Store | 初步载体：KV-cache quantization and compression policies |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 补充系统维度：量化/压缩不只是省显存，也会影响 drift、fidelity 与实际部署。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `system memory / KV budget` 与 `KV-cache quantization and compression policies` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Pyramid Forcing: Head-Aware Pyramid KV Cache Policy for High-Quality Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.13111
- URL: https://arxiv.org/abs/2605.13111
- Category: S2 KV cache / attention memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S2 KV cache / attention memory，核心记忆对象是 head-specific temporal memory，记忆载体是 Anchor/Wave/Veil per-head KV cache。在综述中主要作用：head-aware memory 的核心论文；可以引出 identity/motion/layout head specialization。

## 3. Memory object

head-specific temporal memory

## 4. Memory substrate

Anchor/Wave/Veil per-head KV cache

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：head-aware memory 的核心论文；可以引出 identity/motion/layout head specialization。 |
| Store | 初步载体：Anchor/Wave/Veil per-head KV cache |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: head-aware memory 的核心论文；可以引出 identity/motion/layout head specialization。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `head-specific temporal memory` 与 `Anchor/Wave/Veil per-head KV cache` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Echo-Forcing: A Scene Memory Framework for Interactive Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.16003
- URL: https://arxiv.org/abs/2605.16003
- Category: S2 KV cache / attention memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

场景记忆代表。将历史 KV 从均质 cache 变为 preserve-recall-forget 生命周期：Hierarchical Temporal Memory 分离 early anchors、compressed history、recent window；Scene Recall Frames 将旧场景压缩为可召回 KV；Difference-aware Memory Decay 抑制与新场景冲突的旧 token。适合第四章精讲。局限是偏 scene memory，不直接解决实体身份。

## 3. Memory object

scene memory / historical scene recall

## 4. Memory substrate

hierarchical temporal KV memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：场景记忆核心论文：stable anchor、compressed history、recent window、scene recall、difference-aware decay。 |
| Store | 初步载体：hierarchical temporal KV memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 场景记忆核心论文：stable anchor、compressed history、recent window、scene recall、difference-aware decay。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `scene memory / historical scene recall` 与 `hierarchical temporal KV memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Future Forcing: Future-aware Training-free KV Cache Policy for Autoregressive Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.30083
- URL: https://arxiv.org/abs/2605.30083
- Category: S2 KV cache / attention memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

Future-aware KV cache 代表。不是只看当前 attention，而是估计 future query proxy，保留未来会重要的历史 token。

## 3. Memory object

future-useful historical tokens

## 4. Memory substrate

future query proxy + cache policy

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：从 past-aware cache 走向 future-aware cache。 |
| Store | 初步载体：future query proxy + cache policy |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 从 past-aware cache 走向 future-aware cache。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `future-useful historical tokens` 与 `future query proxy + cache policy` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# OmniMem: A General Retrieval-Augmented Framework for Long Video Generation / full-range KV retrieval

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.30519
- URL: https://arxiv.org/abs/2605.30519
- Category: S2 KV cache / attention memory
- Priority: High
- Status: Verified by web title/abstract search

## 2. One-sentence takeaway

Full-range sparse KV retrieval 代表。保留对全历史 KV 的显式稀疏访问，而不是简单压缩或截断。

## 3. Memory object

long-range sparse KV memory

## 4. Memory substrate

sparse scattered KV retrieval

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：用于 full-range sparse memory retrieval 分类。 |
| Store | 初步载体：sparse scattered KV retrieval |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 用于 full-range sparse memory retrieval 分类。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-range sparse KV memory` 与 `sparse scattered KV retrieval` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# LVSA: Training-Free Sparse Attention for Long Video Diffusion

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.31057
- URL: https://arxiv.org/abs/2605.31057
- Category: S2 KV cache / attention memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

Sparse attention + rotating global anchors 代表。强调固定全局锚点会产生 fixed-grid bias，并提出 VQeval 惩罚 loop/frozen 退化。

## 3. Memory object

global anchor / anti-loop memory

## 4. Memory substrate

block-sparse attention + rotating global anchors

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：旋转全局锚点与 VQeval；提醒普通 consistency metric 可能奖励 loop/frozen video。 |
| Store | 初步载体：block-sparse attention + rotating global anchors |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 旋转全局锚点与 VQeval；提醒普通 consistency metric 可能奖励 loop/frozen video。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `global anchor / anti-loop memory` 与 `block-sparse attention + rotating global anchors` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# DecMem: Decoupled Global and Local Memory for Minute-long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.31336
- URL: https://arxiv.org/abs/2605.31336
- Category: S2 KV cache / attention memory
- Priority: High
- Status: From prior docs / To verify

## 2. One-sentence takeaway

该论文归入 S2 KV cache / attention memory，核心记忆对象是 global-local memory，记忆载体是 Sparse Global Memory + Anchored Local Memory。在综述中主要作用：全局/局部 memory 解耦代表。

## 3. Memory object

global-local memory

## 4. Memory substrate

Sparse Global Memory + Anchored Local Memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：全局/局部 memory 解耦代表。 |
| Store | 初步载体：Sparse Global Memory + Anchored Local Memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 全局/局部 memory 解耦代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `global-local memory` 与 `Sparse Global Memory + Anchored Local Memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.02553
- URL: https://arxiv.org/abs/2606.02553
- Category: S2 KV cache / attention memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

Retrieval-augmented long video generation 代表。将自生成历史 latents 组织成 dynamic searchable history，解决 sliding-window 轨迹一旦漂移就不可逆的问题。

## 3. Memory object

retrieval over long video context

## 4. Memory substrate

retrieval-augmented historical context

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：把 RAG 思路引入 LongLive/long video memory。 |
| Store | 初步载体：retrieval-augmented historical context |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S2 KV cache / attention memory
- Role in survey: 把 RAG 思路引入 LongLive/long video memory。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `retrieval over long video context` 与 `retrieval-augmented historical context` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# FLEX / Train Short, Inference Long

## 1. Metadata

- Year: 2026
- ID: arXiv:2602.14027
- URL: https://arxiv.org/abs/2602.14027
- Category: S3 Positional / RoPE memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

position-frequency 结合代表。用 frequency-aware RoPE 与 antiphase noise 延长 horizon。

## 3. Memory object

temporal horizon extension

## 4. Memory substrate

frequency-aware RoPE modulation + antiphase noise + sink

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：把 3D RoPE spectral bias 和动态先验不足联系起来。 |
| Store | 初步载体：frequency-aware RoPE modulation + antiphase noise + sink |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S3 Positional / RoPE memory
- Role in survey: 把 3D RoPE spectral bias 和动态先验不足联系起来。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `temporal horizon extension` 与 `frequency-aware RoPE modulation + antiphase noise + sink` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# MemRoPE

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.12513
- URL: https://arxiv.org/abs/2603.12513
- Category: S3 Positional / RoPE memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

位置-记忆协同代表。Dual EMA memory tokens 同时保长期身份/场景和近期动态；Online RoPE Indexing 缓存未旋转 key，在 attention 时再施加位置编码，避免 EMA 聚合不同相位 key。适合第五章精讲。

## 3. Memory object

position-free historical keys

## 4. Memory substrate

unrotated key cache + online RoPE indexing

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：位置相位冲突的最重要代表。 |
| Store | 初步载体：unrotated key cache + online RoPE indexing |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S3 Positional / RoPE memory
- Role in survey: 位置相位冲突的最重要代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `position-free historical keys` 与 `unrotated key cache + online RoPE indexing` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Pyramid Forcing

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.13111
- URL: https://arxiv.org/abs/2605.13111
- Category: S3 Positional / RoPE memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S3 Positional / RoPE memory，核心记忆对象是 long-horizon temporal coordinates，记忆载体是 dynamic RoPE remap + head-aware cache。在综述中主要作用：将位置 remap 和 head-aware cache 结合。

## 3. Memory object

long-horizon temporal coordinates

## 4. Memory substrate

dynamic RoPE remap + head-aware cache

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：将位置 remap 和 head-aware cache 结合。 |
| Store | 初步载体：dynamic RoPE remap + head-aware cache |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S3 Positional / RoPE memory
- Role in survey: 将位置 remap 和 head-aware cache 结合。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-horizon temporal coordinates` 与 `dynamic RoPE remap + head-aware cache` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# ConsisID: Identity-Preserving Text-to-Video Generation by Frequency Decomposition

## 1. Metadata

- Year: 2024/2025
- ID: arXiv:2411.17440
- URL: https://arxiv.org/abs/2411.17440
- Category: S4 Frequency / spectrum memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

频率分解身份保持代表。把身份分成低频全局脸部结构和高频身份细节，说明 ID drift 也有频谱层面的原因。

## 3. Memory object

face identity details

## 4. Memory substrate

low/high-frequency identity injection

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：把身份保持和频率分解联系起来。 |
| Store | 初步载体：low/high-frequency identity injection |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S4 Frequency / spectrum memory
- Role in survey: 把身份保持和频率分解联系起来。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `face identity details` 与 `low/high-frequency identity injection` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# FreeLong / FreeLong++: Training-Free Long Video Generation via Multi-band SpectralFusion

## 1. Metadata

- Year: 2025
- ID: arXiv:2507.00162
- URL: https://arxiv.org/abs/2507.00162
- Category: S4 Frequency / spectrum memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

频谱记忆代表。通过多频带融合保留低频长程语义和高频细节/动态。

## 3. Memory object

long-range semantics + high-frequency details

## 4. Memory substrate

multi-band spectral fusion / 3D FFT / SpecMix

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：频域长视频方法主代表。 |
| Store | 初步载体：multi-band spectral fusion / 3D FFT / SpecMix |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S4 Frequency / spectrum memory
- Role in survey: 频域长视频方法主代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-range semantics + high-frequency details` 与 `multi-band spectral fusion / 3D FFT / SpecMix` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# FLEX

## 1. Metadata

- Year: 2026
- ID: arXiv:2602.14027
- URL: https://arxiv.org/abs/2602.14027
- Category: S4 Frequency / spectrum memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

position-frequency 结合代表。用 frequency-aware RoPE 与 antiphase noise 延长 horizon。

## 3. Memory object

dynamic prior and temporal frequency

## 4. Memory substrate

frequency-aware RoPE + antiphase noise

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：连接 positional memory 和 spectral memory。 |
| Store | 初步载体：frequency-aware RoPE + antiphase noise |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S4 Frequency / spectrum memory
- Role in survey: 连接 positional memory 和 spectral memory。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `dynamic prior and temporal frequency` 与 `frequency-aware RoPE + antiphase noise` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.06509
- URL: https://arxiv.org/abs/2605.06509
- Category: S4 Frequency / spectrum memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

singular-spectrum correction 代表。解释长窗口 attention 会导致谱集中，从而保结构但丢动态/细节。

## 3. Memory object

dynamic/high-frequency preservation

## 4. Memory substrate

singular-spectrum reconstruction

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：解释大窗口 attention 的低秩谱集中和动态抹平。 |
| Store | 初步载体：singular-spectrum reconstruction |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S4 Frequency / spectrum memory
- Role in survey: 解释大窗口 attention 的低秩谱集中和动态抹平。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `dynamic/high-frequency preservation` 与 `singular-spectrum reconstruction` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation

## 1. Metadata

- Year: 2024
- ID: arXiv:2405.01434
- URL: https://arxiv.org/abs/2405.01434
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 story character identity，记忆载体是 consistent self-attention + semantic motion predictor。在综述中主要作用：早期 consistent attention / character consistency 代表。

## 3. Memory object

story character identity

## 4. Memory substrate

consistent self-attention + semantic motion predictor

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：早期 consistent attention / character consistency 代表。 |
| Store | 初步载体：consistent self-attention + semantic motion predictor |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 早期 consistent attention / character consistency 代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `story character identity` 与 `consistent self-attention + semantic motion predictor` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# ConsisID

## 1. Metadata

- Year: 2024/2025
- ID: arXiv:2411.17440
- URL: https://arxiv.org/abs/2411.17440
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

频率分解身份保持代表。把身份分成低频全局脸部结构和高频身份细节，说明 ID drift 也有频谱层面的原因。

## 3. Memory object

human identity

## 4. Memory substrate

frequency-decomposed reference identity features

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：reference ID + frequency memory 双重相关。 |
| Store | 初步载体：frequency-decomposed reference identity features |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: reference ID + frequency memory 双重相关。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `human identity` 与 `frequency-decomposed reference identity features` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Video Storyboarding: Multi-Shot Character Consistency for Text-to-Video Generation

## 1. Metadata

- Year: 2024
- ID: arXiv:2412.07750
- URL: https://arxiv.org/abs/2412.07750
- Category: S5 Identity / entity / narrative memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

身份-运动 trade-off 关键论文。指出 self-attention query 同时编码 identity 和 motion，直接共享/注入可能保身份但伤动态。

## 3. Memory object

multi-shot character identity

## 4. Memory substrate

query injection / attention feature control

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：identity-motion trade-off 的关键论文。 |
| Store | 初步载体：query injection / attention feature control |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: identity-motion trade-off 的关键论文。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `multi-shot character identity` 与 `query injection / attention feature control` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# TPIGE: Identity-Preserving Text-to-Video Generation via Training-Free Prompt, Image, and Guidance Enhancement

## 1. Metadata

- Year: 2025
- ID: arXiv:2509.01362
- URL: https://arxiv.org/abs/2509.01362
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 reference subject identity，记忆载体是 prompt/image/guidance enhancement。在综述中主要作用：输入侧 training-free ID memory 的代表。

## 3. Memory object

reference subject identity

## 4. Memory substrate

prompt/image/guidance enhancement

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：输入侧 training-free ID memory 的代表。 |
| Store | 初步载体：prompt/image/guidance enhancement |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 输入侧 training-free ID memory 的代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `reference subject identity` 与 `prompt/image/guidance enhancement` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# StoryMem: Long Story Video Generation with Compact Memory Bank

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.19539
- URL: https://arxiv.org/html/2512.19539v1
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 characters / scenes / style，记忆载体是 compact memory bank + shot-by-shot generation。在综述中主要作用：故事视频中的 compact memory bank。

## 3. Memory object

characters / scenes / style

## 4. Memory substrate

compact memory bank + shot-by-shot generation

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：故事视频中的 compact memory bank。 |
| Store | 初步载体：compact memory bank + shot-by-shot generation |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 故事视频中的 compact memory bank。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `characters / scenes / style` 与 `compact memory bank + shot-by-shot generation` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# VideoMemory: Toward Consistent Video Generation via Memory Integration

## 1. Metadata

- Year: 2026
- ID: arXiv:2601.03655
- URL: https://arxiv.org/abs/2601.03655
- Category: S5 Identity / entity / narrative memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 character / prop / background consistency，记忆载体是 dynamic memory bank。在综述中主要作用：显式 memory integration 论文，适合 narrative memory 章节。

## 3. Memory object

character / prop / background consistency

## 4. Memory substrate

dynamic memory bank

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：显式 memory integration 论文，适合 narrative memory 章节。 |
| Store | 初步载体：dynamic memory bank |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 显式 memory integration 论文，适合 narrative memory 章节。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `character / prop / background consistency` 与 `dynamic memory bank` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory

## 1. Metadata

- Year: 2026
- ID: arXiv:2601.16296
- URL: https://arxiv.org/abs/2601.16296
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 multi-turn editing consistency，记忆载体是 external cache + retrieval + dynamic tokenization + compressor。在综述中主要作用：V2V 多轮编辑 memory 代表。

## 3. Memory object

multi-turn editing consistency

## 4. Memory substrate

external cache + retrieval + dynamic tokenization + compressor

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：V2V 多轮编辑 memory 代表。 |
| Store | 初步载体：external cache + retrieval + dynamic tokenization + compressor |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: V2V 多轮编辑 memory 代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `multi-turn editing consistency` 与 `external cache + retrieval + dynamic tokenization + compressor` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Gloria: Consistent Character Video Generation via Content Anchors

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.29931
- URL: https://arxiv.org/abs/2603.29931
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 character identity across long videos，记忆载体是 character-centric/content anchor frames。在综述中主要作用：anchor-based character memory 代表。

## 3. Memory object

character identity across long videos

## 4. Memory substrate

character-centric/content anchor frames

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：anchor-based character memory 代表。 |
| Store | 初步载体：character-centric/content anchor frames |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: anchor-based character memory 代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `character identity across long videos` 与 `character-centric/content anchor frames` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# IAMFlow: Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.18733
- URL: https://arxiv.org/abs/2605.18733
- Category: S5 Identity / entity / narrative memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

显式 identity-aware entity memory 代表。LLM 抽取实体/属性并分配 global ID，VLM 异步验证更新属性，解决 prompt transition 下的 identity drift、duplication 和 attribute loss。

## 3. Memory object

entity identity and attributes

## 4. Memory substrate

LLM global ID table + VLM attribute verification

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：显式实体/身份记忆核心论文。 |
| Store | 初步载体：LLM global ID table + VLM attribute verification |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 显式实体/身份记忆核心论文。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `entity identity and attributes` 与 `LLM global ID table + VLM attribute verification` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.23610
- URL: https://arxiv.org/abs/2605.23610
- Category: S5 Identity / entity / narrative memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

Entity-indexed sparse latent patch bank 代表。相比 full-frame memory，更适合避免背景噪声污染实体记忆。

## 3. Memory object

recurring entity appearance

## 4. Memory substrate

entity-indexed sparse latent patch bank

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：entity-centric latent patch memory 的核心代表。 |
| Store | 初步载体：entity-indexed sparse latent patch bank |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: entity-centric latent patch memory 的核心代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `recurring entity appearance` 与 `entity-indexed sparse latent patch bank` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.31033
- URL: https://arxiv.org/abs/2605.31033
- Category: S5 Identity / entity / narrative memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

Object-centric KV memory 代表。把记忆单位从“什么时候发生”转为“是什么实体”，用 semantic slots 索引高保真 KV tokens。

## 3. Memory object

object/entity persistence

## 4. Memory substrate

object-centric KV semantic slots

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：从 temporal-centric memory 转向 object-centric memory 的核心代表。 |
| Store | 初步载体：object-centric KV semantic slots |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 从 temporal-centric memory 转向 object-centric memory 的核心代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `object/entity persistence` 与 `object-centric KV semantic slots` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Memento: Reconstruct to Remember for Consistent Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.14667
- URL: https://arxiv.org/abs/2606.14667
- Category: S5 Identity / entity / narrative memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

Subject-reconstruction-guided memory 代表。核心假设是：真正保留主体证据的 memory bank 应该能单独重建主体；用 reconstruction loss 监督 recurring subject memory。

## 3. Memory object

recurring subject identity

## 4. Memory substrate

subject-reconstruction-guided memory bank + dual-query memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：把“记住主体”显式转化为可从 memory 重建主体的监督目标。 |
| Store | 初步载体：subject-reconstruction-guided memory bank + dual-query memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 把“记住主体”显式转化为可从 memory 重建主体的监督目标。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `recurring subject identity` 与 `subject-reconstruction-guided memory bank + dual-query memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Closed-Loop Triplet Synergistic Generation for Long-Form Video / CoTriSyGen

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.16184
- URL: https://arxiv.org/abs/2606.16184
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web, added in v0.2

## 2. One-sentence takeaway

closed-loop narrative memory 代表。VLM analyzer 将生成证据反馈到 prompt 和 mutable visual state，体现 memory update 而非静态存储。

## 3. Memory object

entity/narrative memory

## 4. Memory substrate

closed-loop visual-text-memory synergy + mutable visual state

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：补充 narrative memory：把生成结果反馈到 memory/prompt，体现 memory update 生命周期。 |
| Store | 初步载体：closed-loop visual-text-memory synergy + mutable visual state |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 补充 narrative memory：把生成结果反馈到 memory/prompt，体现 memory update 生命周期。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `entity/narrative memory` 与 `closed-loop visual-text-memory synergy + mutable visual state` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Corgi: Cached Memory Guided Video Generation

## 1. Metadata

- Year: 2025
- ID: WACV 2025
- URL: https://openaccess.thecvf.com/content/WACV2025/papers/Wu_Corgi_Cached_Memory_Guided_Video_Generation_WACV_2025_paper.pdf
- Category: S5 Identity / entity / narrative memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S5 Identity / entity / narrative memory，核心记忆对象是 multi-scene core memories，记忆载体是 cached latent memory bank / key frames。在综述中主要作用：早期 cached memory-guided video generation 代表。

## 3. Memory object

multi-scene core memories

## 4. Memory substrate

cached latent memory bank / key frames

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：早期 cached memory-guided video generation 代表。 |
| Store | 初步载体：cached latent memory bank / key frames |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S5 Identity / entity / narrative memory
- Role in survey: 早期 cached memory-guided video generation 代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `multi-scene core memories` 与 `cached latent memory bank / key frames` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval

## 1. Metadata

- Year: 2025
- ID: arXiv:2506.03141
- URL: https://arxiv.org/abs/2506.03141
- Category: S6 Retrieval / external memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S6 Retrieval / external memory，核心记忆对象是 scene revisit / context visibility，记忆载体是 historical context frames as memory。在综述中主要作用：历史帧检索作为 memory 的核心代表。

## 3. Memory object

scene revisit / context visibility

## 4. Memory substrate

historical context frames as memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：历史帧检索作为 memory 的核心代表。 |
| Store | 初步载体：historical context frames as memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S6 Retrieval / external memory
- Role in survey: 历史帧检索作为 memory 的核心代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `scene revisit / context visibility` 与 `historical context frames as memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# MAG

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.18741
- URL: https://arxiv.org/html/2512.18741v1
- Category: S6 Retrieval / external memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S6 Retrieval / external memory，核心记忆对象是 historical scene consistency，记忆载体是 decoupled memory compression and generation。在综述中主要作用：memory compression/retrieval 章节。

## 3. Memory object

historical scene consistency

## 4. Memory substrate

decoupled memory compression and generation

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：memory compression/retrieval 章节。 |
| Store | 初步载体：decoupled memory compression and generation |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S6 Retrieval / external memory
- Role in survey: memory compression/retrieval 章节。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `historical scene consistency` 与 `decoupled memory compression and generation` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# SlotMemory / EM-Vid / DecMem

## 1. Metadata

- Year: 2026
- ID: 2605.31033 / 2605.23610 / 2605.31336
- URL: 
- Category: S6 Retrieval / external memory
- Priority: High
- Status: Verified for SlotMemory and EM-Vid; DecMem to verify

## 2. One-sentence takeaway

Object-centric KV memory 代表。把记忆单位从“什么时候发生”转为“是什么实体”，用 semantic slots 索引高保真 KV tokens。

## 3. Memory object

entity/global-local memory

## 4. Memory substrate

slot / patch bank / decoupled memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：作为 retrieval memory 与 entity memory 的交叉。 |
| Store | 初步载体：slot / patch bank / decoupled memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S6 Retrieval / external memory
- Role in survey: 作为 retrieval memory 与 entity memory 的交叉。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `entity/global-local memory` 与 `slot / patch bank / decoupled memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# LongLive-RAG

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.02553
- URL: https://arxiv.org/abs/2606.02553
- Category: S6 Retrieval / external memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

Retrieval-augmented long video generation 代表。将自生成历史 latents 组织成 dynamic searchable history，解决 sliding-window 轨迹一旦漂移就不可逆的问题。

## 3. Memory object

long-range context retrieval

## 4. Memory substrate

retrieval-augmented historical frames/tokens

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：RAG for long video generation。 |
| Store | 初步载体：retrieval-augmented historical frames/tokens |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S6 Retrieval / external memory
- Role in survey: RAG for long video generation。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-range context retrieval` 与 `retrieval-augmented historical frames/tokens` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# WorldMem: Long-term Consistent World Simulation with Memory

## 1. Metadata

- Year: 2025
- ID: arXiv:2504.12369
- URL: https://arxiv.org/abs/2504.12369
- Category: S7 Video world model memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

video world model 中 frame/state memory 代表。memory 不只是历史图像，还要包含 pose、timestamp 等状态元数据。

## 3. Memory object

scene/world memory

## 4. Memory substrate

memory frames + states such as pose/timestamp

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：视频世界模型 memory bank 代表。 |
| Store | 初步载体：memory frames + states such as pose/timestamp |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: 视频世界模型 memory bank 代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `scene/world memory` 与 `memory frames + states such as pose/timestamp` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Long-Context State-Space Video World Models

## 1. Metadata

- Year: 2025
- ID: arXiv:2505.20171
- URL: https://arxiv.org/abs/2505.20171
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S7 Video world model memory，核心记忆对象是 long-range world state，记忆载体是 SSM global memory + local attention。在综述中主要作用：state-space memory 替代 attention memory 的代表。

## 3. Memory object

long-range world state

## 4. Memory substrate

SSM global memory + local attention

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：state-space memory 替代 attention memory 的代表。 |
| Store | 初步载体：SSM global memory + local attention |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: state-space memory 替代 attention memory 的代表。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-range world state` 与 `SSM global memory + local attention` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Learning World Models for Interactive Video Generation

## 1. Metadata

- Year: 2025
- ID: arXiv:2505.21996
- URL: https://arxiv.org/abs/2505.21996
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S7 Video world model memory，核心记忆对象是 interactive rollout memory，记忆载体是 VRAG + explicit global state conditioning。在综述中主要作用：指出 AR world model 的 compounding error 和 insufficient memory mechanisms。

## 3. Memory object

interactive rollout memory

## 4. Memory substrate

VRAG + explicit global state conditioning

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：指出 AR world model 的 compounding error 和 insufficient memory mechanisms。 |
| Store | 初步载体：VRAG + explicit global state conditioning |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: 指出 AR world model 的 compounding error 和 insufficient memory mechanisms。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `interactive rollout memory` 与 `VRAG + explicit global state conditioning` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Video World Models with Long-term Spatial Memory / SpMem

## 1. Metadata

- Year: 2025
- ID: arXiv:2506.05284
- URL: https://arxiv.org/abs/2506.05284
- Category: S7 Video world model memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

spatial memory 代表。采用 working/spatial/episodic memory 区分近期上下文、几何长期记忆和访问事件。

## 3. Memory object

long-term spatial memory

## 4. Memory substrate

working memory + spatial memory + episodic memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：geometry-grounded spatial memory 核心论文。 |
| Store | 初步载体：working memory + spatial memory + episodic memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: geometry-grounded spatial memory 核心论文。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `long-term spatial memory` 与 `working memory + spatial memory + episodic memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# WorldPack: Compressed Memory Improves Spatial Consistency in Video World Modeling

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.02473
- URL: https://arxiv.org/abs/2512.02473
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S7 Video world model memory，核心记忆对象是 spatial consistency，记忆载体是 trajectory packing + memory retrieval。在综述中主要作用：压缩记忆提升空间一致性。

## 3. Memory object

spatial consistency

## 4. Memory substrate

trajectory packing + memory retrieval

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：压缩记忆提升空间一致性。 |
| Store | 初步载体：trajectory packing + memory retrieval |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: 压缩记忆提升空间一致性。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `spatial consistency` 与 `trajectory packing + memory retrieval` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# RELIC: Real-time Long Context Interactive World Models

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.04040
- URL: https://arxiv.org/abs/2512.04040
- Category: S7 Video world model memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

实时交互 world model 代表。把历史 latent tokens、relative actions、absolute camera poses 统一进 memory/KV，用于交互式长程生成。

## 3. Memory object

interactive long-context memory

## 4. Memory substrate

compressed historical latent tokens + actions + camera poses in KV cache

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：实时交互 world model 中 latent/history/action/camera 统一进 KV cache。 |
| Store | 初步载体：compressed historical latent tokens + actions + camera poses in KV cache |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: 实时交互 world model 中 latent/history/action/camera 统一进 KV cache。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `interactive long-context memory` 与 `compressed historical latent tokens + actions + camera poses in KV cache` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# WorldPlay

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.14614
- URL: https://arxiv.org/abs/2512.14614
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S7 Video world model memory，核心记忆对象是 real-time interaction / memory attenuation，记忆载体是 Reconstituted Context Memory。在综述中主要作用：interactive world modeling 中动态重建过去上下文。

## 3. Memory object

real-time interaction / memory attenuation

## 4. Memory substrate

Reconstituted Context Memory

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：interactive world modeling 中动态重建过去上下文。 |
| Store | 初步载体：Reconstituted Context Memory |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: interactive world modeling 中动态重建过去上下文。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `real-time interaction / memory attenuation` 与 `Reconstituted Context Memory` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# MIND: Benchmarking Memory Consistency and Action Control in World Models

## 1. Metadata

- Year: 2026
- ID: arXiv:2602.08025
- URL: https://arxiv.org/abs/2602.08025
- Category: S7 Video world model memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

world model memory benchmark 代表。评估 memory consistency 和 action control，适合作为第九章核心 benchmark。

## 3. Memory object

memory consistency + action control

## 4. Memory substrate

benchmark / closed-loop revisiting

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：world model memory 评测核心 benchmark。 |
| Store | 初步载体：benchmark / closed-loop revisiting |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: world model memory 评测核心 benchmark。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `memory consistency + action control` 与 `benchmark / closed-loop revisiting` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Beyond Pixel Histories: World Models with Persistent 3D Memory

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.03482
- URL: https://arxiv.org/abs/2603.03482
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S7 Video world model memory，核心记忆对象是 persistent 3D environment，记忆载体是 explicit 3D memory beyond pixel histories。在综述中主要作用：强调 pixel history 不足，需要 persistent 3D memory。

## 3. Memory object

persistent 3D environment

## 4. Memory substrate

explicit 3D memory beyond pixel histories

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：强调 pixel history 不足，需要 persistent 3D memory。 |
| Store | 初步载体：explicit 3D memory beyond pixel histories |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: 强调 pixel history 不足，需要 persistent 3D memory。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `persistent 3D environment` 与 `explicit 3D memory beyond pixel histories` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# LiveWorld: Simulating Out-of-Sight Dynamics in Generative Video World Models

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.07145
- URL: https://arxiv.org/abs/2603.07145
- Category: S7 Video world model memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

out-of-sight dynamics 代表。指出传统 world model 会冻结不可见物体，用 persistent global state + monitor 机制使动态实体在视野外继续演化。

## 3. Memory object

out-of-sight dynamic world state

## 4. Memory substrate

persistent global state: static 3D background + dynamic entities

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：out-of-sight dynamics 核心论文：世界不可见时也应继续演化。 |
| Store | 初步载体：persistent global state: static 3D background + dynamic entities |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: out-of-sight dynamics 核心论文：世界不可见时也应继续演化。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `out-of-sight dynamic world state` 与 `persistent global state: static 3D background + dynamic entities` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Hybrid Spatial Memory / MosaicMem

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.17117
- URL: https://arxiv.org/abs/2603.17117
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S7 Video world model memory，核心记忆对象是 controllable spatial world model，记忆载体是 3D patch lifting + native conditioning。在综述中主要作用：hybrid spatial memory。

## 3. Memory object

controllable spatial world model

## 4. Memory substrate

3D patch lifting + native conditioning

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：hybrid spatial memory。 |
| Store | 初步载体：3D patch lifting + native conditioning |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: hybrid spatial memory。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `controllable spatial world model` 与 `3D patch lifting + native conditioning` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# ReMind: Dynamic Memory for Out-of-Sight State Evolution

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.25333
- URL: https://arxiv.org/html/2605.25333v1
- Category: S7 Video world model memory
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

world model memory benchmark 代表。评估 memory consistency 和 action control，适合作为第九章核心 benchmark。

## 3. Memory object

hidden state evolution

## 4. Memory substrate

memory-oriented data + event-aware training + cache adaptation

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：out-of-sight state evolution。 |
| Store | 初步载体：memory-oriented data + event-aware training + cache adaptation |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: out-of-sight state evolution。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `hidden state evolution` 与 `memory-oriented data + event-aware training + cache adaptation` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# Latent Spatial Memory for Video World Models / Mirage

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.09828
- URL: https://arxiv.org/abs/2606.09828
- Category: S7 Video world model memory
- Priority: Must-read
- Status: Verified by web

## 2. One-sentence takeaway

latent spatial memory 代表。把 3D memory 放在 diffusion latent space，避免 RGB point cloud 的 repeated rendering 和 VAE 损失。

## 3. Memory object

3D spatial persistence

## 4. Memory substrate

persistent latent 3D cache / depth-guided back-projection

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：latent-space 3D memory 核心新论文。 |
| Store | 初步载体：persistent latent 3D cache / depth-guided back-projection |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S7 Video world model memory
- Role in survey: latent-space 3D memory 核心新论文。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `3D spatial persistence` 与 `persistent latent 3D cache / depth-guided back-projection` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# NarraStream-Bench

## 1. Metadata

- Year: 2026
- ID: IAMFlow paper
- URL: https://arxiv.org/abs/2605.18733
- Category: S8 Evaluation / benchmarks
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S8 Evaluation / benchmarks，核心记忆对象是 multi-prompt narrative identity consistency，记忆载体是 benchmark。在综述中主要作用：叙事/多实体 identity memory 评测。

## 3. Memory object

multi-prompt narrative identity consistency

## 4. Memory substrate

benchmark

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：叙事/多实体 identity memory 评测。 |
| Store | 初步载体：benchmark |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S8 Evaluation / benchmarks
- Role in survey: 叙事/多实体 identity memory 评测。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `multi-prompt narrative identity consistency` 与 `benchmark` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。

---

# VQeval

## 1. Metadata

- Year: 2026
- ID: LVSA paper
- URL: https://arxiv.org/abs/2605.31057
- Category: S8 Evaluation / benchmarks
- Priority: High
- Status: Verified by web

## 2. One-sentence takeaway

该论文归入 S8 Evaluation / benchmarks，核心记忆对象是 loop/frozen degeneration penalty，记忆载体是 metric/evaluator。在综述中主要作用：评测章节的重要论据：普通 consistency metric 可能奖励静止循环。

## 3. Memory object

loop/frozen degeneration penalty

## 4. Memory substrate

metric/evaluator

## 5. Memory lifecycle extraction

| Stage | Notes |
|---|---|
| Write | 需要从论文正文继续补全；初步依据：评测章节的重要论据：普通 consistency metric 可能奖励静止循环。 |
| Store | 初步载体：metric/evaluator |
| Retrieve | 检查是否通过 attention/query/entity/camera/semantic retrieval 召回。 |
| Use | 检查召回内容是进入 KV、cross-attention、prompt rewriting、guidance 还是 state conditioning。 |
| Update | 检查是否有 EMA、VLM verification、memory write-back、state transition 或 closed-loop correction。 |
| Forget | 检查是否有 decay、eviction、flush、conflict-aware forgetting 或 budget pruning。 |
| Evaluate | 记录使用的 benchmark、指标以及是否存在 loop/frozen metric trap。 |

## 6. Survey placement

- Recommended chapter: S8 Evaluation / benchmarks
- Role in survey: 评测章节的重要论据：普通 consistency metric 可能奖励静止循环。

## 7. Strengths

- 明确服务于 memory-centric taxonomy。
- 可用于讨论 `loop/frozen degeneration penalty` 与 `metric/evaluator` 的关系。

## 8. Limitations / questions for full PDF reading

- 需要下载 PDF 后补充方法图、公式、实验设置、消融细节。
- 需要确认是否有代码、benchmark 和可复现实验协议。
- 需要记录与 Echo-Forcing / MemRoPE / Pyramid-Forcing / IAMFlow / WorldMem 等代表论文的差异。

## 9. Relation to our possible future ideas

如果与 identity recall、head-role routing、cross-layer residual、dual-track per-head RoPE 或 unified entity-state memory 有交集，应在 future directions 中引用，而不是在综述主体过度强调自己的方法。
