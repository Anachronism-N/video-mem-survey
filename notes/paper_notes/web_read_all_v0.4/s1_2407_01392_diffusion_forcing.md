# Diffusion Forcing

## 1. Metadata

- Year: 2024
- ID: arXiv:2407.01392
- URL: https://arxiv.org/abs/2407.01392
- Category: S1 AR / streaming video generation backbones 
- Priority: Core background
- Training-free: Trained
- Original status: From prior docs / To verify
- Reading status: metadata-web-ready
- Source basis: structured metadata + prior survey table

## 2. One-sentence takeaway

Diffusion Forcing 属于 S1 AR / streaming video generation backbones；当前根据题名、分类表与可用网页元信息定位为：Forcing 家族源头。。

## 3. Problem / failure mode

需要从论文网页/HTML 继续精化；初步问题是 long sequential generation 在 per-token independent noise / forcing family 载体上的建模、压缩、检索或评测。

## 4. Memory object

- long sequential generation

## 5. Memory substrate

- per-token independent noise / forcing family

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | 记录与 long sequential generation 相关的历史状态或评测对象。 |
| Store | 主要载体：per-token independent noise / forcing family。 |
| Retrieve | 若为方法论文，检查其是否通过 attention、query、entity ID、camera pose、semantic retrieval 或 benchmark protocol 触发记忆召回；若为综述/benchmark，则记录其评测/分类逻辑。 |
| Use | 用于 Forcing 家族源头。。 |
| Update | 需要在二轮 PDF/HTML 精读时补充是否存在 EMA、VLM verification、memory write-back、state transition、cache refresh 或 closed-loop correction。 |
| Forget | 需要二轮精读确认是否存在 decay、eviction、flush、conflict-aware forgetting、budget pruning 或仅依靠 retrieval relevance。 |
| Evaluate | 需要记录 benchmark、指标、消融和是否可能被 loop/frozen video 误导。 |

## 7. Strengths for this survey

可作为综述分类表中的相关条目；是否精讲取决于 priority。

## 8. Limitations / second-pass PDF checks

当前为结构化精读初版；公式、图表编号和实验细节需要 PDF/HTML 二轮复核。

## 9. Recommended placement

- Main category: S1 AR / streaming video generation backbones 
- Role: Forcing 家族源头。
- Priority: Core background
