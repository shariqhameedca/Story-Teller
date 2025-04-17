from openai import OpenAI
import boto3


class StoryGenerator:
    def __init__(self, model_id):
        self.model_id = model_id
        self.bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

    def generate_story(self, text):

        user_message = f"""
            <|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are a story writer that takes a sentence describing a scene and creates a fun, cool story about it.
            <|eot_id|>
            <|start_header_id|>user<|end_header_id|>
            Write a 100-200 words story about this sentence {text}
            <|eot_id|>
            <|start_header_id|>assistant<|end_header_id|>
            """
        messages = [
            {
                "role": "user",
                "content": [
                    {"text": user_message},
                ],
            }
        ]

        response = self.bedrock_client.converse(
            modelId=self.model_id,
            messages=messages,
        )
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text
