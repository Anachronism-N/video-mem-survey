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
