# WEB_READ_NOTES_SUPPLEMENT_v0.5

> Version: v0.5 supplement  
> Stage: candidate validation and theme discussion.  
> Scope: memory mechanisms in video-generation-model-based systems.

## 1. MAGI-1

- Category: S1 AR / streaming video generation backbone.
- Status: resolved background.
- Core idea: MAGI-1 generates videos autoregressively as sequences of fixed-length chunks. It supports causal temporal modeling, streaming generation, and constant peak inference cost regardless of video length.
- Memory relevance: It is not a dedicated memory paper, but it explains the system context where memory becomes necessary. Chunk-level autoregression naturally creates a historical context and cache-management problem.
- Suggested use: Background section, not main memory taxonomy.
- Memory tags: chunk memory, causal rollout, context budget, deployment memory.

## 2. StreamingT2V

- Category: S1/S5 early explicit video memory precursor.
- Status: resolved related.
- Core idea: StreamingT2V uses autoregressive long video generation with a short-term memory block, the conditional attention module, and a long-term appearance preservation module.
- Memory relevance: This is one of the clearest early cases where long video generation explicitly separates short-term transition memory from long-term appearance/scene memory.
- Suggested use: Bridge between early long-video generation and modern structured memory systems.
- Memory tags: short-term memory, long-term appearance memory, first-chunk memory, chunk transition.

## 3. SkyReels-V2

- Category: S1 long-form video system.
- Status: resolved technical-report/system background.
- Core idea: SkyReels-V2 combines MLLM-based captioning, progressive-resolution pretraining, reinforcement learning, and diffusion forcing for infinite-length film-style generation.
- Memory relevance: It is a system-level long-form generator rather than a memory method. It motivates memory as part of film-level continuity, shot-aware generation, and long-form deployment.
- Suggested use: Background or system landscape.
- Memory tags: film-level context, shot structure, long-horizon system.

## 4. Pyramid Flow

- Category: S1 long-video backbone.
- Status: resolved background.
- Core idea: Pyramid Flow is a flow-matching / pyramid-style video generation backbone.
- Memory relevance: It provides long-video generation background, but should not be treated as a memory method unless a specific memory mechanism is identified.
- Suggested use: Background only.
- Memory tags: long-video backbone, temporal pyramid.

## 5. Sparse VideoGen

- Category: S2 sparse attention / head-role background.
- Status: resolved related.
- Core idea: Sparse VideoGen shows that video DiT attention heads exhibit spatial and temporal sparse patterns, and proposes online profiling to classify attention heads and accelerate inference.
- Memory relevance: The method is primarily for efficiency, but it supports the argument that different attention heads carry different temporal/spatial roles. This is useful background for head-aware memory routing and Pyramid-Forcing-like cache policies.
- Suggested use: S2 attention-memory background.
- Memory tags: head roles, spatial attention, temporal attention, sparse attention, profiling.

## 6. Sparse Forcing

- Category: S2 KV / attention memory.
- Status: new mainline candidate.
- Core idea: Sparse Forcing observes that autoregressive diffusion rollouts concentrate attention on persistent salient visual blocks. These blocks form implicit spatiotemporal memory in the KV cache. It introduces trainable sparsity and Persistent Block-Sparse Attention.
- Memory relevance: This is highly aligned with the survey because it explicitly interprets persistent KV blocks as memory. It links cache compression, salient block persistence, and long-horizon quality.
- Suggested use: Main S2 paper together with Echo-Forcing, MemRoPE, Pyramid-Forcing, OmniMem, and KV-cache quantization.
- Memory tags: persistent blocks, KV memory, sparse memory, updateable cache, system memory.

## 7. RIFLEx

- Category: S3 positional / RoPE memory.
- Status: resolved mainline background.
- Core idea: RIFLEx analyzes the frequency components of positional embeddings in video diffusion transformers and identifies intrinsic frequency as a key factor for length extrapolation. It reduces intrinsic frequency to suppress temporal repetition while maintaining motion consistency.
- Memory relevance: RIFLEx supports the thesis that memory requires valid temporal coordinates. Keeping old tokens is not enough if RoPE/frequency coordinates make their temporal meaning collapse.
- Suggested use: Positional memory section.
- Memory tags: RoPE, intrinsic frequency, length extrapolation, temporal coordinate.

## 8. LoL: Longer than Longer

- Category: S3/S2 positional memory and sink memory.
- Status: resolved mainline candidate.
- Core idea: LoL identifies sink-collapse, where generated content repeatedly reverts to sink frames. It attributes the problem to conflict between RoPE periodicity and multi-head attention, and proposes multi-head RoPE jitter.
- Memory relevance: LoL is important because it connects three issues: attention sink, positional phase, and head homogenization. It shows that a memory mechanism can fail because of coordinate/head-role conflict.
- Suggested use: Bridge between attention sink memory and positional memory.
- Memory tags: sink-collapse, RoPE jitter, multi-head conflict, infinite streaming.

