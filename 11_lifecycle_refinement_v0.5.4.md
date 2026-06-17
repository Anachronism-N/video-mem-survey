# 11 Lifecycle Refinement v0.5.4

> Stage: lifecycle-story refinement.  
> Goal: remove overlap between Write and Preserve, simplify the lifecycle story, and make the memory narrative easier to use inside technical-route sections.

## 1. Problem with the previous lifecycle

The previous fine-grained lifecycle was:

```text
Write -> Retain -> Compress -> Route -> Retrieve -> Inject/Use -> Update -> Forget -> Evaluate
```

This is useful as an engineering checklist, but it has three problems for the paper narrative:

1. **Write and Preserve/Retain overlap.** Both can sound like “keeping information.”
2. **Compress and Route are not always sequential.** Some methods route first, then compress; others compress through routing.
3. **Evaluate is not an internal memory operation.** Evaluation is an external validation loop, not part of memory itself.

Therefore, the lifecycle should be simplified for storytelling.

## 2. Revised two-level lifecycle

Use two levels:

### Level 1: story-level phases

These are used in prose:

```text
Register -> Maintain -> Access -> Apply -> Revise -> Validate
```

### Level 2: fine-grained operations

These are used in tables:

```text
write / encode / anchor
retain / preserve / stabilize
compress / route / index
retrieve / recall / select
inject / condition / control
update / overwrite / decay / forget
evaluate / diagnose / stress-test
```

The story-level phases should be the primary wording in the paper. The fine-grained operations should appear in taxonomy tables, method tables, and paper annotations.

## 3. Definitions of the revised phases

### 3.1 Register

**Question:** What information becomes memory in the first place?

Register is about the entry point of memory. It covers how a system turns a frame, prompt, reference, entity, state, or token into something that can be reused later.

Examples:

- A first frame becomes an appearance anchor.
- A reference image becomes identity memory.
- A prompt is parsed into entities and attributes.
- Historical KV tokens become token memory.
- Pose/time metadata becomes spatial or world-state memory.

Register is different from Maintain because registration does not guarantee long-term survival. It only defines what enters the memory system.

### 3.2 Maintain

**Question:** How is memory kept usable under time and budget constraints?

Maintain combines preserve, compress, route, and index. These operations are tightly coupled in video generation models: memory cannot be preserved unless it is made computationally feasible and addressable.

Examples:

- Memory tokens summarize old frames.
- Sink tokens or anchor frames preserve global context.
- KV cache is pruned, quantized, or sparsified.
- Attention heads are assigned different memory roles.
- Entity memories are stored in slots or latent patch banks.

Maintain is not just “keep everything.” It means keeping the right information in a usable form.

### 3.3 Access

**Question:** When the model needs history, which memory is selected?

Access is about retrieval and selection. It decides whether the current generation step needs old scene memory, entity memory, reference memory, spatial memory, or global state memory.

Examples:

- Scene recall frames are selected.
- Historical KV blocks are sparsely retrieved.
- Relevant entity IDs are looked up.
- A latent spatial memory is queried by pose or camera state.
- A reference identity is selected from multiple candidates.

Access is different from Apply because retrieval alone does not determine how memory influences the generated frame.

### 3.4 Apply

**Question:** How does selected memory influence generation?

Apply covers injection, conditioning, attention reuse, cross-attention, guidance, and state-conditioned rollout.

Examples:

- Retrieved frames are injected through attention.
- Identity embeddings condition facial or subject generation.
- Entity memory controls character attributes.
- Spatial memory conditions camera-consistent rollout.
- Retrieved latent tokens guide future video chunks.

Access selects memory; Apply uses memory.

### 3.5 Revise

**Question:** How does memory change after the world, prompt, or entity state changes?

Revise combines update and forget. These should be discussed together because video memory is not only about keeping old information; it must also remove stale or conflicting information.

Examples:

- Difference-aware memory decay weakens irrelevant history.
- Entity attributes are updated after VLM verification.
- Out-of-sight states continue to evolve.
- A subject is reconstructed to refresh memory.
- Sink-collapse mitigation prevents over-retention of old frames.
- Cache eviction removes low-value or harmful memory.

Revise is the most important phase for moving from passive visual consistency to active state persistence.

### 3.6 Validate

**Question:** How do we know memory is real?

Validate is not an internal operation of the model. It is the evaluation loop that tests whether the model truly remembers identity, scene, entity state, environment, causality, and hidden dynamics.

Examples:

