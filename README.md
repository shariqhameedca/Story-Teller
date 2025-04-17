# Story Teller - AI Powered Image Story Generator

This project allows users to upload an image and receive a short, AI-generated caption for the image, followed by a creative story inspired by that caption. The application provides a fun and engaging way to explore the narratives hidden within your photos.

## Features

* **Image Captioning:** Utilizes an AI model to automatically generate a descriptive caption for the uploaded image.
* **Story Generation:** Leverages another AI model to create a unique and imaginative story based on the generated image caption.
* **User-Friendly Interface:** Built with Streamlit, providing a simple and intuitive web interface for easy interaction.

## How to Use

Follow these steps to run the Story Teller application on your local system:

### Prerequisites

* **Python 3.6 or higher:** Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
* **pip:** Python package installer, usually included with Python installations.
* **Git (Optional):** If you want to clone the repository.

### Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [<repository_url>](https://github.com/shariqhameedca/Story-Teller)
    cd Story-Teller
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate   # On Windows
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This command will install all the necessary libraries listed in the `requirements.txt` file, including Streamlit, Transformers, PyTorch, and python-dotenv.

4.  **Set up environment variables:**
    Create a `.env` file in the root directory of the project and add these API keys:

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_DEFAULT_REGION
    USER_AGENT
    OPENSEARCH_ENDPOINT
    HUGGINGFACE_API_TOKEN

    ```

### Running the Application

1.  **Navigate to the project's root directory in your terminal.**

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

3.  **Open your web browser:** Streamlit will automatically open a new tab (usually at `http://localhost:8501`) where you can interact with the Story Teller application.

### Using the Application

1.  **Upload an Image:** On the web interface, you will see a file uploader. Click on "Browse files" and select an image file (JPG, JPEG, or PNG) from your local system.

2.  **View Caption and Story:** Once the image is uploaded, the AI will process it. The generated image caption and the story based on that caption will be displayed in the chat-like interface.

## Project Structure

StoryTeller/
├── pycache/
├── src/
│   ├── pycache/
│   ├── ImageToText.py
│   ├── StoryGenerator.py
│   └── StoryTeller.py
├── .env
├── app.py
├── config.py
└── requirements.txt
└── README.md

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements, bug fixes, or new features, feel free to submit a pull request.

## License
