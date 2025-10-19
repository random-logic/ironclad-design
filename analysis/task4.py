import os
from typing import List

import requests

from analysis.task1 import get_identities_from, GALLERY_DIR, query_probes, mean_ap, PROBE_DIR, query_probe


def count_identities():
    img_counts = [0] * 10

    for identity in get_identities_from(GALLERY_DIR):
        identity_path = os.path.join(GALLERY_DIR, identity)
        count = len(os.listdir(identity_path))
        img_counts[min(count - 1, len(img_counts) - 1)] += 1

    # Get suffix sum
    for i in range(len(img_counts) - 2, -1, -1):
        img_counts[i] += img_counts[i + 1]

    return img_counts


def get_galleries_with_min_images(min_images_required: int) -> List[str]:
    """
    @return list of identities that satisfy the condition
    """
    res = []
    for identity in get_identities_from(GALLERY_DIR):
        identity_path = os.path.join(GALLERY_DIR, identity)
        if len(os.listdir(identity_path)) >= min_images_required:
            res.append(identity)
    return res

def add_identities_with_m_gallery_images(m: int, gallery_min_images: int):
    for identity in get_galleries_with_min_images(gallery_min_images):
        identity_path = os.path.join(GALLERY_DIR, identity)
        files = sorted(os.listdir(identity_path)[:m]) # Extract only the first m identities
        for file in files:
            image_path = os.path.join(identity_path, file)
            requests.post("http://localhost:3000/add", files={"image": open(image_path, "rb")}, data={"name": file[:-4]})


def query_probes_with_m_gallery_images(gallery_min_images: int, k: int = 1) -> List[List[bool]]:
    res = []

    for identity in get_galleries_with_min_images(gallery_min_images):
        identity_path = os.path.join(PROBE_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            res.append([identity == file_name[:-5] for file_name in query_probe(image_path, k=k)])

    return res


if __name__ == '__main__':
    print(count_identities())

    gallery_min_images = 10
    for m in range(1, gallery_min_images + 1):
        print(f'm = {m}, max = {gallery_min_images}')
        add_identities_with_m_gallery_images(m, gallery_min_images)
        print(f"MAP: {mean_ap(query_probes_with_m_gallery_images(gallery_min_images))}")
