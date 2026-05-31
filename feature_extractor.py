import numpy as np
from PIL import Image
import imagehash


class FeatureExtractor:
    def extract(self, image):
        if isinstance(image, str):
            img = Image.open(image).convert('L')
        elif isinstance(image, Image.Image):
            img = image.convert('L')
        else:
            img = Image.open(image).convert('L')
        h = imagehash.phash(img, hash_size=16)
        return np.array(h.hash, dtype=np.float32).flatten()
