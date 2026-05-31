import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import onnxruntime as ort


_session = ort.InferenceSession('mobilenet_feat.onnx')
_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


class FeatureExtractor:
    def extract(self, image):
        if isinstance(image, str):
            img = Image.open(image).convert('RGB')
        elif isinstance(image, Image.Image):
            img = image.convert('RGB')
        else:
            img = Image.open(image).convert('RGB')
        tensor = _transform(img).unsqueeze(0).numpy().astype(np.float32)
        feat = _session.run(['features'], {'input': tensor})[0]
        return feat.flatten().astype(np.float32)
