# 07 Collection Update v0.5: Scope, Candidate Papers, and Positioning Lock

> Version: v0.5 candidate update  
> Date: 2026-06-17  
> Stage: collection and positioning, not paper drafting.

## 1. Scope update

The survey should not be limited to either long video generation or video world models. The broader scope is:

> **Memory mechanisms in video-generation-model-based systems.**

This includes any field where the underlying foundation is a video generation model, video diffusion model, video diffusion transformer, autoregressive video generator, or generative video world model, and where memory is a central mechanism or failure source.

Therefore, the survey may cover:

1. Long-form / streaming video generation.
2. Interactive video generation.
3. Narrative and multi-shot video generation.
4. Identity-preserving video generation.
5. Retrieval-augmented video generation.
6. Video editing / video-to-video generation with memory.
7. Video world models and interactive simulators.
8. Driving / embodied video world models.
9. Evaluation benchmarks for memory, consistency, and world-state persistence.
10. System-level memory, including KV cache, sparse attention, and compression.

The unifying criterion is not the application domain, but whether the method exposes a memory object, memory substrate, memory lifecycle, or memory-related failure mode.

## 2. Working title candidates

### Candidate A

**Memory Systems in Video Generation Models: From KV Cache to Entity and World-State Memory**

This is the most general and currently preferred title. It does not restrict the paper to long videos or world models.

### Candidate B

**Remembering in Generative Video Models: A Survey of Token, Entity, Spatial, and World-State Memory**

This title is more conceptual and emphasizes memory itself.

### Candidate C

**Memory-Centric Video Generation: Mechanisms, Failures, and Evaluation**

This title is concise, but slightly less explicit about world models.

## 3. Recommended scope ratio

A reasonable balance is:

- General video-generation memory mechanisms: 35%.
- Long-form / streaming video generation memory: 25%.
- Identity / entity / narrative memory: 20%.
- Video world model / embodied memory: 15%.
- Evaluation and benchmarks: 5%.

This keeps the paper broader than a long-video survey, while avoiding becoming a generic world-model survey.

## 4. Newly collected candidates in this pass

The v0.5 supplement adds or resolves the following groups:

### AR / streaming / backbone context

- MAGI-1.
- StreamingT2V.
- SkyReels-V2.
- Pyramid Flow.

### Attention / KV / sparse memory

- Sparse VideoGen.
- Sparse Forcing.
- SVOO / sparse video generation profiling.

### Positional / RoPE / frequency memory

- RIFLEx.
- LoL: Longer than Longer.

### Identity / entity / narrative memory

- AnyID.
- Slot-ID.
- LaVieID.
- ConsistI2V.
- Concat-ID.
- FantasyID.
- Identity-GRPO.

### World-model and technical-report context

- OpenAI Sora technical report: Video generation models as world simulators.
- Genie 2 / Genie 3.
- V-JEPA 2.
- UniDriveDreamer.
- GAIA-1 / DriveDreamer / MagicDrive / other driving world-model family.

### Evaluation / benchmarks

- MBench.
- iWorld-Bench.
- WorldScore.

## 5. v0.5 goal

v0.5 should end with a locked discussion package, not a written paper:

1. Confirm final topic scope.
2. Confirm article structure.
3. Resolve metadata-only entries.
4. Add v0.5 candidate papers and web-read notes.
5. Decide which papers become mainline, background, appendix, or excluded.

Only after this lock should the project enter v0.6 writing.
