# 1 - Model Performance Comparison
To assess the performance of VGGFace2 and CASIA-WebFace, we compare them using the mAP (Mean Average Precision) metric. This metric is superior as it not only measures whether relevant identities are retrieved, but also incorporates the ranking of those identities—penalizing cases where true matches are pushed further down the list. Unlike plain precision, which treats a correct match at rank 1 the same as one at rank 5, mAP rewards models that consistently place relevant items higher in the ranking. Furthermore, it increases as a greater proportion of all relevant identities are included in the retrieved set, making it a more comprehensive evaluation of retrieval quality.

### Results
**Table 1.** Comparison of mAP for VGGFace2 and CASIA-WebFace under different environmental noise conditions on the IronClad dataset.

| Condition              | VGGFace2 mAP | CASIA-WebFace mAP |
|------------------------|--------------|-------------------|
| No environmental noise | 0.6463       | 0.3726            |
| Gaussian blur          | 0.5575       | 0.2677            |
| Resizing               | 0.6278       | 0.3678            |
| Brightness adjustment  | 0.5506       | 0.3561            |

Table 1 reports the Mean Average Precision (mAP) for VGGFace2 and CASIA-WebFace across four environmental conditions using a BruteForce nearest neighbor search with Euclidean distance. Across all conditions, VGGFace2 outperforms CASIA-WebFace by approximately 0.2–0.3 mAP. This trend is consistent regardless of whether noise is introduced.

### Impact of Environmental Noise
Environmental degradations reduce performance for both models, but the relative gap between the two remains stable. Here is how the different environment noises impact the model:

* **Gaussian blur:** VGGFace2 drops from 0.6463 to 0.5575 (−13.7%) and CASIA-WebFace drops from 0.3726 to 0.2677 (−28.2%). Generally, VGGFace2 is more resilient to this type of noise than CASIA-WebFace.
* **Resizing:** VGGFace2 is minimally affected from 0.6463 to 0.6278 (−2.9%), while CASIA-WebFace also shows a small reduction from 0.3726 to 0.3678 (−1.3%). This means that both models are generally resilient towards this type of noise.
* **Brightness adjustment:** Both models degrade substantially, with VGGFace2 falling 14.8% and CASIA-WebFace 4.4%. Generally CASIA-WebFace is more resilient to this type of noise than VGGFace2, although VGGFace2 still beats CASIA-WebFace in raw accuracy.


### Model Selection Argument
VGGFace2 achieves higher accuracy under both the baseline condition (no environmental noise) and the more severe noise settings (Gaussian blur, brightness). CASIA-WebFace demonstrates consistently lower mAP values. Therefore, VGGFace2 should be selected.

# 2
VGG FACE, euclidean metric

CPU = Intel Core i5-11600k

**Table 2.** Comparison of Brute Force, HNSW, and LSH methods on PC in terms of identity addition time, memory footprint, query speed, and retrieval accuracy (mAP).

| Metric                  | Brute Force | HNSW (PC) | LSH (PC) |
|-------------------------|-------------|-----------|----------|
| Time Add Identities (s) | 0.0602      | 0.3072    | 0.1590   |
| Mem footprint (GB)      | 0.0043      | 0.0049    | 0.0003   |
| Time Query Probes (s/q) | 0.2522      | 0.1728    | 0.1130   |
| Max queries/s           | 3.9658      | 5.7867    | 8.8480   |
| mAP                     | 0.6463      | 0.5575    | 0.3862   |


# 3
# VGGFace2

## Brute Force
**Table: VGGFace2 – Brute Force Results (per k value)**

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.7087 | 0.3316             | 3.0161        |
| 2 | 0.6789 | 0.3319             | 3.0128        |
| 3 | 0.6619 | 0.3357             | 2.9793        |
| 4 | 0.6528 | 0.3706             | 2.6986        |
| 5 | 0.6463 | 0.3569             | 2.8017        |
| 6 | 0.6392 | 0.3634             | 2.7520        |

