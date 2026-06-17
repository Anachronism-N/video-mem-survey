# 04 检索与更新协议

> 目标：保证 `video-mem-survey` 文献库可持续更新，尤其是在 2026 年 7 月后补齐“截至 2026 年 7 月”的最终版本。

---

## 1. 时间边界

当前版本截至：**2026-06-17**。

由于当前日期尚未到 2026 年 7 月，建议在以下时间点更新：

1. **2026-06-30**：补齐 6 月下旬 arXiv。
2. **2026-07-15**：补齐 7 月上旬 arXiv、会议 workshop 论文和项目页。
3. **2026-07-31**：做正式“截至 2026 年 7 月”的锁版。

---

## 2. 推荐检索关键词

### 2.1 General memory + video generation

```text
"video generation" "memory" "long video"
"long video generation" "KV cache" memory
"autoregressive video generation" "memory tokens"
"streaming video generation" "memory" "cache"
"training-free" "long video generation" "memory"
"scene memory" "video generation"
```

### 2.2 KV cache / attention / RoPE

```text
"video generation" "KV cache" "training-free"
"attention sink" "video diffusion"
"RoPE" "long video generation"
"Online RoPE Indexing" video generation
"head-aware" "KV cache" "video generation"
"sparse attention" "long video diffusion"
```

### 2.3 Identity / entity / narrative memory

```text
"identity-aware memory" "video generation"
"entity-centric memory" "video generation"
"object-centric KV memory" "video generation"
"character consistency" "memory" "long video"
"multi-shot video generation" "memory"
"narrative long video generation" "identity memory"
```

### 2.4 Video world model memory

```text
"video world model" "memory"
"world model" "spatial memory" video
"latent spatial memory" "video world models"
"out-of-sight dynamics" "video world models"
"persistent 3D memory" "world models"
"memory consistency" "action control" "world models"
"interactive video generation" "global state" memory
```

### 2.5 Evaluation / benchmark

```text
"VBench-Long" memory video generation
"VQeval" "long video"
"NarraStream-Bench" video generation
"MIND" "memory consistency" "world models"
"WorldScore" "video world models"
"out-of-sight" benchmark world model
```

---

## 3. 推荐检索源

1. arXiv advanced search。
2. Papers with Code。
3. Hugging Face papers。
4. OpenReview。
5. CVF Open Access。
6. GitHub awesome lists。
7. Google Scholar / Semantic Scholar。
8. 重点作者主页和项目页。

---

## 4. 纳入标准

一篇论文应至少满足以下条件之一：

- 提出显式 memory bank、memory token、memory cache、memory retrieval。
- 修改 KV cache、attention sink、sparse attention、cache eviction/compression。
- 处理 long video 中的 identity drift、scene recall、motion loop、prompt transition。
- 提出 entity/global ID/attribute table/object slot 类方法。
- 引入 3D/spatial/latent/world-state memory。
- 提出 memory consistency / revisit / out-of-sight dynamics 评测。

---

## 5. 排除标准

以下论文不应进入主表，除非与 memory 有直接关系：

- 普通 T2V/I2V 模型，没有长程一致性或 memory 机制。
- 只做美学质量、分辨率提升、加速，但不涉及历史状态或记忆。
- 普通视频编辑论文，除非涉及 multi-turn consistency / explicit memory。
- 纯 LLM/agent memory 论文，除非用于视频生成或 world model。

---

## 6. 每篇论文的阅读笔记模板

放入 `notes/paper_notes/`。

```markdown
# YEAR FirstAuthor - Short Title

## 1. Metadata

- Title:
- Authors:
- Venue / arXiv:
- URL:
- Code / project:
- Category:
- Priority:

## 2. Problem

这篇论文解决什么 memory failure？

## 3. Memory object

它记住什么？identity / scene / motion / position / entity / spatial / world-state？

## 4. Memory substrate

记忆存在什么载体里？frame / KV / token / RoPE / spectrum / entity table / 3D cache / SSM state？

## 5. Lifecycle

| Stage | Design |
|---|---|
| Write | |
| Store | |
| Retrieve | |
| Use | |
| Update | |
| Forget | |
| Evaluate | |

## 6. Strengths

## 7. Limitations

## 8. Relation to our survey

这篇论文放在哪一章？是否精讲？

## 9. Relation to our ideas

与 AAI / HRMR / DARV / active identity recall / entity-state memory 是否重叠？
```

---

## 7. 更新流程

每次新增论文：

1. 先写入 `tables/papers_master.csv`。
2. 再同步到 `01_paper_taxonomy_论文分类库.md` 对应类别。
3. 如果是 Must-read，写单篇 paper note。
4. 如果改变了 taxonomy，更新 `02_overall_idea_总体思路.md`。
5. 如果影响章节结构，更新 `03_survey_outline_综述写作大纲.md`。

---

## 8. 2026 年 7 月锁版 checklist

- [ ] 检索所有 `arXiv:2606` 与 `arXiv:2607` 中包含 memory / cache / identity / entity / world model 的论文。
- [ ] 检索 CVPR/ICCV/ECCV/NeurIPS/ICLR workshop 与 OpenReview。
- [ ] 逐篇确认 `From prior docs / To verify` 的条目。
- [ ] 删除不相关或不可验证条目。
- [ ] 为 Must-read 论文补齐 paper note。
- [ ] 更新论文分类库和 CSV。
- [ ] 更新 existing survey comparison。
- [ ] 更新 evaluation benchmark 表。
- [ ] 再生成一版 final outline。

---

## 9. 推荐锁版命名

```text
video-mem-survey_v0.2_2026-06-30.zip
video-mem-survey_v0.3_2026-07-15.zip
video-mem-survey_v1.0_2026-07-31.zip
```
