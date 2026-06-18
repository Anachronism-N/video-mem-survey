# 32 v0.7.7 Identity and World-State Deepening

> Stage: continue journal-first writing after v0.7.6 formula/pseudocode pass.  
> Goal: deepen Section 7 and Section 9, repair compact route tables, and add additional pseudo-algorithmic support.

## 1. Main update

v0.7.7 continues the journal-first manuscript development. The key change is that identity/entity/narrative memory and world-state memory are now written in a more mechanism-level style, closer to a journal survey section rather than a short conference sketch.

## 2. Section 7: Identity, Entity, and Narrative Memory

Section 7 now separates six mechanism groups:

1. Reference anchors.
2. Learned identity embeddings and adapters.
3. Slots and object-centric memory.
4. Entity tables and attribute-state memory.
5. Narrative-role memory.
6. Reconstruction and verification loops.

The section now argues that the main difficulty is not only identity preservation, but identity-state disentanglement: persistent identity should remain stable while mutable attributes, relations, locations, roles, and possessions remain revisable.

## 3. New Section 7 pseudo-algorithm

v0.7.7 adds:

```text
Pseudo-algorithmic view of entity-state memory maintenance
```

The table maps entity memory to the lifecycle:

- Register: create entity IDs and identity embeddings.
- Maintain: separate persistent identity from mutable state.
- Access: retrieve entity records by ID, role, reference feature, or shot requirement.
- Apply: condition generation with identity anchors or entity facts.
- Revise: update mutable state and merge/split conflicting entities.
- Validate: check identity drift, attribute contradiction, relation errors, and duplication.

## 4. Section 9: Spatial and World-State Memory

Section 9 now has a stronger state-centric formulation. It separates:

- static scene layout,
- spatial anchors,
- hidden object state,
- dynamic subject state,
- causal environment state,
- action-conditioned state.

Mechanism groups now include static scene revisit, latent spatial context, training-free KV world memory, hidden object/dynamic subject memory, geometry-aware implicit memory, and action-conditioned/embodied memory.

## 5. New Section 9 formulas

v0.7.7 adds a world-state record:

```tex
\mathcal{W}_t=(\mathcal{L}_t,\mathcal{O}_t,\mathcal{H}_t,\mathcal{A}_t)
```

where layout, visible object state, hidden state, and action-conditioned state are separated.

It also adds a transition interface:

```tex
\mathcal{W}_{t+1}=T(\mathcal{W}_t,u_t,y_{t+1},\epsilon_{t+1})
```

and a vector-valued world-memory diagnostic:

```tex
\mathbf{s}_{world}=(s_{revisit},s_{geom},s_{hidden},s_{causal},s_{action},s_{budget})
```

This emphasizes that world-state memory cannot be validated by visual quality alone.

## 6. Table repair

v0.7.7 compacts the identity/entity/narrative and world-state tables. The main-text tables now emphasize mechanism group, memory object/state, substrate/interface, lifecycle focus, and representative methods. Longer diagnostic questions and paper-level caveats should move to appendix audit tables.

## 7. Output status

Local artifacts:

```text
TMM_Journal_Track_v0.7.7_preview.pdf
TMM_Journal_Track_v0.7.7.zip
```

The PDF compiles successfully and has been rendered for visual checking. It is now 11 pages. The new tables are more readable than earlier spreadsheet-like versions, although route tables remain dense and will need appendix-level detailed counterparts later.

## 8. Next writing tasks

1. Deepen Section 6: Positional and Spectral Memory.
2. Expand Section 10: Evaluation synthesis, without claiming a new benchmark.
3. Add appendix-level audit tables for limitations, evaluation implications, citations, and verification status.
4. Strengthen the introduction with the literature trend from visual continuity to world-state persistence.
5. Start normalizing BibTeX for all mainline and high-support methods.