## 9. AnyID

- Category: S5 identity memory.
- Status: new related candidate.
- Core idea: AnyID targets universal identity-preserving video generation from heterogeneous identity references, including faces, portraits, and videos. It introduces an omni-referenced architecture and a primary-reference paradigm.
- Memory relevance: AnyID broadens identity memory from single-reference conditioning to multi-reference identity aggregation. It is a precursor to more explicit entity-state memory.
- Suggested use: Identity-memory precursor group, not central entity-memory method unless we focus more on identity preservation.
- Memory tags: identity reference, canonical anchor, attribute control, identity fidelity.

## 10. Slot-ID

- Category: S5 identity dynamics memory.
- Status: new related candidate.
- Core idea: Slot-ID uses short reference videos rather than a single image, and extracts compact temporal identity tokens through slot-based temporal identity encoding.
- Memory relevance: It is stronger than static ID conditioning because it models characteristic identity dynamics, such as expression and pose changes. This makes it a bridge between identity memory and entity-state memory.
- Suggested use: Identity/entity bridge.
- Memory tags: temporal identity tokens, reference-video memory, identity dynamics, slot routing.

## 11. OpenAI Sora technical report

- Category: S7 technical-report background.
- Status: technical report.
- Core idea: Sora uses spacetime latent patches and diffusion transformers to train on variable-duration, variable-resolution visual data. The report highlights emergent simulation capabilities, including 3D consistency, long-range coherence, object permanence, interactions with world state, and digital-world simulation.
- Memory relevance: Sora is not a memory-method paper, but it establishes the high-level argument that large-scale video generation models can behave like world simulators. Its limitations, including physics errors and state-update failures, motivate memory-aware world-state modeling.
- Suggested use: Introduction and background.
- Memory tags: spacetime patches, long-range coherence, object permanence, world-state interaction.

## 12. V-JEPA 2

- Category: S7 latent world-model boundary.
- Status: background.
- Core idea: V-JEPA 2 is a self-supervised video model that learns visual representations from large-scale video and supports prediction and planning through a latent action-conditioned world model.
- Memory relevance: It is not a generative video diffusion model, so it should be used as boundary material. It helps distinguish generative video world models from JEPA-style latent world models.
- Suggested use: Background and scope boundary.
- Memory tags: latent prediction, planning, physical world model, representation memory.

## 13. UniDriveDreamer

- Category: S7 embodied / driving world model.
- Status: new related candidate.
- Core idea: UniDriveDreamer is a single-stage multimodal world model for autonomous driving that jointly generates video and LiDAR observations using unified latent anchoring.
- Memory relevance: It extends memory from visual video to cross-modal world-state memory. For the survey, it should be a boundary/background example rather than a central method unless the paper emphasizes embodied memory.
- Suggested use: Driving/embodied world-model background.
- Memory tags: multimodal memory, video-LiDAR latent anchoring, temporal evolution, scene layout.

## 14. WorldScore

- Category: S8 evaluation benchmark.
- Status: resolved benchmark.
- Core idea: WorldScore evaluates world generation through controllability, quality, and dynamics over next-scene generation tasks with explicit camera trajectories.
- Memory relevance: It is not purely memory-specific, but its dynamics and scene-controllability dimensions are relevant to spatial and world-state memory evaluation.
- Suggested use: Evaluation background.
- Memory tags: world generation, controllability, dynamics, scene trajectory.

## 15. MBench

- Category: S8 memory benchmark.
- Status: new mainline benchmark.
- Core idea: MBench directly evaluates memory capability of video world models. It decomposes memory into entity consistency, environment consistency, and causal consistency, further refined into multiple sub-dimensions.
- Memory relevance: This is one of the most important evaluation papers for the survey because it treats memory as the object of evaluation rather than as an implicit consistency issue.
- Suggested use: Central benchmark in Evaluation section.
- Memory tags: entity consistency, environment consistency, causal consistency, long-term retention.

## 16. iWorld-Bench

- Category: S8 interactive world-model benchmark.
- Status: new benchmark candidate.
- Core idea: iWorld-Bench evaluates interactive world models with a unified action generation framework and tasks covering visual generation, trajectory following, and memory.
- Memory relevance: It supports the argument that memory should be tested in closed-loop interaction, not only open-loop video generation.
- Suggested use: Evaluation section, especially for interactive memory.
- Memory tags: interactive memory, trajectory following, action generation, closed-loop benchmark.

## Current conclusion

The v0.5 supplement suggests that the survey should be broader than long-video generation and world models. A better formulation is:

> Memory systems in video-generation-model-based systems.

This includes long video, identity-preserving video, narrative video, video editing, retrieval-augmented video, world models, driving simulators, and memory-specific benchmarks, as long as the central issue is what is remembered, where it is stored, how it is retrieved or updated, and how memory failure is evaluated.
