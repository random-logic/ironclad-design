import os
from typing import Sequence, List, Tuple

from analysis.task1 import ap_at_k, PROBE_DIR, get_identities_from, query_probe, add_identities


def get_identities_with_lowest_and_highest_ap_k(samples: Sequence[Tuple[str, Sequence[bool]]], n = 20) -> Tuple[List[str], List[str]]:
    all_ap_at_k = [(ap_at_k(sample[1]), sample[0]) for sample in samples]
    all_ap_at_k.sort()

    identities_with_lowest = [identity for _, identity in all_ap_at_k[:n]]
    identities_with_highest = [identity for _, identity in all_ap_at_k[-n:]]

    return identities_with_lowest, identities_with_highest


def query_probes_with_identity(k: int = 1) -> List[Tuple[str, List[bool]]]:
    res = []

    for identity in get_identities_from(PROBE_DIR):
        identity_path = os.path.join(PROBE_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            res.append((identity, [identity == file_name[:-5] for file_name in query_probe(image_path, k=k)]))

    return res


if __name__ == "__main__":
    add_identities()

    samples = query_probes_with_identity()
    worst_performing_identities, best_performing_identities = get_identities_with_lowest_and_highest_ap_k(samples)
    print("Worst Performing Identities:", worst_performing_identities)
    print("Best Performing Identities:", best_performing_identities)
