# 03 综述写作大纲

> 目标：把 `02_overall_idea_总体思路.md` 中的研究主线落实为可写作的章节结构。  
> 建议：先写英文 title/abstract/outline，再写中文详细笔记，最后转英文正式稿。

---

## Title candidates

1. **Memory Systems in Video Generation and Video World Models: From KV Cache to Entity and World-State Memory**
2. **From Context to Memory: A Survey of Long-Form Video Generation and Video World Models**
3. **What Should Video Models Remember? A Survey on Memory Mechanisms in Video Generation and World Models**
4. **Structured Memory for Long Video Generation: Identity, Scene, Entity, and World-State Persistence**

推荐第 1 个，信息最完整，也最像正式综述题目。

---

## Abstract 草稿骨架

> Long-form video generation and video world modeling require models to preserve identities, scenes, motions, spatial layouts, and hidden world states over extended horizons. Existing surveys mainly organize the field around model architectures, controllability, diffusion frameworks, or spatiotemporal consistency, leaving the memory mechanisms behind long-horizon generation underexplored. This survey presents a memory-centric view of video generation and video world models. We categorize existing methods by what they remember, where the memory is stored, and how memory is written, retrieved, updated, forgotten, and evaluated. We review implicit token memory in KV caches and attention sinks, positional and spectral memory, identity and entity-centric memory, retrieval-augmented memory, and spatial/world-state memory in interactive video world models. Finally, we discuss evaluation protocols and open challenges, including active identity recall, entity-state memory, memory-aware forgetting, and metrics beyond superficial temporal consistency.

---

## 1. Introduction

### 1.1 开场问题

- 短视频生成已经能生成高质量 5-16 秒 clip。
- 但长视频、叙事视频、可交互视频、world model 场景下，模型经常“忘记”。
- 遗忘不是单一现象：identity drift、scene forgetting、motion loop、RoPE conflict、entity duplication、out-of-sight freezing。

### 1.2 现有综述缺口

已有综述覆盖：

- video diffusion models；
- long video generation；
- spatiotemporal consistency；
- controllable video generation；
- long-video storytelling；
- efficient video world models；
- robotic world models。

但缺少 memory-centric survey。

### 1.3 本文贡献

- 提出 memory object / memory substrate / memory lifecycle 三层分类。
- 统一视频生成与视频世界模型中的 memory 机制。
- 系统梳理 KV cache、RoPE、frequency、entity、retrieval、3D/SSM/world-state memory。
- 总结 memory evaluation 与 future directions。

---

## 2. Preliminaries

### 2.1 Video generation foundations

- Diffusion video models。
- DiT / latent diffusion。
- T2V / I2V / V2V。
- Long video generation 的 basic paradigms。

### 2.2 Autoregressive and streaming generation

- 为什么 AR/streaming 让 memory 问题显性化。
- KV cache、causal attention、rolling window、attention sink。
- 代表：Diffusion Forcing、CausVid、Self Forcing、Rolling Forcing、LongLive、FramePack。

### 2.3 Video world models

- video generation as world simulation。
- action-conditioned rollout。
- state construction and dynamics modeling。
- object permanence 和 world-state persistence。

---

## 3. What Should Video Models Remember?

这一章是全篇最重要的概念章。

### 3.1 Identity Memory

- 同一个角色的脸、衣服、体型、风格、配饰。
- 失败：ID drift、character swap、duplication。
- 代表：StoryDiffusion、Video Storyboarding、ConsisID、TPIGE、IAMFlow、Memento。

### 3.2 Scene and Layout Memory

- 背景、场景布局、物体位置、视觉风格。
- 失败：旧场景回看不一致、背景污染。
- 代表：Echo-Forcing、Context as Memory、MAG、WorldMem。

### 3.3 Motion and Event Memory

