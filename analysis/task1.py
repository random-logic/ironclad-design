import os
from typing import List, Sequence
from PIL import Image, ImageFilter, ImageEnhance
import io
import requests

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

def apply_gaussian_blur(image_path: str, radius: float = 2.0) -> io.BytesIO:
    """Apply Gaussian blur to the image and return as BytesIO."""
    img = Image.open(image_path)
    img = img.filter(ImageFilter.GaussianBlur(radius))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)
    return buf

def apply_resize(image_path: str, size=(160, 160)) -> io.BytesIO:
    """Resize the image to the given size and return as BytesIO."""
    img = Image.open(image_path)
    img = img.resize(size)
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)
    return buf

def apply_brightness(image_path: str, factor: float = 1.2) -> io.BytesIO:
    """Adjust brightness (factor > 1 brighter, < 1 darker) and return as BytesIO."""
    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(factor)
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)
    return buf

def add_identities():
    for identity in get_identities_from(GALLERY_DIR):
        identity_path = os.path.join(GALLERY_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            requests.post("http://localhost:3000/add", files={"image": open(image_path, "rb")}, data={"name": file[:-4]})

def query_probe(image_path: str, k: int = 5):
    r = requests.post("http://localhost:3000/identify",
                      files={"image": open(image_path, 'rb')},
                      data={"k": str(k)})
    return r.json()["ranked identities"]

def query_probes(k: int = 5) -> List[List[bool]]:
    res = []

    for identity in get_identities_from(PROBE_DIR):
        identity_path = os.path.join(PROBE_DIR, identity)
        for file in os.listdir(identity_path):
            image_path = os.path.join(identity_path, file)
            res.append([identity == file_name[:-5] for file_name in query_probe(image_path, k=k)])

    return res

def ap_at_k(sample: Sequence[bool]) -> float:
    precision = sum(1 / (i + 1) for i, item in enumerate(sample) if item)
    total_relevant_items = sum(1 for item in sample if item)
    return precision / total_relevant_items if total_relevant_items > 0 else 0

def mean_ap(samples: Sequence[Sequence[bool]]) -> float:
    m = len(samples)
    return sum(ap_at_k(sample) for sample in samples) / m

def main():
    # add_identities()
    print(f"MAP: {mean_ap(query_probes())}")

if __name__ == '__main__':
    main()
