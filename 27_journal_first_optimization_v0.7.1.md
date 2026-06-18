# 27 Journal-First Optimization v0.7.1

> Stage: continue journal-first manuscript optimization.  
> Goal: deepen Section 5, define route-level table requirements, and identify whether additional figures are needed.

## 1. Current writing policy

The active manuscript should continue as a **journal-first, mechanism-level survey**. The conference benchmark direction remains useful as a later companion paper, but it should not drive the current manuscript. Evaluation should currently be written as a synthesis of existing diagnostic benchmarks rather than as a claim that we introduce a new benchmark.

The current writing priority is:

```text
Build a thesis-driven, mechanism-level survey of memory systems in video generation models, supported by route-level comparison tables, a full coverage appendix, and carefully selected synthesis figures.
```

## 2. Deepened Section 5: Implicit Token Memory in Attention and KV Caches

The v0.7.1 writing pass deepens Section 5 around a mechanism-level structure rather than a paper-by-paper list.

### 5.1 Problem and failure mode

Token/KV/attention memory becomes necessary when video generation moves from short clips to long rollouts, streaming generation, or autoregressive chunk prediction. A generator may maintain local frame quality while gradually losing identity, scene layout, temporal direction, or action history. In transformer-based video generation, this failure is often mediated by which historical tokens remain accessible, which attention heads actually use them, and how long-range context is compressed under memory budgets.

The central question of this route is:

```text
How can a video generator maintain useful historical evidence across long rollouts without storing every token forever?
```

### 5.2 Mechanism groups

Section 5 should be organized into six mechanism groups:

1. **Recent-window retention and causal rollout**: StreamingT2V, MAGI-style chunk generation, LongLive-like streaming training, Self-Forcing, Diffusion/Causal Forcing.
2. **Sink, anchor, and memory-token stabilization**: sink tokens, anchor tokens, memory tokens, MemRoPE.
3. **Sparse persistent blocks**: Sparse Forcing and related sparse-attention approaches.
4. **Head-aware routing and cache policy**: pyramid/head-aware cache policies.
5. **Historical KV retrieval**: OmniMem, WorldKV-like historical KV reuse.
6. **Quantization and system memory budget**: KV quantization, compression, offloading, and system budget studies.

### 5.3 Shared limitations

Token/KV memory methods share five limitations:

1. **Implicitness**: it is difficult to know what fact is stored in a latent or KV state.
2. **Staleness**: old tokens may preserve obsolete evidence after the scene changes.
3. **Selection bias**: salience measured now may not predict future usefulness.
4. **Position conflict**: long-range memory can fail if positional encoding cannot distinguish reused or extended history.
5. **Budget-quality trade-off**: more memory improves access but increases compute, latency, and instability.

### 5.4 Section-level role

The section should argue that Token/KV/attention memory is the systems backbone of long video generation. It explains how history is retained, compressed, routed, retrieved, and budgeted inside or near the transformer. However, because it is implicit, it cannot by itself guarantee entity-state or world-state correctness.

## 3. Route comparison table requirements

The journal paper should include one route table per major technical section. Each table should answer a different comparison question and should not merely repeat section headings.

### Table 5: Token/KV/Attention Memory

Required columns:

```text
Mechanism group | Representative methods | Memory object | Substrate | Lifecycle focus | Training regime | Main limitation | Evaluation implication
```

Suggested rows:

- recent-window retention and causal rollout;
- sink/anchor/memory-token stabilization;
- sparse persistent blocks;
- head-aware routing;
- historical KV retrieval;
- quantization and system memory budget.

### Table 6: Positional and Spectral Memory

Rows should include coordinate extrapolation, RoPE phase conflict, sink-collapse mitigation, frequency/spectral consistency, and identity-frequency bridges.

### Table 7: Identity, Entity, and Narrative Memory

Rows should include reference identity anchors, learned ID embeddings, identity slots, entity tables, object-centric memory, attribute-state tracking, reconstruction/verification loops, and narrative-role memory.

### Table 8: Retrieval-Augmented Recall

Rows should include latent retrieval, KV retrieval, scene recall frames, entity-conditioned retrieval, external corpus retrieval, and conflict filtering.

### Table 9: Spatial and World-State Memory

Rows should include static scene revisit, spatial layout memory, latent spatial cache, training-free KV world memory, hidden object/dynamic subject memory, geometry-aware implicit memory, and action-conditioned/embodied memory.

### Table 10: Memory Evaluation

Figure 10 should be converted into an auditable LaTeX table with columns:

```text
Dimension | What it tests | Representative benchmarks | Failure exposed | Not captured by generic video metrics
```

## 4. Figure requirements

The current F1--F10 are sufficient for the next writing pass. No urgent new large figure is required.

For the journal version, two additional synthesis figures would be valuable later:

### Optional Figure A: Training-Regime Spectrum

Purpose: show the axis from training-free memory to memory-oriented training.

Suggested content:

```text
Training-free / inference-time -> Adapter/fine-tuning -> Distillation/self-forcing -> Memory-oriented training -> Benchmark-only diagnostic
```

Example methods:

```text
RIFLEx, LoL, Sparse Forcing, WorldKV -> identity adapters -> Self-Forcing, LongLive -> HyDRA, GIM-World, LiveWorld, ReMind -> MIND, MBench, Echo-Memory
```

### Optional Figure B: World-State Memory Design Patterns

Purpose: summarize common modules across world-state methods.

Suggested modules:

```text
History encoder -> Compact memory state -> Query mechanism -> Apply to generation -> Revise hidden state -> Diagnostic evaluation
```

Example method families:

```text
WorldMem / SpMem / Mirage / RELIC / WorldKV / HyDRA / GIM-World / LiveWorld / ReMind / HiMem-WAM
```

If only one additional figure is drawn, choose **World-State Memory Design Patterns**, because Section 9 is the strongest differentiator of the journal survey.

## 5. Next writing pass

Next actions:

1. Merge Section 5 and Section 9 rewrites into the journal LaTeX source.
2. Create Table 5 and Table 9 in LaTeX.
3. Convert Figure 10 into Table 10.
4. Continue with Section 7 identity/entity/narrative memory.
5. Keep benchmark construction out of the main contribution for now.
