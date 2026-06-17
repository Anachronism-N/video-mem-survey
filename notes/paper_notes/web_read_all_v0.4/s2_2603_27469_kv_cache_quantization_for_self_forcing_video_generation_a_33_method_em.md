# KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.27469
- URL: https://arxiv.org/abs/2603.27469
- Category: S2 KV cache / attention memory 
- Priority: High
- Training-free: Empirical/system
- Original status: Verified by web, added in v0.2
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

This paper is a systems-memory study: it shows that nominal KV compression is not enough; realized VRAM, runtime, buffer reconstruction and terminal drift matter.

## 3. Problem / failure mode

Self-forcing long videos expose KV-cache growth as a systems bottleneck.

## 4. Memory object

- system memory / KV budget

## 5. Memory substrate

- KV-cache quantization and compression policies

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Not about semantic write; evaluates cache policies and quantization variants in self-forcing stack. |
| Store | Quantized/pruned KV caches including FlowCache-inspired soft-prune INT4 and other methods. |
| Retrieve | Retrieval follows attention cache access; emphasis is on storage/compression behavior. |
| Use | Compresses cache to reduce VRAM while preserving generation fidelity. |
| Update | Evaluates refresh stages and integration costs. |
| Forget | Soft-prune and cache policy variants implement system-level eviction/compression. |
| Evaluate | 33 variants, 610 prompt-level observations, 63 benchmark summaries, MovieGen/StoryEval, VRAM/runtime/SSIM/LPIPS/PSNR/terminal drift. |

## 7. Strengths for this survey

Essential for system memory section: compression ratio != deployment benefit.

## 8. Limitations / second-pass PDF checks

Not a semantic memory method; complements rather than replaces identity/scene memory.

## 9. Recommended placement

- Main category: S2 KV cache / attention memory 
- Role: 补充系统维度：量化/压缩不只是省显存，也会影响 drift、fidelity 与实际部署。
- Priority: High
