# 02 总体思路：如何写“视频生成与视频世界模型中的记忆系统综述”

> 工作题目：**Memory Systems in Video Generation and Video World Models: From KV Cache to Entity and World-State Memory**  
> 中文题目：**视频生成与视频世界模型中的记忆系统综述：从 KV Cache 到实体记忆与世界状态记忆**  
> 当前版本：v0.1  
> 时间边界：截至 2026-06-17；2026-07 后需要二次更新。

---

## 1. 这篇综述应该解决什么问题

不要把这篇综述写成“长视频生成论文合集”。更有价值的写法是：

> 长视频生成的问题不只是上下文窗口不够长，而是模型缺少结构化记忆系统。

换句话说，已有很多工作在问：

- 如何生成更长的视频？
- 如何提升时空一致性？
- 如何控制主体、姿态、相机和布局？
- 如何把视频生成模型变成 world model？

但我们要问的是：

- 视频模型到底应该记住什么？
- 这些记忆存在哪里？
- 它们如何被写入、压缩、检索、召回、更新和遗忘？
- identity memory、scene memory、motion memory、spatial memory、world-state memory 之间是什么关系？
- 如何证明模型真的“记住了”，而不是靠静止、循环、低动态来骗过一致性指标？

这就是本文与普通 video generation survey 的区别。

---

## 2. 推荐主论点

### 2.1 一句话主论点

> Long video generation is not merely a problem of longer context; it is a problem of structured memory.

中文表达：

> 长视频生成不是简单的长上下文问题，而是结构化记忆问题。

### 2.2 扩展论点

当前视频生成正在经历三个阶段：

1. **Short Clip Generation**：模型只需要生成几秒钟视频，记忆问题被短时一致性掩盖。
2. **Long / Streaming Video Generation**：模型需要在 AR rollout 中保留历史，KV cache、sink、RoPE、frequency degeneration 等问题显性化。
3. **Video World Models**：模型需要模拟一个持续存在的世界，记忆不再只是视觉一致性，而是 object permanence、spatial persistence、hidden-state evolution 和 action-conditioned transition。

因此，记忆系统是连接长视频生成、叙事视频、多角色一致性、交互世界模型的共同机制。

---

## 3. 综述的核心贡献设计

建议在 Introduction 中写成 3-4 个贡献点：

### Contribution 1: Memory-centric taxonomy

本文提出以 memory object、memory substrate 和 memory lifecycle 为核心的分类体系，而不是按 T2V/I2V/V2V 或架构名称堆论文。

### Contribution 2: Unified view from video generation to video world models

本文统一讨论视频生成中的 identity/scene/motion memory 与世界模型中的 spatial/world-state memory，指出二者不是两个孤立问题，而是记忆能力从视觉连续性到世界持续性的升级。

### Contribution 3: Lifecycle analysis

本文用 Write–Store–Retrieve–Use–Update–Forget–Evaluate 框架分析不同方法，强调“如何遗忘”和“如何评测”与“如何记住”同等重要。

### Contribution 4: Open problems and future directions

本文总结从 passive retention 到 active recall、从 temporal-centric memory 到 entity-centric memory、从 frame/KV memory 到 latent 3D/world-state memory 的未来趋势。

---

## 4. 三层分类框架

### 4.1 第一层：按“记什么”分类 Memory Object

| 类别 | 记忆内容 | 典型失败 | 代表方向 |
|---|---|---|---|
| Identity Memory | 人脸、服装、主体属性、角色身份 | identity drift、角色互换、身份复制 | StoryDiffusion、Video Storyboarding、ConsisID、TPIGE、IAMFlow、Memento |
| Scene Memory | 背景、场景外观、旧场景 recall | scene forgetting、background contamination | Echo-Forcing、Context as Memory、MAG、WorldMem |
| Motion Memory | 动作趋势、速度、短期动态 | motion stagnation、frozen video、loop | Deep Forcing、LVSA、FreeSpec、FLEX、Rolling Forcing |
| Positional Memory | 长程时间坐标、相对位置、RoPE 相位 | phase conflict、position jump、temporal misalignment | MemRoPE、Pyramid Forcing、FLEX、Infinity-RoPE |
| Entity Memory | 全局实体 ID、属性表、角色/道具状态 | duplication、attribute loss、prompt transition failure | IAMFlow、SlotMemory、EM-Vid、VideoMemory、Memento |
| Spatial Memory | 3D layout、camera pose、重访区域 | revisit inconsistency、geometry drift | WorldMem、SpMem、WorldPack、RELIC、Mirage |
| World-State Memory | 视野外实体状态、时间演化、因果状态 | out-of-sight freezing、hidden event failure | LiveWorld、ReMind、MIND、Echo-Memory |
| System Memory | cache budget、quantization、sparse retrieval | 显存爆炸、延迟过高、质量下降 | Quant VideoGen、OmniMem、FramePack、DecMem |