## HNSW
**Table: VGGFace2 – HNSW Results (per k value)**

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.7087 | 0.1659             | 6.0278        |
| 2 | 0.6784 | 0.1678             | 5.9587        |
| 3 | 0.6617 | 0.1672             | 5.9807        |
| 4 | 0.6524 | 0.1723             | 5.8050        |
| 5 | 0.6459 | 0.1718             | 5.8214        |
| 6 | 0.6388 | 0.1727             | 5.7896        |

## LSH
**Table: VGGFace2 – LSH Results (per k value)**

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.4875 | 0.0947             | 10.5600       |
| 2 | 0.4940 | 0.0953             | 10.4949       |
| 3 | 0.4903 | 0.0951             | 10.5118       |
| 4 | 0.4834 | 0.0961             | 10.4013       |
| 5 | 0.4790 | 0.0961             | 10.4018       |
| 6 | 0.4754 | 0.0970             | 10.3104       |

# CASIA
## Brute Force
**Table: CASIA – Brute Force Results (per k value)**

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.3624 | 0.1902             | 5.2567        |
| 2 | 0.3774 | 0.1920             | 5.2077        |
| 3 | 0.3732 | 0.1964             | 5.0921        |
| 4 | 0.3697 | 0.1935             | 5.1669        |
| 5 | 0.3687 | 0.1934             | 5.1708        |
| 6 | 0.3651 | 0.1949             | 5.1306        |

## HNSW
**Table: CASIA – HNSW Results (per k value)**

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.3624 | 0.1796             | 5.5679        |
| 2 | 0.3774 | 0.1827             | 5.4734        |
| 3 | 0.3732 | 0.1829             | 5.4670        |
| 4 | 0.3697 | 0.1829             | 5.4664        |
| 5 | 0.3687 | 0.1844             | 5.4216        |
| 6 | 0.3651 | 0.1818             | 5.4998        |

## LSH
**Table: CASIA – LSH Results (per k value)**

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.1211 | 0.0981             | 10.1894       |
| 2 | 0.1421 | 0.0940             | 10.6393       |
| 3 | 0.1481 | 0.0919             | 10.8850       |
| 4 | 0.1532 | 0.0949             | 10.5355       |
| 5 | 0.1548 | 0.0961             | 10.4065       |
| 6 | 0.1564 | 0.0967             | 10.3460       |

# 4
# VGGFace
m = 1, max = 5, k = 5
MAP: 0.8299457994579945

m = 2, max = 5, k = 5
MAP: 0.7150406504065041

m = 3, max = 5, k = 5
MAP: 0.6057588075880758

m = 1, max = 5
MAP: 0.7642276422764228

m = 2, max = 5
MAP: 0.8780487804878049

m = 3, max = 5
MAP: 0.9186991869918699

m = 4, max = 5
MAP: 0.9349593495934959

m = 5, max = 5
MAP: 0.9512195121951219

m = 1, max = 3
MAP: 0.75

m = 2, max = 3
MAP: 0.8531746031746031

m = 3, max = 3
MAP: 0.8968253968253969

m = 1, max = 10
MAP: 0.8627450980392157

m = 2, max = 10
MAP: 0.9411764705882353

m = 3, max = 10
MAP: 0.9803921568627451

m = 4, max = 10
MAP: 0.9803921568627451

m = 5, max = 10
MAP: 0.9803921568627451

m = 1, max = 7
MAP: 0.8333333333333334

m = 2, max = 7
MAP: 0.8974358974358975

m = 3, max = 7
MAP: 0.9358974358974359

m = 4, max = 7
MAP: 0.9615384615384616

m = 5, max = 7
MAP: 0.9615384615384616

m = 6, max = 7
MAP: 0.9615384615384616

m = 1, max = 4
MAP: 0.7619047619047619

m = 2, max = 4
MAP: 0.8452380952380952

m = 3, max = 4
MAP: 0.8869047619047619

m = 4, max = 4
MAP: 0.9047619047619048

m = 1, max = 6
MAP: 0.8247422680412371

m = 2, max = 6
MAP: 0.9072164948453608

m = 3, max = 6
MAP: 0.9381443298969072

m = 4, max = 6
MAP: 0.9484536082474226

m = 5, max = 6
MAP: 0.9587628865979382

m = 6, max = 6
MAP: 0.9587628865979382

## TODO - Casia-Webface

# 5

