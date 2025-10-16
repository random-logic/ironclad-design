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
mAP for k = 1: 0.7087087087087087
mAP for k = 2: 0.678928928928929
mAP for k = 3: 0.6618841063285508
mAP for k = 4: 0.6528333889445
mAP for k = 5: 0.6463371705038372
mAP for k = 6: 0.6392492492492493

Time Query Probes k=1 (s/query):
0.33155179023742676
Max queries/s:
3.0161200435198747
Time Query Probes k=2 (s/query):
0.3319120407104492
Max queries/s:
3.012846409125519
Time Query Probes k=3 (s/query):
0.33565402030944824
Max queries/s:
2.979258222732067
Time Query Probes k=4 (s/query):
0.37056922912597656
Max queries/s:
2.6985510976143297
Time Query Probes k=5 (s/query):
0.3569221496582031
Max queries/s:
2.8017314166622134
Time Query Probes k=6 (s/query):
0.363372802734375
Max queries/s:
2.751994625010498

## HNSW
mAP for k = 1: 0.7087087087087087
mAP for k = 2: 0.6784284284284284
mAP for k = 3: 0.6617172728283839
mAP for k = 4: 0.652416305194083
mAP for k = 5: 0.6459200867534202
mAP for k = 6: 0.6388321654988323

Time Query Probes k=1 (s/query):
0.16589760780334473
Max queries/s:
6.027814464843891
Time Query Probes k=2 (s/query):
0.16782307624816895
Max queries/s:
5.958656117834752
Time Query Probes k=3 (s/query):
0.1672046184539795
Max queries/s:
5.980696043244969
Time Query Probes k=4 (s/query):
0.17226457595825195
Max queries/s:
5.805024012843758
Time Query Probes k=5 (s/query):
0.17177915573120117
Max queries/s:
5.821428075736925
Time Query Probes k=6 (s/query):
0.17272377014160156
Max queries/s:
5.789591086277151

## LSH
mAP for k = 1: 0.4874874874874875
mAP for k = 2: 0.493993993993994
mAP for k = 3: 0.4902958514069625
mAP for k = 4: 0.4833931153375598
mAP for k = 5: 0.4789828717606495
mAP for k = 6: 0.47536063841619397

Time Query Probes k=1 (s/query):
0.0946969985961914
Max queries/s:
10.559996777344734
Time Query Probes k=2 (s/query):
0.09528446197509766
Max queries/s:
10.49489055478266
Time Query Probes k=3 (s/query):
0.09513163566589355
Max queries/s:
10.511750302623236
Time Query Probes k=4 (s/query):
0.09614157676696777
Max queries/s:
10.401327226240989
Time Query Probes k=5 (s/query):
0.09613752365112305
Max queries/s:
10.401765741636288
Time Query Probes k=6 (s/query):
0.09698939323425293
Max queries/s:
10.310405773802062

# CASIA
## Brute Force
mAP for k = 1: 0.36236236236236236
mAP for k = 2: 0.37737737737737737
mAP for k = 3: 0.3732065398732065
mAP for k = 4: 0.36973779334890444
mAP for k = 5: 0.3687159381603826
mAP for k = 6: 0.36507146034923815

Latency:
Time Query Probes k=1 (s/query):
0.1902329921722412
Max queries/s:
5.256711722720408
Time Query Probes k=2 (s/query):
0.19202446937561035
Max queries/s:
5.207669643622061
Time Query Probes k=3 (s/query):
0.19638395309448242
Max queries/s:
5.09206574286082
Time Query Probes k=4 (s/query):
0.1935405731201172
Max queries/s:
5.1668752648539975
Time Query Probes k=5 (s/query):
0.19339418411254883
Max queries/s:
5.170786311847072
Time Query Probes k=6 (s/query):
0.19490790367126465
Max queries/s:
5.130628266807584

## HNSW
mAP for k = 1: 0.36236236236236236
mAP for k = 2: 0.37737737737737737
mAP for k = 3: 0.3732065398732065
mAP for k = 4: 0.36973779334890444
mAP for k = 5: 0.3687159381603826
mAP for k = 6: 0.36507146034923815

Time Query Probes k=1 (s/query):
0.17960000038146973
Max queries/s:
5.56792871868599
Time Query Probes k=2 (s/query):
0.18270039558410645
Max queries/s:
5.473441898157512
Time Query Probes k=3 (s/query):
0.18291568756103516
Max queries/s:
5.466999650679611
Time Query Probes k=4 (s/query):
0.1829373836517334
Max queries/s:
5.46635127297845
Time Query Probes k=5 (s/query):
0.1844487190246582
Max queries/s:
5.421561099951656
Time Query Probes k=6 (s/query):
0.1818242073059082
Max queries/s:
5.499817735036571

## LSH
mAP for k = 1: 0.12112112112112113
mAP for k = 2: 0.14214214214214213
mAP for k = 3: 0.148120342564787
mAP for k = 4: 0.15320876431987543
mAP for k = 5: 0.15475308641975308
mAP for k = 6: 0.15637276165053943

Time Query Probes k=1 (s/query):
0.09814119338989258
Max queries/s:
10.189401264229874
Time Query Probes k=2 (s/query):
0.09399151802062988
Max queries/s:
10.639257893254936
Time Query Probes k=3 (s/query):
0.09186959266662598
Max queries/s:
10.884994381424704
Time Query Probes k=4 (s/query):
0.09491682052612305
Max queries/s:
10.53554042852478
Time Query Probes k=5 (s/query):
0.09609413146972656
Max queries/s:
10.406462753815923
Time Query Probes k=6 (s/query):
0.09665608406066895
Max queries/s:
10.34596021262688

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

# 5