### 4.2 第二层：按“存在哪里”分类 Memory Substrate

| 载体 | 形式 | 代表论文 |
|---|---|---|
| Raw Frame Memory | 历史帧、关键帧、context frame | Context as Memory、Corgi |
| KV Cache Memory | sink token、rolling KV、compressed KV | Rolling Forcing、LongLive、Echo-Forcing、Deep Forcing |
| Compressed Token Memory | EMA token、packed context、memory token | MemRoPE、FramePack、MAG |
| Sparse Retrieval Memory | selected KV blocks、future-useful tokens | Future Forcing、OmniMem、LVSA |
| Head-specific Memory | per-head cache policy、head role | Pyramid Forcing、SlotMemory、HRMR-like future work |
| Positional Memory | unrotated key、RoPE remap、relativistic RoPE | MemRoPE、FLEX、Infinity-RoPE |
| Spectral Memory | low/high-frequency branch、singular spectrum | FreeLong++、FreeSpec、ConsisID |
| Entity Memory | global ID table、attribute table、entity slots | IAMFlow、VideoMemory、SlotMemory、EM-Vid |
| 3D / Spatial Memory | memory frames + pose、3D bank、latent 3D cache | WorldMem、SpMem、Mirage、MosaicMem |
| Recurrent / SSM Memory | hidden state、state-space scan | Long-Context SSM Video World Models、VideoSSM/RAD-like routes |

### 4.3 第三层：按“生命周期”分类 Memory Lifecycle

这是最适合作为全文主轴的分类。

| 阶段 | 核心问题 | 代表机制 |
|---|---|---|
| Write | 什么信息被写入 memory？ | frame、KV、latent patch、entity attribute、pose/state、3D point |
| Store | 以什么结构保存？ | sliding window、sink、EMA token、entity table、memory bank、SSM state |
| Retrieve | 什么时候召回？根据什么召回？ | attention score、future query proxy、semantic slot、camera overlap、global ID |
| Use | 召回后如何影响生成？ | cross-attention、KV injection、query injection、guidance、prompt rewriting、conditioning |
| Update | 新生成内容如何更新 memory？ | EMA、VLM verification、memory write-back、budgeted update、state transition |
| Forget | 何时遗忘或衰减？ | FIFO eviction、difference-aware decay、KV flush、conflict-aware forgetting |
| Evaluate | 怎么证明真的记住了？ | subject consistency、scene revisit、MIND、VQeval、out-of-sight dynamics |

---

## 5. 文章叙事路线

### 5.1 从 failure 开场

开头不要先讲模型结构，而要先讲“为什么会忘”：

- Identity drift：同一个角色脸、衣服、体型逐渐变。
- Subject duplication：同一角色复制出多个版本。
- Scene forgetting：离开旧场景再回来时背景和布局变化。
- Motion stagnation：长视频变成近似静止或循环。
- RoPE phase conflict：长程外推中位置相位错乱。
- Entity attribute loss：多 prompt 中角色属性丢失。
- Out-of-sight freezing：世界模型中不可见物体被冻结。

然后指出：这些 failure 表面上叫 temporal inconsistency，但机制上都是 memory failure。

### 5.2 再讲为什么 2025-2026 年 memory 突然爆发

因为视频生成进入 AR / streaming 范式后，历史不再只是“训练时的隐式分布”，而是推理时必须维护的显式状态：

- KV cache 怎么保留？
- sink token 是否会导致 motion stagnation？
- 历史 key 的 RoPE 相位如何处理？
- 哪些历史帧是 identity anchor，哪些是 motion context？
- prompt 切换时旧 memory 应该保留还是遗忘？

这就是 Echo-Forcing、MemRoPE、Deep Forcing、Pyramid Forcing、LVSA、Future Forcing、IAMFlow、SlotMemory、EM-Vid 等工作密集出现的原因。

