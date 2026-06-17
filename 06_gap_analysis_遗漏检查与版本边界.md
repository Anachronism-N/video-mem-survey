# 06 遗漏检查与版本边界

> 当前检查日期：2026-06-17  
> 结论：不能严格声称“无遗漏”，尤其不能声称“截至 2026 年 7 月无遗漏”。当前版本是截至 2026-06-17 的可检索文献库，并已补入本轮发现的新增条目。

## 1. 本轮新增/修正条目

本轮检索在原有 100 条基础上补充或重点确认：

1. **KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study**，arXiv:2603.27469。应归入 S2 / system memory，因为它系统评估 KV 量化/压缩对 VRAM、runtime、fidelity、terminal drift 的影响。
2. **Closed-Loop Triplet Synergistic Generation for Long-Form Video / CoTriSyGen**，arXiv:2606.16184。应归入 S5 / entity-narrative memory，因为它把多镜头长视频生成建模为 visual-text-memory closed loop，并维护 mutable visual state。
3. 再次确认 **LongLive-RAG**，arXiv:2606.02553，应同时出现在 S2/S6，因为它把自生成历史 latent 组织成 content-addressable retrieval memory。
4. 再次确认 **Memento**，arXiv:2606.14667，应归入 S5，因为它用 subject reconstruction 监督历史 memory bank 是否真正保留主体证据。

## 2. 当前未完成的复核事项

1. 若干 `To verify` 条目仍需在 2026-07 锁版前逐篇确认，包括 StreamingT2V、MAGI-1、MemCam、MALT Diffusion、LongLive-RAG 衍生 repo、Echo-Memory/JoyAI-Echo 等。
2. 一些系统/项目页条目没有标准 arXiv ID，下载 PDF 脚本不会覆盖，需要人工补 URL。
3. 2026 年 7 月论文尚未全部出现，因此必须在 2026-07-31 后复检。

## 3. 不能说的话

- 不应说“已经确认没有任何遗漏论文”。
- 不应说“已覆盖截至 2026 年 7 月的所有论文”。
- 不应把未验证的项目页条目当成正式论文引用。

## 4. 可以说的话

- 已建立截至 2026-06-17 的 video memory survey 文献库。
- 已覆盖当前能检索到的核心路线：KV/attention memory、RoPE/position memory、frequency memory、identity/entity memory、retrieval memory、world-model spatial/state memory、evaluation benchmark。
- 已为 2026-07 锁版预留检索协议、下载 manifest、阅读笔记模板和索引。
