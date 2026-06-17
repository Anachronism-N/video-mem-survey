# papers/ PDF 下载与重命名说明

本目录用于保存综述相关论文 PDF。当前运行环境尝试通过 `curl https://arxiv.org/pdf/<id>.pdf` 下载时发生 DNS 解析失败，因此本次没有把 PDF 二进制文件直接写入仓库。为了保证后续可复现，v0.2 资料包中已经生成：

- `papers/download_manifest.tsv`：所有可识别 arXiv 论文的 PDF URL 与目标重命名路径。
- `scripts/download_papers.py`：离线/本地环境可直接运行的下载脚本。

## 推荐本地执行

```bash
python scripts/download_papers.py --manifest papers/download_manifest.tsv --root .
```

下载后的命名规则：

```text
papers/pdfs/<category>/<category>_<arxiv_id>_<short_slug>.pdf
```

示例：

```text
papers/pdfs/s2/s2_2605.16003_echo_forcing_a_scene_memory_framework.pdf
```

## 当前状态

- 可生成下载 URL 的 arXiv 条目数：81。
- PDF 二进制：本次受运行环境网络限制未能直接下载。
- 论文笔记：已在 `notes/paper_notes/` 建立索引和重点论文结构化精读笔记。
