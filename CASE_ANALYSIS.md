# 1 - Model Performance Comparison: CASIA-WebFace vs. VGGFace2 on the IronClad Dataset


## Results

Table 1 reports the Mean Average Precision (mAP) for VGGFace2 and CASIA-WebFace across four environmental conditions using a BruteForce nearest neighbor search with Euclidean distance.

**Table 1.** Comparison of Mean Average Precision (mAP) for VGGFace2 and CASIA-WebFace under different environmental noise conditions on the IronClad dataset.

| Condition              | VGGFace2 mAP | CASIA-WebFace mAP |
|------------------------|--------------|-------------------|
| No environmental noise | 0.6463       | 0.3726            |
| Gaussian blur          | 0.5575       | 0.2677            |
| Resizing               | 0.6278       | 0.3678            |
| Brightness adjustment  | 0.5506       | 0.3561            |

Across all conditions, VGGFace2 outperforms CASIA-WebFace by approximately 0.2–0.3 mAP. This trend is consistent regardless of whether noise is introduced.

## Impact of Environmental Noise

Environmental degradations reduce performance for both models, but the relative gap between the two remains stable. Here is how the different environment noises impact the model:

* **Gaussian blur:** VGGFace2 drops from 0.6463 to 0.5575 (−13.7%) and CASIA-WebFace drops from 0.3726 to 0.2677 (−28.2%). Generally, VGGFace2 is more resilient to this type of noise than CASIA-WebFace.
* **Resizing:** VGGFace2 is minimally affected from 0.6463 to 0.6278 (−2.9%), while CASIA-WebFace also shows a small reduction from 0.3726 to 0.3678 (−1.3%). This means that both models are generally resilient towards this type of noise.
* **Brightness adjustment:** Both models degrade substantially, with VGGFace2 falling 14.8% and CASIA-WebFace 4.4%. Generally CASIA-WebFace is more resilient to this type of noise than VGGFace2, although VGGFace2 still beats CASIA-WebFace in raw accuracy.

VGGFace2 achieves higher accuracy under both the baseline condition (no environmental noise) and the more severe noise settings (Gaussian blur, brightness). CASIA-WebFace demonstrates consistently lower mAP values.

## Model Selection Argument

Given the goal of robust identity retrieval on the full IronClad dataset:

* **Accuracy advantage:** VGGFace2 maintains an absolute margin of +0.20 to +0.29 mAP across all conditions.
* **Noise resilience:** VGGFace2 retains higher performance under Gaussian blur and resizing—common artifacts in real-world data pipelines.
* **Generalization:** The consistency of VGGFace2’s advantage suggests stronger learned features and better suitability for deployment in varied environments.

Therefore, **VGGFace2 should be selected** for the IronClad dataset. While CASIA-WebFace is competitive in relative stability under brightness adjustments, its much lower absolute mAP scores make it unsuitable compared to VGGFace2.


# 2
VGG FACE, euclidean metric

CPU = Intel Core i5-11600k

| Metric                  | Brute Force | HNSW (PC) | LSH (PC) |
|-------------------------|-------------|-----------|----------|
| Time Add Identities (s) | 0.0602      | 0.3072    | 0.1590   |
| Mem footprint (GB)      | 0.0043      | 0.0049    | 0.0003   |
| Time Query Probes (s/q) | 0.2522      | 0.1728    | 0.1130   |
| Max queries/s           | 3.9658      | 5.7867    | 8.8480   |
| mAP                     | 0.6463      | 0.5575    | 0.3862   |


# 3
## Brute Force
mAP for k = 1: 0.7087087087087087
mAP for k = 2: 0.678928928928929
mAP for k = 3: 0.6618841063285508
mAP for k = 4: 0.6528333889445
mAP for k = 5: 0.6463371705038372
mAP for k = 6: 0.6392492492492493

## HNSW