- Identity consistency.
- Scene revisit consistency.
- Entity/environment/causal consistency.
- Out-of-sight dynamics.
- Closed-loop action control.
- Memory budget and efficiency.

Validate should be introduced in Section 4.3, but fully discussed in the evaluation section.

## 4. Why this is better than Write/Preserve

The previous terms Write and Preserve are close because both sound like storage. The new terms separate them:

| Old term | New term | Difference |
|---|---|---|
| Write | Register | Entry into memory: what becomes memory? |
| Preserve / Retain | Maintain | Survival and usability: how is memory kept addressable and affordable? |
| Retrieve | Access | Selection: which memory is needed now? |
| Inject / Use | Apply | Influence: how does memory control generation? |
| Update / Forget | Revise | Adaptation: how does memory change or decay? |
| Evaluate | Validate | External testing: did memory actually work? |

This version avoids the Write/Preserve overlap and gives the paper a cleaner story.

## 5. Recommended narrative

The paper can tell the story as follows:

> A video generation model first registers information from prompts, frames, references, entities, and states. Since long videos and interactive systems cannot keep everything, the model must maintain memory under limited context and compute by compressing, routing, and indexing it. At generation time, memory must be accessed selectively and applied through attention, conditioning, retrieval, or state rollout. As the scene, prompt, or hidden world changes, memory must be revised: updated, decayed, overwritten, or forgotten. Finally, memory must be validated through diagnostic benchmarks rather than surface-level video quality metrics.

This is the recommended high-level story.

## 6. How to use these phases inside technical-route sections

Each technical-route section should use only the phases that are relevant to that route.

### Token/KV/Attention Memory

- Register: historical tokens enter KV cache.
- Maintain: cache retention, memory tokens, sinks, sparse blocks, quantization.
- Access: sparse KV retrieval, scene recall.
- Apply: attention reuse or retrieved-context conditioning.
- Revise: cache eviction, decay, sink-collapse mitigation.

### Positional/Spectral Memory

- Register: temporal coordinates and frequency components are assigned.
- Maintain: coordinates remain valid under long rollout.
- Access: old content can be retrieved only if positions remain meaningful.
- Apply: positional/frequency correction affects generation dynamics.
- Revise: phase conflict, spectral degradation, or sink collapse must be corrected.

### Identity/Entity/Narrative Memory

- Register: references, identities, entities, and attributes are encoded.
- Maintain: identity embeddings, slots, entity tables, latent patch banks keep them stable.
- Access: relevant entity or subject is selected for current generation.
- Apply: identity/entity memory is injected into generation.
- Revise: attributes, subject state, and narrative role are updated or repaired.

### Retrieval-Augmented Memory

- Register: memories are stored in external or latent banks.
- Maintain: banks are indexed and possibly compressed.
- Access: relevant memory is retrieved.
- Apply: retrieved memory guides generation.
- Revise: stale retrieved memory is filtered, decayed, or replaced.

### Spatial/World-State Memory

- Register: spatial layout, pose, object state, and world state are stored.
- Maintain: scene memory, spatial cache, episodic memory, or global state persists.
- Access: memory is queried by camera, action, pose, or scene revisit.
- Apply: state-conditioned generation maintains spatial/world consistency.
- Revise: hidden or out-of-sight state evolves.

## 7. Multi-category paper handling

A paper may span several routes, but it should be explained in detail only once. Use:

```text
primary_route + lifecycle_focus + secondary_tags
```

The primary route is where the method is explained. Lifecycle focus is the story used to explain it. Secondary tags appear only in tables or short cross-references.

Example:

- MemRoPE primary route: Token/KV/Attention Memory.
- Lifecycle focus: Maintain.
- Secondary tags: positional memory, RoPE, memory tokens.

Example:

- IAMFlow primary route: Identity/Entity/Narrative Memory.
- Lifecycle focus: Register -> Access -> Apply -> Revise.
- Secondary tags: retrieval memory, narrative memory.

Example:

- LiveWorld primary route: Spatial/World-State Memory.
- Lifecycle focus: Revise.
- Secondary tags: out-of-sight dynamics, causal consistency, evaluation.

## 8. Recommended Section 4.3 wording

Section 4.3 should be named:

> **Memory Lifecycle: From Registration to Revision**

It should define the six story-level phases:

```text
Register -> Maintain -> Access -> Apply -> Revise -> Validate
```

Then it should include a table that maps these phases to fine-grained operations and representative methods.

The method chapters should not repeat all six phases mechanically. They should use whichever phases explain the core contribution of each technical route.
