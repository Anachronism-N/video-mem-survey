# 01 论文分类库：Memory Systems in Video Generation and Video World Models

> 当前版本：v0.1  
> 时间边界：截至 2026-06-17；2026-07 后需要二次检索锁版。  
> 用途：记录与视频生成、长视频生成、视频世界模型、身份保持、实体记忆、空间记忆和世界状态记忆相关的论文，并按综述 taxonomy 分类。

---

## 分类总览

本文献库采用如下分类编号：

| 编号 | 类别 | 说明 |
|---|---|---|
| S0 | Existing surveys / 相邻综述 | 用于说明本文与已有综述的差异。 |
| S1 | AR / streaming video generation backbones | 解释 memory 问题如何在 AR/streaming 范式下显性化。 |
| S2 | KV cache / attention memory | 隐式 token memory，本文第一主线。 |
| S3 | Positional / RoPE memory | 时间坐标、RoPE 相位与记忆压缩。 |
| S4 | Frequency / spectrum memory | 低频结构、高频细节和动态记忆。 |
| S5 | Identity / entity / narrative memory | 从参考身份到显式实体状态，本文第二主线。 |
| S6 | Retrieval / external memory | frame、shot、latent patch、entity slot、KV block 等外部检索记忆。 |
| S7 | Video world model memory | spatial memory、world-state memory、out-of-sight dynamics，本文第三主线。 |
| S8 | Evaluation / benchmarks | 记忆一致性、身份一致性、重访一致性、世界模型评测。 |

---

## S0. Existing surveys / 相邻综述

这些综述可用于 Introduction 的 related survey 对比，强调本文不是普通视频生成综述，而是 memory-centric survey。

| 论文 / 主题 | 角色 | 与本文关系 |
|---|---|---|
| Survey of Video Diffusion Models | Background | 讲 diffusion video model 总体架构，memory 不是主线。 |
| Video Diffusion Models: A Survey | Background | 可引用其架构和任务背景。 |
| Spatiotemporal Consistency in Video Generation Survey | Related | 与 memory 强相关，但以 consistency 现象分类，而不是 memory lifecycle 分类。 |
| Controllable Video Generation Survey | Related | reference/control signal 对 identity memory 有帮助。 |
| Long-Video Storytelling Generation Survey | Related | 和 narrative/entity memory 接近，但中心是 storytelling。 |
| Video Generation Models as World Models | Related | world model 背景。 |
| Simulating the Visual World with Artificial Intelligence | Related | 讨论 video/world simulation，可支撑 world-state memory 章节。 |
| Video Generation Models in Robotics | Background | embodied world model 应用背景。 |
| Efficient World Models Survey | Background | 关注效率、planning、control，不专门讨论 memory object/substrate。 |
| Long Video Generation Survey | Related | 解释长视频生成脉络，但不以 memory system 组织。 |

---

## S1. AR / streaming video generation backbones

这一类论文使 memory 问题显性化。它们不一定都以 memory 为题，但 KV cache、rolling window、attention sink、frame-level AR 等机制让“历史如何保存和更新”成为核心问题。

| 论文 / 系统 | 年份 | 记忆相关性 | 优先级 |
|---|---:|---|---|
| Diffusion Forcing | 2024 | forcing 家族源头，逐 token 噪声建模，为后续 AR video diffusion 铺路。 | Background |
| CausVid | 2024/2025 | 双向到因果蒸馏、block-causal + KV cache。 | High |
| Self Forcing | 2025 | self-generated rollout + KV cache，缓解 train-test gap。 | Must-read |
| Self-Forcing++ | 2025/2026 | 自生成 segment guidance、rolling KV、GRPO 等。 | High |
| Rolling Forcing | 2025/2026 | rolling-window joint denoising + frame-0 attention sink。 | Must-read |
| Causal-Forcing | 2026 | block-causal / chunk-wise AR video generation。 | High |
| LongLive | 2025/2026 | frame-level causal AR、frame sink、KV rolling、prompt switching。 | Must-read |
| LongLive-2.0 | 2026 | 长视频生成系统化加速与 infrastructure。 | Related |
| FramePack | 2025 | 将历史帧上下文压缩到固定长度 context。 | High |
| StreamDiT | 2024/2025 | streaming diffusion transformer。 | Related |
| StreamingT2V | 2024/2025 | 流式 T2V 生成。 | Related |
| SkyReels-V2 | 2025 | 长视频生成系统，可作为应用背景。 | Related |
| MAGI-1 | 2025 | chunk AR / long video generation baseline。 | Related |
| Pyramid Flow | 2024/2025 | flow-based 长视频/多尺度生成背景。 | Background |
| LongVie / LongVie 2 | 2025/2026 | ultra-long controllable video / world model，history-context guidance。 | High |
| Infinity-RoPE | 2025/2026 | infinite action-controllable rollout，RoPE/KV flush 与场景切换。 | High |
| SANA-Video | 2025/2026 | linear attention / constant-memory KV cache。 | Related |

