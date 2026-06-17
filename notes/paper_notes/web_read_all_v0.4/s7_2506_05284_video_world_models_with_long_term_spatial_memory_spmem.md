# Video World Models with Long-term Spatial Memory / SpMem

## 1. Metadata

- Year: 2025
- ID: arXiv:2506.05284
- URL: https://arxiv.org/abs/2506.05284
- Category: S7 Video world model memory 
- Priority: Must-read
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

SpMem frames world-model memory after human memory: working memory for recent context, geometry-grounded long-term spatial memory for revisits, and episodic memory for past experiences.

## 3. Problem / failure mode

Action-conditioned world models forget previously generated environments during revisits because temporal context windows are limited.

## 4. Memory object

- long-term spatial memory

## 5. Memory substrate

- working memory + spatial memory + episodic memory

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes generated/observed scene information into explicitly stored 3D memory mechanisms. |
| Store | Working memory, geometry-grounded long-term spatial memory and episodic memory. |
| Retrieve | Retrieves spatial information for scene revisits and long-term consistency. |
| Use | Improves quality, consistency and context length of video world models. |
| Update | Memory is updated as the model explores/generates new parts of the scene. |
| Forget | Not explicit; focus on long-term storage/retrieval. |
| Evaluate | Custom datasets for training/evaluating explicitly stored 3D memory mechanisms. |

## 7. Strengths for this survey

Key taxonomy paper for working/spatial/episodic world-model memory.

## 8. Limitations / second-pass PDF checks

Requires geometry grounding and custom data.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: geometry-grounded spatial memory 核心论文。
- Priority: Must-read
