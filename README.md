# Language Converter

A simple [Streamlit](https://streamlit.io/) web app that translates text between English, Sinhala, Chinese (Traditional), Tamil, Bengali, Spanish, Gujarati, and French.

## Features

- Paste or type text into a text box
- Pick a target language from a dropdown
- Click **Translate** to get the translated text back
- Copy the result straight from the output box

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [deep-translator](https://github.com/nidhaloff/deep-translator) — Google Translate client
- Custom CSS (`style.css`) for a gradient background

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/MinulSandith/Language-Converter.git
cd Language-Converter
pip install -r requirements.txt
```

### Run

```bash
streamlit run main.py
```

The app opens at `http://localhost:8501` by default.

## How to Use

1. **Enter your text** in the text field.
2. **Select a language** you want to translate into from the dropdown.
3. **Click Translate.**
4. **Read or copy** the translated text from the output box.

## Project Structure

```
.
├── main.py            # Streamlit app entry point
├── requirements.txt    # Python dependencies
└── style.css           # Custom styling (animated gradient background, fonts)
```

## Notes

- This project previously depended on `googletrans==3.1.0a0`, which is unmaintained and fails to build on modern Python/setuptools versions. It was replaced with `deep-translator`, which is actively maintained and uses the same underlying Google Translate endpoint.
- Translation requires outbound internet access to `translate.google.com`; the app will show an on-screen error if a translation request fails instead of crashing.

## Contributing

Bug reports and suggestions for improvements are welcome — please open an issue or pull request.