---

## S2. KV cache / attention memory

本文第一条主线。核心问题是：在固定 memory budget 下，哪些历史 token 应该保留、压缩、召回或遗忘。

| 论文 / 方法 | 年份 | Memory object | Memory substrate | 核心机制 | 优先级 |
|---|---:|---|---|---|---|
| Echo-Forcing | 2026 | scene / temporal | hierarchical KV memory | stable anchors、compressed history、recent windows、Scene Recall Frames、Difference-aware Decay。 | Must-read |
| MemRoPE | 2026 | temporal / positional | memory tokens + unrotated KV | long/short EMA memory tokens + online RoPE indexing。 | Must-read |
| Deep Forcing | 2025 | motion / temporal | deep sink + compressed KV | deep sink、RoPE phase realignment、participative compression。 | Must-read |
| Pyramid-Forcing | 2026 | temporal / head role | head-aware KV cache | Anchor/Wave/Veil heads + per-head cache policy。 | Must-read |
| LVSA | 2026 | scene / motion | sparse attention + rotating anchors | block sparse attention、structured window、rotating global anchors、VQeval。 | Must-read |
| Future Forcing | 2026 | future-useful context | future-aware KV cache | future query proxy，避免删掉未来重要 token。 | High |
| OmniMem | 2026 | full-range context | sparse KV retrieval | per-head scattered KV access。 | High |
| Quant VideoGen | 2026 | system memory | low-bit KV cache | 低比特 KV cache，缓解 memory budget。 | Related |
| Pack and Force Your Memory / MemoryPack | 2025 | context | packed retrieval memory | learnable context retrieval / packed memory。 | Related |
| MAG / Memorize-and-Generate | 2025 | scene / temporal | compression model + generation model | memory compression 与 next-frame generation 解耦。 | High |
| SWIFT | 2026 | semantic prompt context | semantic injection cache | Semantic Injection Cache + Adaptive Dynamic Window。 | High |
| DecMem | 2026 | global/local context | sparse global + anchored local memory | 解耦全局和局部 memory。 | High |
| StreamingLLM / Attention Sink | 2024 | token continuity | sink tokens | LLM sink 思想，被 video generation 借鉴。 | Background |
| H2O / SnapKV / Quest / PyramidKV | 2023-2025 | system memory | KV pruning/compression | LLM KV cache 压缩背景。 | Background |
| Sparse VideoGen | 2025 | attention role | sparse attention heads | online spatial/temporal head classification，启发 head-aware video memory。 | Related |

---

## S3. Positional / RoPE memory

记忆不仅是内容，还包括时间坐标。历史 token 如果带有错误 RoPE 相位，会在长视频中被错误解释。

| 论文 / 方法 | 年份 | 核心问题 | 机制 | 优先级 |
|---|---:|---|---|---|
| MemRoPE | 2026 | EMA key 混合旧 RoPE 相位不严格 | 缓存 unrotated keys，attention 时在线加 RoPE。 | Must-read |
| Pyramid-Forcing | 2026 | 长程外推超出训练位置分布 | dynamic RoPE remap 回训练区间。 | Must-read |
| FLEX | 2026 | 3D RoPE spectral bias + 动态先验不足 | Frequency-aware RoPE Modulation + Antiphase Noise Sampling。 | High |
| Infinity-RoPE | 2025/2026 | infinite rollout 与 action/prompt 切换 | Block-Relativistic RoPE、KV Flush、RoPE Cut。 | High |
| FreeLOC | 2026 | 相对位置重映射 / temporal sparse attention | VRPR + TSA。 | Related |
| LoL / RoPE jitter 类方法 | 2026 | sink 对齐崩塌或相位偏差 | per-head RoPE jitter 等。 | To-check |

---

## S4. Frequency / spectrum memory

频域方法强调：长视频中的身份、细节和运动退化不只是语义问题，也和频谱能量分布有关。

