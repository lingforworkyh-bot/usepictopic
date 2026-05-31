import numpy as np
from PIL import Image, ImageFilter
import imagehash


class FeatureExtractor:
    def extract(self, image):
        if isinstance(image, str):
            img = Image.open(image)
        elif isinstance(image, Image.Image):
            img = image
        else:
            img = Image.open(image)

        gray = img.convert('L')
        rgb = img.convert('RGB')

        ph = np.array(imagehash.phash(gray, hash_size=16).hash, dtype=np.float32).flatten()
        dh = np.array(imagehash.dhash(gray, hash_size=16).hash, dtype=np.float32).flatten()
        wh = np.array(imagehash.whash(gray, hash_size=16).hash, dtype=np.float32).flatten()

        hist = np.array(rgb.histogram(), dtype=np.float32)
        hist = hist / (hist.sum() + 1e-8)

        return np.concatenate([ph, dh, wh, hist])
