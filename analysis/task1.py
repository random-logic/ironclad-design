import os
from typing import List

import requests

GALLERY_DIR = os.path.join(
    'multi_image_identities',
    'multi_image_gallery'
)

PROBE_DIR = os.path.join(
    'multi_image_identities',
    'probe'
)

# List only subdirectories
def get_identities_from(directory: str) -> List[str]:
    return [
        d for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d))
    ]

def add_identities():
    for identity in get_identities_from(GALLERY_DIR):
        identity_path = os.path.join(GALLERY_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            requests.post("http://localhost:3000/add", files={"image": open(image_path, "rb")}, data={"name": file[:-4]})

def query_probe(image_path: str, k: int = 5):
    r = requests.post("http://localhost:3000/identify",
                      files={"image": open(image_path, "rb")},
                      data={"k": str(k)})
    return r.json()["ranked identities"]

def query_probes() -> List[List[bool]]:
    res = []

    for identity in get_identities_from(PROBE_DIR):
        identity_path = os.path.join(PROBE_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            res.append([identity == file_name[:-5] for file_name in query_probe(image_path, k=5)])

    return res

def ap_at_k(sample: List[bool]) -> float:
    precision = sum(1 / (i + 1) for i, item in enumerate(sample) if item)
    total_relevant_items = sum(1 for item in sample if item)
    return precision / total_relevant_items if total_relevant_items > 0 else 0

def mean_ap(samples: List[List[bool]]) -> float:
    m = len(samples)
    return sum(ap_at_k(sample) for sample in samples) / m

def main():
    print(f"MAP: {mean_ap(query_probes())}")

if __name__ == '__main__':
    main()
