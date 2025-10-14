# 1 - Model Performance Comparison: CASIA-WebFace vs. VGGFace2 on the IronClad Dataset


## Results

Table 1 reports the Mean Average Precision (mAP) for VGGFace2 and CASIA-WebFace across four environmental conditions using a BruteForce nearest neighbor search with Euclidean distance.

**Table 1.** Comparison of Mean Average Precision (mAP) for VGGFace2 and CASIA-WebFace under different environmental noise conditions on the IronClad dataset.

| Condition              | VGGFace2 mAP | CASIA-WebFace mAP |
| ---------------------- | ------------ | ----------------- |
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

## Brute Force (PC)
Time Add Identities (s):
0.06016826629638672
Mem footprint (GB):
0.004320187
Time Query Probes (s/query):
0.2521541118621826
Max queries/s:
3.965828645882087
mAP:
0.6463371705038372

## HNSW (PC)
Time Add Identities (s):
0.30722951889038086
Mem footprint (GB):
0.004893197
Time Query Probes (s/query):
0.17280960083007812
Max queries/s:
5.786715525043597
mAP:
0.5575102880658436

## LSH (PC)
Time Add Identities (s):
0.15897607803344727
Mem footprint (GB):
0.000277978
Time Query Probes (s/query):
0.11302042007446289
Max queries/s:
8.847958619700364
mAP:
0.38624374374374376
