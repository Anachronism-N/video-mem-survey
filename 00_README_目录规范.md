# video-mem-survey 目录规范

> 项目：视频生成与视频世界模型中的记忆系统综述  
> 当前版本：v0.1  
> 时间边界：当前整理截至 **2026-06-17**。由于现在尚未到 2026 年 7 月，所有“截至 2026 年 7 月”的表述都应在 2026-07-31 后进行二次检索与更新。  
> 目标：把已有调研、论文库、综述总思路、写作大纲和后续检索协议放入一个可持续维护的资料包。

---

## 1. 推荐目录结构

```text
video-mem-survey/
├── 00_README_目录规范.md
├── 01_paper_taxonomy_论文分类库.md
├── 02_overall_idea_总体思路.md
├── 03_survey_outline_综述写作大纲.md
├── 04_literature_search_protocol_检索与更新协议.md
├── tables/
│   └── papers_master.csv
├── assets/
│   ├── taxonomy_figures/
│   ├── mindmaps/
│   └── paper_figures/
├── drafts/
│   ├── sections/
│   └── full_draft/
└── notes/
    ├── paper_notes/
    ├── experiment_notes/
    └── reading_logs/
```

---

## 2. 文件命名规范

### 2.1 主文档命名

主文档采用两位数字前缀，保证排序稳定：

| 前缀 | 含义 | 示例 |
|---|---|---|
| `00_` | 项目说明、目录规范 | `00_README_目录规范.md` |
| `01_` | 论文库、分类表 | `01_paper_taxonomy_论文分类库.md` |
| `02_` | 总体思路、核心论点 | `02_overall_idea_总体思路.md` |
| `03_` | 大纲、章节写法 | `03_survey_outline_综述写作大纲.md` |
| `04_` | 检索协议、更新流程 | `04_literature_search_protocol_检索与更新协议.md` |
| `05_` 以后 | 章节草稿、实验设计、评测方案 | `05_evaluation_design.md` |

### 2.2 单篇论文笔记命名

建议放在 `notes/paper_notes/`：

```text
YYYY_firstauthor_shorttitle_category.md
```

示例：

```text
2026_wu_echo_forcing_kv_scene_memory.md
2026_kim_memrope_positional_memory.md
2026_liu_iamflow_entity_memory.md
2026_wang_mirage_latent_spatial_memory.md
```

---

## 3. 文献库字段规范

主表位于：

```text
tables/papers_master.csv
```

字段说明：

| 字段 | 说明 |
|---|---|
| `cat` | 论文分类。建议以 S0-S8 编号。 |
| `paper` | 论文题目或系统名称。 |
| `year` | 年份。预印本可写 arXiv 年份。 |
| `id` | arXiv ID、会议或项目页。 |
| `memory_object` | 记忆对象：identity、scene、motion、entity、spatial、world-state 等。 |
| `substrate` | 记忆载体：KV cache、frame、latent patch、entity table、3D cache、SSM state 等。 |
| `tf` | 是否 training-free。可写 Yes / No / Trained / System / Mixed / N/A。 |
| `priority` | Must-read / High / Related / Background / To-check。 |
| `role` | 在综述中的使用方式。 |
| `url` | 论文或项目链接。 |
| `status` | Verified by web / From prior docs / To verify。 |

---

## 4. 分类编号规范

| 编号 | 类别 | 用途 |
|---|---|---|
| S0 | Existing surveys / 相邻综述 | 说明本文与已有综述的差异。 |
| S1 | AR / streaming video generation backbones | 说明 memory 问题如何在 AR/streaming 范式下显性化。 |
| S2 | KV cache / attention memory | 本文第一主线：隐式 token memory。 |
| S3 | Positional / RoPE memory | 时间坐标和位置相位也是记忆系统的一部分。 |
| S4 | Frequency / spectrum memory | 低频保结构，高频保细节和动态。 |
| S5 | Identity / entity / narrative memory | 本文第二主线：从参考身份到显式实体状态。 |
| S6 | Retrieval / external memory | 历史帧、latent patch、entity slot、scene cache 等外部检索记忆。 |
| S7 | Video world model memory | 本文第三主线：spatial memory、world-state memory、out-of-sight dynamics。 |
| S8 | Evaluation / benchmarks | 记忆能力如何评测。 |

---

## 5. 版本更新规则

建议采用如下更新记录：

```markdown
## Changelog

### v0.1 - 2026-06-17
- 建立目录规范。
- 建立第一版论文分类库。
- 建立总体思路和写作大纲。
- 标注“截至 2026-06-17”，等待 2026-07 后二次检索。
```

---

## 6. 这套资料包的使用方式

1. 先读 `02_overall_idea_总体思路.md`，确定综述的中心论点和章节主线。
2. 再读 `01_paper_taxonomy_论文分类库.md`，按类别补全文献。
3. 写作时参考 `03_survey_outline_综述写作大纲.md`，不要从论文列表直接堆正文。
4. 每次新增论文，先写入 `tables/papers_master.csv`，再同步到 `01_paper_taxonomy_论文分类库.md`。
5. 2026-07-31 后按 `04_literature_search_protocol_检索与更新协议.md` 做一次系统更新。