| 论文 | 年份 | Memory view | 核心机制 | 优先级 |
|---|---:|---|---|---|
| FreeLong | 2024/2025 | long-range temporal semantics | 长窗口/短窗口特征融合。 | Related |
| FreeLong++ | 2025 | low/high-frequency memory | Multi-band SpectralFusion。 | Must-read |
| FreeSpec | 2026 | dynamic/high-frequency memory | Singular-spectrum Reconstruction，避免 spectral concentration。 | High |
| FLEX | 2026 | spectral positional memory | frequency-aware RoPE + antiphase noise。 | High |
| ConsisID | 2024/2025 | identity frequency memory | 低频全局身份 + 高频身份细节。 | Must-read |

---

## S5. Identity / entity / narrative memory

本文第二条主线。核心问题从“第 t 帧的历史 token”升级为“实体 A 的可持续身份和状态”。

| 论文 / 系统 | 年份 | Memory object | Memory substrate | 核心机制 | 优先级 |
|---|---:|---|---|---|---|
| StoryDiffusion | 2024 | character identity | consistent self-attention | 跨图像/视频保持角色一致性。 | High |
| Video Storyboarding | 2024 | identity + motion | query injection / attention feature | 揭示 identity-motion trade-off。 | Must-read |
| ConsisID | 2024/2025 | face identity | frequency-decomposed ID feature | DiT-based tuning-free ID preserving T2V。 | Must-read |
| TPIGE | 2025 | identity | prompt/image/guidance enhancement | prompt、reference image、ID-aware spatiotemporal guidance。 | High |
| Gloria | 2026 | character identity | character-centric anchor frames | 多视角、长视频角色一致性。 | High |
| VideoMemory | 2026 | character/prop/background | dynamic memory bank | multi-shot narrative video memory。 | High |
| IAMFlow | 2026 | entity identity / attributes | global ID table + VLM verification | LLM 抽取实体，VLM 校验更新属性。 | Must-read |
| SlotMemory | 2026 | object/entity | object-centric KV slots | 把 history 从时间 token 组织为 object-centric memory。 | Must-read |
| EM-Vid | 2026 | entity | sparse latent patch bank | entity-indexed latent memory。 | Must-read |
| Memento | 2026 | recurring subject | reconstruction-guided historical memory bank | 用 subject reconstruction 监督 memory。 | Must-read |
| StoryMem | 2025 | characters/scenes/styles | compact memory bank | shot-by-shot story video generation。 | High |
| Corgi | 2025 | multi-scene consistency | cached latent memory bank | key frames as core memories。 | Related |
| Lynx | 2025 | identity | ID adapter / reference adapter | Wan2.1 身份保持 baseline。 | Related |
| Echo-Memory / JoyAI-Echo | 2026 | role identity / audiovisual memory | per-character memory slots | 多分钟角色一致性和音视记忆。 | To-check |
| LaVieID / ConsistI2V / FantasyID | 2024-2025 | identity | ID routing / reference attention | 身份保持相关 baseline。 | Related |

---

## S6. Retrieval / external memory

这类方法将历史帧、shot、latent patch、KV block 或 entity slot 作为可检索记忆库。

| 论文 / 方法 | 年份 | 记忆单位 | 核心机制 | 优先级 |
|---|---:|---|---|---|
| Context as Memory | 2025 | historical frames | FOV/camera overlap 或上下文检索。 | Must-read |
| MemCam | 2026 | compressed memory frames | camera/co-visibility-aware retrieval。 | High |
| Memory-V2V | 2026 | visual memory | multi-turn video editing consistency。 | High |
| MALT Diffusion | 2025/2026 | latent memory | memory-augmented latent transformer。 | Related |
| MAG | 2025 | compressed history | memory compression + generation 解耦。 | High |
| LongLive-RAG | 2026 | historical retrieval | 检索历史辅助 LongLive。 | To-check |
| Memorize-When-Needed / A2RD / MemFlow | 2025/2026 | adaptive retrieval memory | 按需激活历史或 agentic memory。 | To-check |

---

## S7. Video world model memory

本文第三条主线。普通视频生成的 memory 是视觉一致性；world model 的 memory 是世界持续存在。

