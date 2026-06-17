# WEB_READ_SUMMARY_v0.4

> Generated on 2026-06-17. This is the first all-paper web-reading pass based on arXiv pages, arXiv search summaries, prior survey tables, and structured metadata.

## Scope

- Total entries in `tables/papers_master.csv`: 102.
- Structured notes generated locally: 102.
- Core papers/benchmarks with detailed web-read extraction in this pass: 25.
- Remaining entries with stable arXiv/project URLs: marked `metadata-web-ready` for second-pass direct HTML/PDF verification.
- Entries without stable arXiv URLs: marked `metadata-only` and require manual URL confirmation.

## Files in the local v0.4 artifact

- `notes/paper_notes/WEB_READ_INDEX_v0.4.md`
- `notes/paper_notes/WEB_READ_NOTES_ALL_v0.4.md`
- `notes/paper_notes/WEB_READ_STATUS_v0.4.csv`
- `notes/paper_notes/web_read_all_v0.4/`: one structured note per paper.

## Detailed web-read papers in this pass

### KV / attention / positional memory

- Echo-Forcing: hierarchical temporal KV memory, scene recall frames, difference-aware decay.
- MemRoPE: dual EMA memory tokens plus unrotated key cache and online RoPE indexing.
- Deep Forcing: deep sink plus participative compression; warns that naive sinks can cause motion stagnation.
- Pyramid Forcing: Anchor/Wave/Veil head types and head-aware cache policies.
- LongLive-RAG: self-generated latents as content-addressable retrieval memory.
- Future Forcing: future-aware KV token retention.
- OmniMem: full-range sparse KV retrieval.
- KV Cache Quantization for Self-Forcing: systems-memory study of 33 cache/quantization variants.

### Identity / entity / narrative memory

- IAMFlow: LLM-extracted entities, global IDs, and VLM-verified identity-aware memory.
- SlotMemory: object-centric KV semantic slots.
- EM-Vid: entity-indexed sparse latent patch memory.
- Memento: subject-reconstruction-guided historical memory.
- CoTriSyGen: closed-loop visual-text-memory synergy with mutable visual state.

### World-model spatial / state memory

- WorldMem: memory frames plus state metadata such as poses and timestamps.
- Video World Models with Long-term Spatial Memory / SpMem: working, spatial, and episodic memory.
- RELIC: compressed historical latent tokens with relative actions and absolute camera poses in KV cache.
- LiveWorld: persistent global state and out-of-sight dynamics.
- Mirage / Latent Spatial Memory: diffusion-latent 3D cache.
- ReMind: memory-oriented data and curriculum for out-of-sight state evolution.
- MosaicMem: hybrid explicit/implicit spatial patch memory.
- MIND: benchmark for memory consistency and action control.

## Status convention

- `web-read`: detailed extraction from arXiv/search page content opened in browser during this pass.
- `metadata-web-ready`: structured note generated and URL available, but still needs direct second-pass page/PDF verification.
- `metadata-only`: no stable paper URL in master table; requires manual URL confirmation.

## Next pass

The next pass should open each `metadata-web-ready` arXiv page directly and fill missing formula, figure, benchmark, and ablation details. PDF is still useful for final BibTeX accuracy, equations, algorithm blocks, and table values, but is not required for this first structured reading pass.
