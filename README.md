# AI Language Detection using Hugging Face and Streamlit

A simple web-based AI Language Detection application that uses a pre-trained Hugging Face Transformer model to identify the language of a given sentence or paragraph.

The application provides the detected language along with the language code and model's confidence score through an interactive Streamlit interface.

---

## Project Overview

This project demonstrates how Natural Language Processing (NLP) and Transformer-based models can be integrated into a lightweight web application.

The user enters a sentence or paragraph into the application. The text is then passed to a pre-trained language detection model from Hugging Face.

The model analyzes the text and returns:

- Detected language
- Language code
- Confidence score of the prediction

The result is displayed immediately through the Streamlit interface.

---

## Key Features

- Interactive web interface using Streamlit
- Pre-trained Transformer model from Hugging Face
- Multilingual language detection
- Supports multiple languages
- Language code displayed with the detected language
- Confidence score displayed as a percentage
- Input validation for empty text
- Model caching using Streamlit's `st.cache_resource`
- No model training required
- No API token required
- Simple and lightweight NLP application

---

## Technologies and Tools

| Technology / Tool | Purpose |
|-------------------|---------|
| Python | Core programming language |
| Streamlit | Creates the interactive web application |
| Hugging Face Transformers | Provides the pre-trained NLP model |
| XLM-RoBERTa | Performs language detection |
| PyTorch | Backend used by the Transformer pipeline |
| VS Code | Development environment |
| Git & GitHub | Version control and project hosting |

---

## AI Model

This project uses:

**Model:** `papluca/xlm-roberta-base-language-detection`

This is a multilingual XLM-RoBERTa model designed to identify the language of a given text.

The model predicts different language classes using language codes.

Examples include:

- `en` - English
- `fr` - French
- `es` - Spanish
- `de` - German
- `hi` - Hindi
- `it` - Italian
- `pt` - Portuguese
- `ar` - Arabic
- `zh` - Chinese
- `ja` - Japanese
- `ko` - Korean
- `ta` - Tamil
- `te` - Telugu
- `ml` - Malayalam
- `kn` - Kannada

The model also returns a confidence score representing how confident it is in the prediction.

---

## How the Application Works

The application follows a simple NLP workflow:

```text
User enters a sentence
          |
          v
   Streamlit Interface
          |
          v
     Text Validation
          |
          v
  Hugging Face Pipeline
          |
          v
   XLM-RoBERTa Model
          |
          v
   Language Prediction
          |
          v
    Detected Language
          |
          v
     Language Code
          |
          v
    Confidence Score
          |
          v
     Result Displayed
