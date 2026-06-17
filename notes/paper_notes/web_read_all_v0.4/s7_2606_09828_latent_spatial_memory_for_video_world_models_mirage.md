# Latent Spatial Memory for Video World Models / Mirage

## 1. Metadata

- Year: 2026
- ID: arXiv:2606.09828
- URL: https://arxiv.org/abs/2606.09828
- Category: S7 Video world model memory 
- Priority: Must-read
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

Mirage argues spatial memory should live in diffusion latent space, not pixel-space point clouds, to avoid repeated rendering/VAE encoding and feature loss.

## 3. Problem / failure mode

Explicit RGB point-cloud memory is expensive and lossy for 3D-consistent video world models.

## 4. Memory object

- 3D spatial persistence

## 5. Memory substrate

- persistent latent 3D cache / depth-guided back-projection

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Lifts diffusion latent tokens into 3D via depth-guided back-projection. |
| Store | Persistent 3D cache in diffusion latent space. |
| Retrieve | Queries memory by latent-space warping to synthesize novel views. |
| Use | Eliminates pixel-space reconstruction bottlenecks and improves WorldScore/RealEstate10K reconstruction. |
| Update | Latent cache is updated as new scene regions are generated/observed. |
| Forget | Not central; memory footprint reduction is emphasized. |
| Evaluate | Reports up to 10.57x faster end-to-end generation and 55x memory footprint reduction vs explicit 3D baselines. |

## 7. Strengths for this survey

Key example of substrate innovation: latent 3D memory.

## 8. Limitations / second-pass PDF checks

Needs depth/geometric pipeline; PDF needed for exact warping and cache updates.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: latent-space 3D memory 核心新论文。
- Priority: Must-read
