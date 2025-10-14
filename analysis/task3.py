import numpy as np

from analysis.task1 import mean_ap, query_probes, add_identities

if __name__ == '__main__':
    add_identities()
    res = np.array(query_probes(k=7))

    for k in range(1, 7):
        print(f"mAP for k = {k}:", mean_ap(res[:, :k]))
