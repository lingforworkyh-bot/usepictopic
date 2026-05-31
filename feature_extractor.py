import numpy as np
from PIL import Image
import onnxruntime as ort


_session = ort.InferenceSession('mobilenet_feat.onnx')
MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)


def _preprocess(img):
    img = img.resize((224, 224), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = (arr - MEAN) / STD
    arr = np.transpose(arr, (2, 0, 1))
    return np.expand_dims(arr, 0)


class FeatureExtractor:
    def extract(self, image):
        if isinstance(image, str):
            img = Image.open(image).convert('RGB')
        elif isinstance(image, Image.Image):
            img = image.convert('RGB')
        else:
            img = Image.open(image).convert('RGB')
        tensor = _preprocess(img)
        feat = _session.run(['features'], {'input': tensor})[0]
        return feat.flatten().astype(np.float32)
