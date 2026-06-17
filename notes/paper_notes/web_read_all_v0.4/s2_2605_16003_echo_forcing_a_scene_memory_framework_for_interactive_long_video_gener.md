# Echo-Forcing: A Scene Memory Framework for Interactive Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.16003
- URL: https://arxiv.org/abs/2605.16003
- Category: S2 KV cache / attention memory 
- Priority: Must-read
- Training-free: Yes
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

Echo-Forcing is the clearest scene-memory paper: it reframes long-video degradation as functional entanglement of historical KV states and explicitly separates stable anchors, compressed history, recent windows, recall, and conflict-aware forgetting.

## 3. Problem / failure mode

Interactive AR video generation under prompt switching suffers from old-scene forgetting, delayed prompt response, and background contamination because all historical KV tokens are handled by one cache policy.

## 4. Memory object

- scene memory / historical scene recall

## 5. Memory substrate

- hierarchical temporal KV memory

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes historical scene evidence into hierarchical temporal KV states; old scenes can be crystallized as Scene Recall Frames. |
| Store | Stable anchors, compressed history, and recent windows under relative RoPE; scene recall frames store spatially structured KV representations. |
| Retrieve | Retrieves long-range scene evidence through Scene Recall Frames when old scenes need to reappear. |
| Use | Injects/reuses recalled historical KV evidence during generation to support smooth transitions, hard cuts, and old-scene recall. |
| Update | Updates bounded cache by maintaining recent dynamics and compressed history instead of keeping a uniform sliding window. |
| Forget | Difference-aware Memory Decay adaptively suppresses tokens that conflict with the current/new scene. |
| Evaluate | VBench-Long and interactive long-video settings; should be paired with dynamic/anti-loop metrics because stable recall may otherwise be over-rewarded. |

## 7. Strengths for this survey

Best representative for the preserve-recall-forget lifecycle; ideal as the anchor example in Section 4.

## 8. Limitations / second-pass PDF checks

Scene-centric rather than entity-centric; it remembers what/where a scene is more than who an entity is.

## 9. Recommended placement

- Main category: S2 KV cache / attention memory 
- Role: 场景记忆核心论文：stable anchor、compressed history、recent window、scene recall、difference-aware decay。
- Priority: Must-read