| 论文 / 系统 | 年份 | Memory object | Memory substrate | 核心机制 | 优先级 |
|---|---:|---|---|---|---|
| Genie 2 | 2024 | world / scene | system-level world memory | 展示 long-horizon world memory 与视野外重现。 | Background |
| Genie 3 | 2025 | interactive world | system-level memory | 实时可交互世界模型。 | Background |
| WorldMem | 2025 | scene/spatial | memory frames + states | memory bank 存帧、pose、timestamp 等。 | Must-read |
| Video World Models with Long-term Spatial Memory / SpMem | 2025 | spatial / episodic | working + spatial + episodic memory | geometry-grounded long-term spatial memory。 | Must-read |
| WorldPack | 2025 | spatial | trajectory packing + memory retrieval | 压缩记忆提升 spatial consistency。 | High |
| RELIC | 2025 | spatial/action | latent tokens + actions + camera poses in KV | 实时交互、长程 streaming world model。 | Must-read |
| Long-Context State-Space Video World Models | 2025 | long-range spatial | SSM state + local attention | 用 SSM 解决 attention 长上下文成本。 | High |
| Learning World Models for Interactive Video Generation | 2025 | global state | VRAG + explicit state conditioning | 指出 AR world model 的 compounding error 与 insufficient memory。 | High |
| LiveWorld | 2026 | dynamic world-state | persistent global state | static 3D background + dynamic entities + out-of-sight dynamics。 | Must-read |
| ReMind | 2026 | out-of-sight state | dynamic memory/cache adaptation | event-aware training 激活动态记忆。 | High |
| Mirage / Latent Spatial Memory | 2026 | latent spatial memory | latent 3D cache | 在 diffusion latent space 存 3D memory。 | Must-read |
| MosaicMem / Hybrid Spatial Memory | 2026 | spatial memory | 3D patch lifting + native conditioning | controllable video world models。 | High |
| Beyond Pixel Histories | 2026 | 3D environment | persistent 3D memory | 强调 explicit 3D memory。 | High |
| Echo-Memory | 2026 | action world memory | benchmark/study | action world model memory 控制实验。 | High |
| WorldPlay | 2025 | interactive context | Reconstituted Context Memory | 动态重建过去上下文，缓解 memory attenuation。 | Related |
| MoVerse | 2026 | navigation world | spatial memory + Gaussian conditioning | 单图生成可交互导航世界。 | Related |
| DriveWAM / Driving world models | 2024-2026 | driving scene state | world model memory | 自动驾驶场景中的 world memory。 | Background |
| VideoSSM / RAD-like routes | 2025/2026 | recurrent temporal state | SSM/RNN memory | recurrent/state-space memory for long videos。 | Related |
| MIND-related world model systems | 2026 | action + memory | benchmark-driven memory | 与 memory consistency/action control 评测绑定。 | Related |

---

## S8. Evaluation / benchmarks

记忆评测不能只看 frame consistency，因为静止/循环视频可能骗过一致性指标。

| Benchmark / Metric | 能力 | 作用 | 优先级 |
|---|---|---|---|
| VBench / VBench-Long | subject consistency / dynamic degree 等 | 常用视频生成评测。 | Must-use |
| VQeval | loop/frozen 退化惩罚 | 避免一致性指标奖励静止循环。 | Must-read |
| NarraStream-Bench | multi-prompt narrative / identity | IAMFlow 提出的 narrative long video benchmark。 | High |
| MIND | memory consistency + action control | open-domain closed-loop revisited benchmark。 | Must-read |
| LiveBench / LoopNav / WorldScore | world model revisit / out-of-sight | 世界模型空间/状态记忆评测。 | High |
| Human evaluation protocols | identity、scene、motion、attribute | 最终仍需人工抽查，避免指标被骗。 | Must-use |

---

## 精读优先级

### Must-read

Echo-Forcing、MemRoPE、Deep Forcing、Pyramid-Forcing、LVSA、Self Forcing、Rolling Forcing、LongLive、Video Storyboarding、ConsisID、IAMFlow、SlotMemory、EM-Vid、Memento、WorldMem、SpMem、RELIC、LiveWorld、Mirage、MIND。

### High priority

Future Forcing、OmniMem、MAG、SWIFT、DecMem、FreeLong++、FreeSpec、FLEX、TPIGE、Gloria、VideoMemory、StoryMem、Context as Memory、MemCam、WorldPack、ReMind、MosaicMem。

### Related / background

Diffusion Forcing、CausVid、FramePack、Genie 2/3、Corgi、MALT Diffusion、Long-Context SSM Video World Models、Video generation surveys、world model surveys。

---

## 写作提醒

1. 这不是普通 long video survey，而是 memory system survey。
2. 论文分类应服务于 memory object、memory substrate、memory lifecycle。
3. ID 保持只是 memory 的一个子问题，不要让文章变窄。
4. world model 章节能把文章从视觉一致性提升到 object permanence 和 hidden-state evolution。
5. 后续 2026-07 锁版时，需要逐篇验证 To-check 条目，删除不可检索或不相关项。
