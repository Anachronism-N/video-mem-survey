# H2O / SnapKV / Quest / PyramidKV / SirLLM

## 1. Metadata

- Year: 2023-2025
- ID: LLM KV cache literature
- URL: N/A
- Category: S2 KV cache / attention memory 
- Priority: Background
- Training-free: Yes
- Original status: From prior docs / To verify individually
- Reading status: metadata-only
- Source basis: structured metadata + prior survey table

## 2. One-sentence takeaway

H2O / SnapKV / Quest / PyramidKV / SirLLM 属于 S2 KV cache / attention memory；当前根据题名、分类表与可用网页元信息定位为：作为 KV cache policy 的通用来源，不要喧宾夺主。。

## 3. Problem / failure mode

需要从论文网页/HTML 继续精化；初步问题是 generic KV cache selection/compression 在 heavy hitter / query-aware / layer budget / entropy retention 载体上的建模、压缩、检索或评测。

## 4. Memory object

- generic KV cache selection/compression

## 5. Memory substrate

- heavy hitter / query-aware / layer budget / entropy retention

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | 记录与 generic KV cache selection/compression 相关的历史状态或评测对象。 |
| Store | 主要载体：heavy hitter / query-aware / layer budget / entropy retention。 |
| Retrieve | 若为方法论文，检查其是否通过 attention、query、entity ID、camera pose、semantic retrieval 或 benchmark protocol 触发记忆召回；若为综述/benchmark，则记录其评测/分类逻辑。 |
| Use | 用于 作为 KV cache policy 的通用来源，不要喧宾夺主。。 |
| Update | 需要在二轮 PDF/HTML 精读时补充是否存在 EMA、VLM verification、memory write-back、state transition、cache refresh 或 closed-loop correction。 |
| Forget | 需要二轮精读确认是否存在 decay、eviction、flush、conflict-aware forgetting、budget pruning 或仅依靠 retrieval relevance。 |
| Evaluate | 需要记录 benchmark、指标、消融和是否可能被 loop/frozen video 误导。 |

## 7. Strengths for this survey

可作为综述分类表中的相关条目；是否精讲取决于 priority。

## 8. Limitations / second-pass PDF checks

当前为结构化精读初版；公式、图表编号和实验细节需要 PDF/HTML 二轮复核。

## 9. Recommended placement

- Main category: S2 KV cache / attention memory 
- Role: 作为 KV cache policy 的通用来源，不要喧宾夺主。
- Priority: Background