### 5.3 最后升到 world model

普通视频生成的 memory 目标是：视觉别漂。

世界模型的 memory 目标是：世界真的持续存在。

这包括：

- object permanence；
- spatial consistency；
- action-conditioned transition；
- hidden-state evolution；
- out-of-sight dynamics；
- scene revisit consistency。

因此，将视频生成和视频世界模型放在同一篇 memory survey 中是合理的：前者是视觉记忆，后者是世界状态记忆。

---

## 6. 建议章节结构

1. Introduction
2. Preliminaries: Video Generation, AR Rollout and World Models
3. What Should Video Models Remember?
4. Implicit Token Memory: KV Cache, Sink and Sparse Retrieval
5. Positional and Spectral Memory
6. Identity, Entity and Narrative Memory
7. Spatial and World-State Memory in Video World Models
8. Evaluation of Memory
9. Open Problems and Future Directions
10. Conclusion

---

## 7. 重点图表规划

### Figure 1: Failure taxonomy

展示 identity drift、scene forgetting、motion loop、RoPE conflict、entity duplication、out-of-sight freezing。

### Figure 2: Memory lifecycle

Write → Store → Retrieve → Use → Update → Forget → Evaluate。

### Figure 3: Memory substrate map

Frame / KV / Token / RoPE / Spectrum / Entity / 3D / SSM。

### Figure 4: 从 video generation 到 video world model

Visual continuity → narrative continuity → spatial persistence → world-state evolution。

### Table 1: Existing surveys vs our survey

说明已有综述覆盖视频扩散、长视频、时空一致性、可控生成、storytelling、world model efficiency；本文覆盖 memory objects/substrates/lifecycle。

### Table 2: Paper taxonomy table

对应 `01_paper_taxonomy_论文分类库.md` 和 `tables/papers_master.csv`。

### Table 3: Evaluation metrics and failure traps

重点指出普通 consistency 指标可能奖励 frozen/loop video。

---

## 8. 未来方向：如何放入我们自己的 idea

我们自己的 AAI、HRMR、DARV 等 idea 建议不要放在前面文献综述主线中重点讲，而是放在 Future Directions 里作为可能方向。

可以写成如下几类：

### 8.1 Active Identity Recall

现有工作多关注哪些历史 token 该留下，下一步应关注当前 query 如何主动召回身份相关证据。

### 8.2 Identity-aware Head Routing

Pyramid Forcing 已经说明不同 head 有不同时间角色，但身份头、运动头、布局头能否分别维护不同 memory，还没有被充分系统化。

### 8.3 Cross-layer Identity Residual

如果身份证据只在单层注入，容易衰减或被 motion/context 覆盖。跨层 identity residual 可能稳定传递主体证据，但需要控制 ghosting。

### 8.4 Dual-track Per-head RoPE

身份头可以锚定较稳定的位置坐标，运动头使用滑动位置坐标，混合头折中。这与 uniform RoPE remap 不同，是可能的未来方向。

### 8.5 Unified Entity-State Memory

将 video identity memory 与 world model state memory 连接起来：同一个实体不仅要外观一致，还要具有位置、属性、行为和不可见状态演化。

---

## 9. 写作警告

1. 不要把这篇写成普通“长视频生成综述”。核心词应是 memory，而不是 long video。
2. 不要只讲 identity preservation。ID 保持只是 memory 的一个子问题。
3. 不要忽略 world model。世界模型能把综述拔高到 object permanence 和 hidden-state evolution。
4. 不要只讲“如何记”，也要讲“如何忘”。遗忘是 memory system 的必要功能。
5. 不要只看一致性指标。稳定但不动的视频不是好视频。
6. 不要把我们的 idea 过早作为主角。综述主线应先客观，再在 future directions 中提可推进方向。

---

## 10. 最终想表达的中心句

> Existing works increasingly reveal that the bottleneck of long-form video generation is not merely the lack of longer context, but the lack of structured memory: memory for identities, scenes, motions, temporal coordinates, entities, spatial layouts, and persistent world states.

中文：

> 现有工作逐渐表明，长视频生成的瓶颈不只是上下文长度不够，而是缺少结构化记忆：对身份、场景、运动、时间坐标、实体、空间布局和持续世界状态的记忆。
