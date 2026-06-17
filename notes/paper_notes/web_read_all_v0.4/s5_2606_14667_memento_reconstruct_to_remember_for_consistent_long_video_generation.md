# Memento: Reconstruct to Remember for Consistent Long Video Generation

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.14667
- URL: https://arxiv.org/abs/2606.14667
- Category: S5 Identity / entity / narrative memory 
- Priority: Must-read
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv/search abstract web-read

## 2. One-sentence takeaway

Memento makes an important diagnostic claim: if a memory bank really preserves a subject, it should be able to reconstruct that subject from memory alone.

## 3. Problem / failure mode

Shot-by-shot long-video methods optimize plausible next shots but do not verify whether historical memory still contains identity-critical subject evidence.

## 4. Memory object

- recurring subject identity

## 5. Memory substrate

- subject-reconstruction-guided memory bank + dual-query memory

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes historical subject evidence and global story captions into a memory bank supervised by reconstruction. |
| Store | Historical memory bank plus dual-query mechanism for identity evidence and short-context keyframes. |
| Retrieve | One query retrieves identity-relevant long-range memory; another selects short-context keyframes for continuation. |
| Use | Jointly trains next-shot generation and memory-based subject reconstruction. |
| Update | Memory evolves as story proceeds; reconstruction supervision preserves identity evidence. |
| Forget | Aims to prevent dilution/overwriting/forgetting but exact forgetting mechanism needs PDF. |
| Evaluate | Long-term subject consistency, cross-shot coherence and visual quality. |

## 7. Strengths for this survey

Excellent for evaluation section: reconstruction tests whether memory is actually useful.

## 8. Limitations / second-pass PDF checks

Requires training/data pipeline and precise subject descriptions; less plug-and-play than training-free methods.

## 9. Recommended placement

- Main category: S5 Identity / entity / narrative memory 
- Role: 把“记住主体”显式转化为可从 memory 重建主体的监督目标。
- Priority: Must-read
