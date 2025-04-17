import torch
from transformers import pipeline
from transformers.utils import is_flash_attn_2_available
import requests
import os


class StoryTeller:
    def __init__(self, model_id):
        self.API_URL = f"https://api-inference.huggingface.co/models/{model_id}"

    def generate_speech_from_text(self, message, output_file, HUGGINGFACE_API_TOKEN):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
        payloads = {"inputs": message}

        response = requests.post(self.API_URL, headers=headers, json=payloads)
        with open(output_file, "wb") as file:
            file.write(response.content)
