import os
from typing import List
import requests
from analysis.task1 import query_probes, mean_ap

GALLERY_DIR = os.path.join(
    'storage',
    'multi_image_gallery'
)

PROBE_DIR = os.path.join(
    'storage',
    'probe'
)

# List only subdirectories
def get_identities_from(directory: str) -> List[str]:
    return [
        d for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d))
    ]

def add_identities() -> float:
    res = 0.0
    for identity in get_identities_from(GALLERY_DIR):
        identity_path = os.path.join(GALLERY_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            response = requests.post("http://localhost:3000/add", files={"image": open(image_path, "rb")}, data={"name": file[:-4]})
            res += response.json().get("build_time")

    return res

def time_query_probe(image_path: str, k: int = 5) -> float:
    r = requests.post("http://localhost:3000/identify",
                      files={"image": open(image_path, "rb")},
                      data={"k": str(k)})
    return r.json().get("search_time")

def time_query_probes() -> float:
    res = 0.0

    for identity in get_identities_from(PROBE_DIR):
        identity_path = os.path.join(PROBE_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            res += time_query_probe(image_path, k=5)

    return res

def main():
    print("Time Add Identities (s):")
    print(add_identities())
    print("Mem footprint (GB):")
    r = requests.get("http://localhost:3000/index/memory")
    print(r.json().get("memory_footprint_gb"))
    print("Time Query Probes (s/query):")
    search_time = time_query_probes()
    print(search_time)
    print("Max queries/s:")
    print(1/search_time)
    print("mAP:")
    print(mean_ap(query_probes()))

if __name__ == "__main__":
    main()