- 最近动作、速度、动态趋势、事件进展。
- 失败：motion stagnation、frozen video、loop。
- 代表：Deep Forcing、LVSA、FreeSpec、FLEX、Rolling Forcing。

### 3.4 Positional Memory

- 历史 token 的时间坐标和 RoPE 相位。
- 失败：phase conflict、position jump。
- 代表：MemRoPE、Pyramid Forcing、FLEX、Infinity-RoPE。

### 3.5 Entity and Narrative Memory

- 多 prompt 中角色/道具/背景的全局 ID、属性和状态。
- 失败：attribute loss、entity duplication、prompt transition failure。
- 代表：IAMFlow、VideoMemory、SlotMemory、EM-Vid、StoryMem。

### 3.6 Spatial and World-State Memory

- 3D layout、camera pose、不可见物体的持续状态。
- 失败：revisit inconsistency、out-of-sight freezing。
- 代表：WorldMem、SpMem、RELIC、LiveWorld、Mirage、ReMind。

### 3.7 Unified lifecycle

Write → Store → Retrieve → Use → Update → Forget → Evaluate。

---

## 4. Implicit Token Memory: KV Cache, Attention Sink, and Sparse Retrieval

### 4.1 From sliding window to structured KV memory

- Sliding window 的问题：丢历史、ID drift、scene forgetting。
- Static sink 的问题：global anchor but motion stagnation。

### 4.2 Echo-Forcing

重点讲：

- Hierarchical Temporal Memory；
- Scene Recall Frames；
- Difference-aware Memory Decay；
- 它偏 scene memory，不专门解决 entity identity。

### 4.3 MemRoPE

重点讲：

- dual EMA memory tokens；
- unrotated key cache；
- online RoPE indexing；
- 为什么位置相位解耦是 memory compression 的前提。

### 4.4 Deep Forcing

重点讲：

- deep sink；
- participative compression；
- sink 太强会 motion stagnation。

### 4.5 Pyramid Forcing

重点讲：

- Anchor / Wave / Veil heads；
- per-head cache policy；
- 从 temporal head role 引出 identity/motion/layout-aware head role。

### 4.6 LVSA, Future Forcing, OmniMem, DecMem

- LVSA：sparse attention + rotating global anchors + VQeval。
- Future Forcing：future-aware token retention。
- OmniMem：full-range sparse KV retrieval。
- DecMem：global-local memory 解耦。

---

## 5. Positional and Spectral Memory

### 5.1 Why content memory needs coordinates

历史 token 如果有错误时间坐标，会被错误召回。

### 5.2 RoPE phase conflict

- MemRoPE 的 unrotated key。
- Pyramid Forcing 的 dynamic RoPE remap。
- Infinity-RoPE 的 Block-Relativistic RoPE / KV Flush / RoPE Cut。

### 5.3 Frequency and spectrum

- FreeLong++：multi-band spectral fusion。
- FreeSpec：singular-spectrum reconstruction。
- FLEX：frequency-aware RoPE + antiphase noise。
- ConsisID：低频全局身份 + 高频身份细节。

### 5.4 小结

记忆不是只保留 token，还要保留它在时间坐标和频谱结构中的正确解释。

---

## 6. Identity, Entity, and Narrative Memory

### 6.1 Reference-based identity memory

- TPIGE。
- ConsisID。
- Gloria。

### 6.2 Multi-shot consistency

- StoryDiffusion。
- Video Storyboarding。
- Corgi。
- StoryMem。

### 6.3 Explicit entity memory

- IAMFlow：LLM global ID + VLM verification。
- VideoMemory：dynamic memory bank。
- SlotMemory：object-centric KV semantic slots。
- EM-Vid：entity-indexed sparse latent patch bank。
- Memento：subject reconstruction-guided memory。

### 6.4 关键结论

从“第 t 帧的历史 token”转向“实体 A 的可持续状态”是 2026 年最重要的趋势之一。

---

## 7. Retrieval-Augmented Memory

