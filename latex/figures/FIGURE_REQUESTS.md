# Figure Requests / 图示需求

本综述建议优先绘制原创示意图，而不是直接截取论文图片，避免版权和风格不统一问题。

## Figure 1: Memory failure taxonomy

**位置**：Introduction。  
**内容**：六个 failure panel：identity drift、scene forgetting、motion loop/frozen video、RoPE phase conflict、entity duplication、out-of-sight freezing。  
**需要**：可以用抽象小人/场景/时间轴示意图，不必使用真实生成视频。

## Figure 2: Memory lifecycle

**位置**：What Should Video Models Remember?  
**内容**：Write -> Store -> Retrieve -> Use -> Update -> Forget -> Evaluate。  
**需要**：中心放 memory bank，外圈放生命周期箭头；每个阶段标注代表方法。

## Figure 3: Memory substrate map

**位置**：Preliminaries 或 taxonomy。  
**内容**：Frame memory、KV cache、sink token、compressed token、RoPE coordinate、spectrum、entity table、latent patch bank、3D cache、SSM state。  
**需要**：横轴从 implicit 到 explicit，纵轴从 2D visual 到 world-state。

## Figure 4: From video generation to video world models

**位置**：World Model Memory。  
**内容**：Visual continuity -> narrative continuity -> spatial persistence -> world-state evolution。  
**需要**：四级金字塔或路线图。

## Figure 5: Method taxonomy overview

**位置**：可选，放在正文前半。  
**内容**：S1-S8 分类总览：backbone、KV/attention、position/RoPE、frequency、identity/entity、retrieval、world-model、evaluation。

## Figure 6: Evaluation trap

**位置**：Evaluation。  
**内容**：稳定但静止的视频 vs 动态但身份漂移的视频 vs 好的视频。  
**需要**：说明为什么单一 consistency metric 不够。
