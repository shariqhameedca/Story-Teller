from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


class ImageToText:
    def __init__(self, model_id):
        self.processor = BlipProcessor.from_pretrained(model_id)
        self.model = BlipForConditionalGeneration.from_pretrained(model_id)

    def get_image_captions(self, image_file):
        raw_image = Image.open(image_file).convert("RGB")

        # conditional image captioning
        text = "A photography of"
        inputs = self.processor(raw_image, text, return_tensors="pt")

        out = self.model.generate(**inputs)
        return self.processor.decode(out[0], skip_special_tokens=True)