### 7.1 Why retrieval is different in video

Text RAG 的单位是 passage；video RAG 的单位可能是 frame、shot、patch、latent token、KV block、entity slot、camera pose、3D point。

### 7.2 Historical frame retrieval

- Context as Memory。
- MemCam。
- LongLive-RAG。

### 7.3 Latent / entity retrieval

- Memory-V2V。
- MALT Diffusion。
- MAG。
- SlotMemory。
- EM-Vid。

### 7.4 Challenges

- 检索到错误历史会污染新 prompt。
- full-frame memory 会把 transient context 和 persistent identity 混在一起。
- retrieval 必须和 forgetting/update 绑定。

---

## 8. Spatial and World-State Memory in Video World Models

### 8.1 From visual continuity to object permanence

普通视频生成关注“看起来连续”；world model 关注“世界持续存在”。

### 8.2 Spatial memory

- WorldMem。
- SpMem。
- WorldPack。
- RELIC。
- Mirage。
- MosaicMem。
- Beyond Pixel Histories。

### 8.3 Hidden state and out-of-sight dynamics

- LiveWorld。
- ReMind。
- Echo-Memory。

### 8.4 Recurrent / state-space memory

- Long-Context State-Space Video World Models。
- VideoSSM / RAD-like routes。

### 8.5 Interactive and embodied settings

- Genie 2/3。
- Learning World Models for Interactive Video Generation。
- WorldPlay。
- DriveWAM / autonomous driving world models。

---

## 9. Evaluation of Memory

### 9.1 Why ordinary metrics are insufficient

- CLIP/frame consistency 可能奖励静止。
- subject consistency 可能忽略 motion diversity。
- VBench-Long 需要搭配 anti-loop / dynamic degree。

### 9.2 Evaluation categories

| 能力 | 评测方式 |
|---|---|
| Identity consistency | ArcFace、DINO/CLIP subject similarity、human eval |
| Dynamic quality | Dynamic Degree、optical flow、anti-loop score、VQeval |
| Scene revisit | revisit consistency、layout similarity、camera-aware retrieval score |
| Entity consistency | global ID accuracy、attribute accuracy、NarraStream-style score |
| Spatial memory | pose-aware reconstruction、3D consistency、WorldScore |
| World-state memory | MIND、out-of-sight dynamics tests、closed-loop revisiting |
| Action control | action-conditioned success rate、trajectory following |

### 9.3 Recommended evaluation protocol

至少包含四类 prompt：

1. Single-subject long rollout。
2. Multi-shot same character。
3. Multi-entity narrative。
4. Scene/object revisit with long gap。
5. Interactive/world-model closed-loop revisit。

---

## 10. Open Problems and Future Directions

### 10.1 Passive retention → active recall

不是留下更多历史，而是主动召回相关身份证据、场景证据或实体状态。

### 10.2 Temporal-centric memory → entity-centric memory

记忆单位应从 frame/chunk/token 转向 entity/slot/state。

### 10.3 Uniform cache → head/layer-specialized memory

不同 head/layer 可能承担 identity、motion、layout、style 等不同功能。

### 10.4 Position and memory co-design

记忆压缩必须和位置编码共同设计，否则压缩后的历史 token 会带有错误相位。

### 10.5 Memory-aware forgetting

遗忘不是失败，而是功能。prompt 切换、场景变化、角色属性更新时，必须有冲突感知遗忘。

### 10.6 Unified entity-state memory

未来视频生成和 world model 应统一：实体外观、位置、属性、动作、不可见状态演化。

### 10.7 Better benchmarks

需要惩罚 loop/frozen video，并测试 scene revisit、entity reappearance、out-of-sight dynamics。

---

## 11. Conclusion

结尾可以回到主论点：

> The future of long-form video generation depends not only on scaling models or extending context windows, but on building structured memory systems that can preserve, retrieve, update, and forget identities, scenes, events, and world states.
