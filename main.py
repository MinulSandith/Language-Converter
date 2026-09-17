import streamlit as st
from deep_translator import GoogleTranslator

LANGUAGES = {
    "English": "en",
    "Sinhala": "si",
    "Chinese (traditional)": "zh-TW",
    "Tamil": "ta",
    "Bengali": "bn",
    "Spanish": "es",
    "Gujarati": "gu",
    "French": "fr",
}

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Language Translator")
col1, col2 = st.columns(2)

input_text = col1.text_area("Text", "Enter your text here")
target_language = col2.selectbox("To what language", list(LANGUAGES.keys()))

if col1.button("Translate"):
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            result = GoogleTranslator(
                source="auto", target=LANGUAGES[target_language]
            ).translate(input_text)
            st.code(result)
        except Exception as e:
            st.error(f"Translation failed: {e}")
