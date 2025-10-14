# 1

euclidean metric

**Table 1.** Comparison of Mean Average Precision (mAP) for vggface2 and casia_webface under different conditions.

| Condition              | vggface2 mAP | casia_webface mAP |
|------------------------|--------------|-------------------|
| No env noise           | 0.6463       | 0.3726            |
| Gaussian blur          | 0.5575       | 0.2677            |
| Resizing               | 0.6278       | 0.3678            |
| Brightness adjustment  | 0.5506       | 0.3561            |



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
