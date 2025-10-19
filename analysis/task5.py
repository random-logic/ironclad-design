import math
import os
from typing import Sequence, Tuple, List

from analysis.task1 import ap_at_k, PROBE_DIR, get_identities_from, query_probe


def get_identities_with_lowest_and_highest_ap_k(samples: Sequence[Tuple[str, Sequence[bool]]]) -> Tuple[List[str], List[str], float, float]:
    # Compute AP@k for each sample
    all_ap_at_k = [ap_at_k(sample[1]) for sample in samples]

    # Get min and max AP@k values
    lowest_ap = min(all_ap_at_k)
    highest_ap = max(all_ap_at_k)

    # Tolerance for floating-point comparisons
    eps = 1e-6

    # Get all identities with AP close to the lowest and highest
    identities_with_lowest = [
        samples[i][0] for i, ap in enumerate(all_ap_at_k)
        if math.isclose(ap, lowest_ap, abs_tol=eps)
    ]
    identities_with_highest = [
        samples[i][0] for i, ap in enumerate(all_ap_at_k)
        if math.isclose(ap, highest_ap, abs_tol=eps)
    ]

    return identities_with_lowest, identities_with_highest, lowest_ap, highest_ap


def query_probes_with_identity(k: int = 1) -> List[Tuple[str, List[bool]]]:
    res = []

    for identity in get_identities_from(PROBE_DIR):
        identity_path = os.path.join(PROBE_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            res.append((identity, [identity == file_name[:-5] for file_name in query_probe(image_path, k=k)]))

    return res


if __name__ == "__main__":
    # add_identities()

    samples = query_probes_with_identity()
    worst_performing_identities, best_performing_identities, lowest_map, highest_map = get_identities_with_lowest_and_highest_ap_k(samples)
    print(f"Worst Performing Identities (map = {lowest_map}):", worst_performing_identities)
    print(f"Best Performing Identities (map = {highest_map}:", best_performing_identities)


