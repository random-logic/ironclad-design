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

## Brute Force
Time Add Identities (s):
0.033447265625
Mem footprint (GB):
0.00432
Time Query Probes (s/query):
0.11519265174865723
Max queries/s:
8.681109296641022

## HNSW
Time Add Identities (s):
0.3884561061859131
Mem footprint (GB):
0.004893197
Time Query Probes (s/query):
0.14606595039367676
Max queries/s:
6.846222526911997

## LSH

