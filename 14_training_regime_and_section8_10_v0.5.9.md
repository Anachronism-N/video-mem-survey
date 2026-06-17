# 14 Training Regime and Section 8--10 Expansion v0.5.9

> Stage: continued writing pass after v0.5.8.  
> Goal: add the training-regime axis, then expand Retrieval-Augmented Recall, World-State Memory, and Memory Evaluation with top-conference-level tables and citations.

## 1. New cross-cutting axis: training regime

Memory methods should not be classified only by technical route and lifecycle. A third practical axis is the training/deployment regime:

```text
Technical route = what mechanism family the method belongs to
Lifecycle focus = what memory operation it emphasizes
Training regime = how the memory behavior is obtained
```

The new draft distinguishes:

1. **Training-free / inference-time memory.** Cache policy, RoPE/frequency correction, retrieval bank, reference injection, or entity lookup without changing model weights.
2. **Fine-tuning / adapter-based memory.** Learned reference encoders, identity adapters, LoRA modules, or memory routers.
3. **Distillation / self-forcing memory.** Teacher-to-student conversion or long-rollout distillation to create streaming/casual memory behavior.
4. **Memory-oriented training.** Data, curriculum, sparse attention, or event-aware training designed to teach memory explicitly.
5. **Benchmark-only / diagnostic.** No generation method, but a test of memory capability.

This axis is orthogonal to the route taxonomy. For example, token/KV memory includes both training-free cache policies and trainable sparse attention; identity/entity memory includes training-free entity banks and fine-tuned identity adapters; world-state memory often requires memory-oriented training because out-of-sight state evolution is difficult to elicit from frozen generators.

## 2. Tables added in v0.5.9

v0.5.9 adds four new tables:

1. **Training and deployment regimes for memory systems.**
2. **Retrieval-augmented memory methods.**
3. **Spatial and world-state memory methods.**
4. **Memory-aware evaluation benchmarks and diagnostic dimensions.**

These complement the v0.5.8 tables for token/KV memory, positional/spectral memory, and identity/entity/narrative memory.

## 3. Section 8 expansion

Section 8 now distinguishes retrieval by indexed memory object:

- Historical latents: LongLive-RAG.
- Historical KV cache: OmniMem.
- Scene memory and recall frames: Echo-Forcing.
- Entity-indexed latent patches: EM-Vid.
- Global entity IDs and attributes: IAMFlow.

The section also names three retrieval failures:

- under-recall,
- over-recall,
- wrong recall.

## 4. Section 9 expansion

Section 9 now emphasizes that world-state memory often requires stronger training than simple reference or cache memory. It adds a table covering:

- WorldMem.
- SpMem.
- RELIC.
- Mirage.
- LiveWorld.
- ReMind.

This section makes the training-regime point concrete: hidden state evolution is rarely solved by static reference injection or local frame continuity alone.

## 5. Section 10 expansion

Section 10 now includes a benchmark table covering:

- MIND.
- MBench.
- WorldScore.
- iWorld-Bench.
- EntityBench.
- LiveBench.

The section clarifies that ordinary video quality and short-term temporal consistency are not sufficient evidence of memory.

## 6. Citation updates

v0.5.9 adds citations for:

- OmniMem.
- RELIC.
- LiveWorld.
- ReMind.
- iWorld-Bench.

These were checked with current public metadata before inclusion.

## 7. Remaining tasks

Next pass should:

- Normalize all bibliography entries into BibTeX.
- Upgrade remaining author lists marked as “et al.”
- Replace the working two-column format with the official AAAI style once the author kit is available.
- Add figure placeholders and begin drawing Figure 1, Figure 3, Figure 4, Figure 5, and Figure 8.
- Decide whether Section 8 remains independent or is folded into Sections 5 and 7 after the full draft stabilizes.
