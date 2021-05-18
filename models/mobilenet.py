import timm


class MobileNetV3:
    def __init__(self):
        self._predictor = timm.create_model("mobilenetv3_large_100", pretrained=True)
