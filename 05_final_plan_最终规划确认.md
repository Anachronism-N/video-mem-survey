# 05 最终规划确认：Video Memory Survey 写作方案 v0.2

> 当前锁定版本：v0.2，2026-06-17  
> 重要边界：当前日期尚未到 2026-07。本文献库不能诚实地声称“截至 2026 年 7 月无遗漏”；它只能作为截至 2026-06-17 的当前可检索版本。2026-07-31 后应执行最终复检。

## 1. 最终定位

推荐题目：

**Memory Systems in Video Generation and Video World Models: From KV Cache to Entity and World-State Memory**

核心论点：

> Long video generation is not merely a problem of longer context; it is a problem of structured memory.

中文表达：

> 长视频生成不是简单的长上下文问题，而是结构化记忆问题。

本文应与普通 video generation survey、long video survey、consistency survey、world model survey 拉开差异：它不按 T2V/I2V/V2V 或模型架构堆论文，而是按“记什么、存在哪里、如何写入、如何检索、如何更新、如何遗忘、如何评测”组织。

## 2. 最终三层 taxonomy

### 2.1 Memory Object：记什么

1. Identity Memory：角色/主体身份、面部、服装、属性。
2. Scene Memory：场景、背景、布局和旧场景召回。
3. Motion Memory：动作趋势、速度、动态程度和避免 loop/frozen。
4. Positional Memory：时间坐标、RoPE 相位、长程位置外推。
5. Entity/Narrative Memory：全局实体 ID、属性表、叙事状态。
6. Spatial Memory：3D layout、camera pose、重访区域。
7. World-State Memory：不可见实体状态、隐藏事件、out-of-sight dynamics。
8. System Memory：KV budget、量化、稀疏检索、显存/速度。

### 2.2 Memory Substrate：存在哪里

Frame / keyframe / KV cache / sink token / compressed token / sparse retrieval block / RoPE coordinate / spectrum / entity table / latent patch bank / 3D cache / SSM state。

### 2.3 Memory Lifecycle：如何工作

Write → Store → Retrieve → Use → Update → Forget → Evaluate。

这应成为全文最核心图。

## 3. 最终章节结构

1. Introduction
2. Preliminaries: Video Generation, AR Rollout and Video World Models
3. What Should Video Models Remember?
4. Implicit Token Memory: KV Cache, Sink and Sparse Retrieval
5. Positional and Spectral Memory
6. Identity, Entity and Narrative Memory
7. Retrieval-Augmented Memory
8. Spatial and World-State Memory in Video World Models
9. Evaluation of Memory
10. Open Problems and Future Directions
11. Conclusion

## 4. 最终精读优先级

### Tier 1：正文必须精讲

Echo-Forcing、MemRoPE、Deep Forcing、Pyramid-Forcing、LVSA、Future Forcing、OmniMem、LongLive-RAG、IAMFlow、SlotMemory、EM-Vid、Memento、Video Storyboarding、ConsisID、WorldMem、SpMem、RELIC、LiveWorld、Mirage、MIND。

### Tier 2：分类表必须覆盖

Self Forcing、Rolling Forcing、LongLive、FramePack、FreeLong++、FreeSpec、FLEX、TPIGE、Gloria、VideoMemory、StoryMem、Memory-V2V、MAG、SWIFT、DecMem、WorldPack、ReMind、MosaicMem、CoTriSyGen、KV Cache Quantization for Self-Forcing Video Generation。

### Tier 3：背景引用

Video diffusion surveys、long video generation surveys、controllable video generation surveys、world model surveys、Genie 2/3、Sora technical report page、robotic world model surveys。

## 5. 最终图表规划

- Figure 1: Memory failure taxonomy。
- Figure 2: Memory lifecycle。
- Figure 3: Memory substrate map。
- Figure 4: From visual continuity to world-state persistence。
- Table 1: Existing surveys vs this survey。
- Table 2: Core paper taxonomy。
- Table 3: Memory lifecycle by representative method。
- Table 4: Evaluation protocols and failure traps。

## 6. 未来方向最终版

1. Passive retention -> active recall。
2. Temporal memory -> entity-centric memory。
3. Uniform cache -> head/layer-specialized memory。
4. Content memory -> content + coordinate + spectrum co-design。
5. Static memory -> updateable and forgettable memory。
6. Visual consistency -> world-state persistence。
7. Single score evaluation -> diagnostic memory benchmark。

我们的 AAI / HRMR / DARV 相关想法建议只放在 Future Directions，表述为“可能推进方向”，不要在综述主体抢文献客观性。
