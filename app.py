import streamlit as st
from transformers import pipeline

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Language Detection",
    page_icon="Language",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------

st.title("AI Language Detection System")

st.write(
    "Enter a sentence or paragraph and the AI model "
    "will detect the language."
)

# -------------------------------
# Load Hugging Face Model
# -------------------------------

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="papluca/xlm-roberta-base-language-detection"
    )


classifier = load_model()

# -------------------------------
# Language Mapping
# -------------------------------

language_codes = {
    "af": "Afrikaans",
    "am": "Amharic",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "et": "Estonian",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "ga": "Irish",
    "gl": "Galician",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jv": "Javanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mr": "Marathi",
    "ms": "Malay",
    "my": "Burmese",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "or": "Odia",
    "pa": "Punjabi",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "sq": "Albanian",
    "sr": "Serbian",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-cn": "Chinese",
    "zh-tw": "Chinese",
}

# -------------------------------
# Text Input
# -------------------------------

text = st.text_area(
    "Enter your text:",
    placeholder="Example: Bonjour, comment allez-vous aujourd'hui?",
    height=150
)

# -------------------------------
# Detect Language
# -------------------------------

if st.button("Detect Language"):

    if not text.strip():

        st.warning("Please enter some text.")

    else:

        with st.spinner("Detecting language..."):

            result = classifier(text)[0]

        language_code = result["label"]
        confidence = result["score"]

        language_name = language_codes.get(
            language_code,
            language_code
        )

        # -------------------------------
        # Display Result
        # -------------------------------

        st.subheader("Detection Result")

        st.success(
            f"Detected Language: {language_name}"
        )

        st.write(
            f"Language Code: {language_code}"
        )

        st.write(
            f"Confidence: {confidence:.2%}"
        )

        # -------------------------------
        # Confidence Bar
        # -------------------------------

        st.progress(float(confidence))

# -------------------------------
# About Project
# -------------------------------

st.divider()

st.subheader("About this Project")

st.write(
    "This application uses a pre-trained language detection "
    "model from Hugging Face to identify the language of "
    "the provided text."
)

st.write("Technologies Used:")

st.write(
    "Python\n"
    "Streamlit\n"
    "Hugging Face Transformers\n"
    "XLM-RoBERTa"
)