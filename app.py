import streamlit as st
from src.ImageToText import ImageToText
from src.StoryGenerator import StoryGenerator
from src.StoryTeller import StoryTeller
from dotenv import load_dotenv
import torch
import os

load_dotenv()

torch.classes.__path__ = []


def main():
    st.set_page_config("Story Teller", page_icon=":scroll:")
    st.header("Story Teller - 🤖 ")

    image_to_text_generator = ImageToText(
        model_id="Salesforce/blip-image-captioning-base"
    )
    story_generator = StoryGenerator(model_id="us.meta.llama3-2-90b-instruct-v1:0")
    story_teller = StoryTeller(model_id="espnet/kan-bayashi_ljspeech_vits")

    # File uploader
    uploaded_file = st.file_uploader(
        "Upload an image to tell a story", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        # Display uploaded image like a chat message
        with st.chat_message("user"):
            st.image(
                uploaded_file, caption="Here's my image!", use_container_width=True
            )

        image_caption = image_to_text_generator.get_image_captions(uploaded_file)
        caption_story = story_generator.generate_story(image_caption)
        story_teller.generate_speech_from_text(
            caption_story,
            "audio/generated_audio.flac",
            os.environ["HUGGINGFACE_API_TOKEN"],
        )

        # Simulate AI reply (placeholder)
        with st.chat_message("assistant"):

            st.markdown(f"Image Captions: \n{image_caption}")
            st.markdown("\n")
            st.markdown(f"Cool story about it: \n{caption_story}")

            with open("audio/generated_audio.flac", "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/flac")


if __name__ == "__main__":
    main()
