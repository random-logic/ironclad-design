import numpy as np

from analysis.task1 import mean_ap, query_probes, add_identities
from analysis.task2 import time_query_probes

if __name__ == '__main__':
    add_identities()

    '''
    res = np.array(query_probes(k=7))

    for k in range(1, 7):
        print(f"mAP for k = {k}:", mean_ap(res[:, :k]))
    '''

    for k in range(1, 7):
        print(f"Time Query Probes k={k} (s/query):")
        search_time = time_query_probes(k=k)
        print(search_time)
        print("Max queries/s:")
        print(1 / search_time)
