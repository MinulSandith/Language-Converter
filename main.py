import streamlit as st
from googletrans import Translator
translator = Translator()

with open ("style.css") as f :
    st.markdown( f'<style>{f.read()}</style>',unsafe_allow_html=True)
title=st.title("Language Translator")
col1,col2=st.columns(2)
input = col1.text_area('Text', '''Enter your text here''')
langconvert = col2.selectbox(
     'To what language',
     ["English", 'Sinhala','Chinese (traditional)','Tamil','Bengali','Spanish','Gujarati','French'])

result = translator.translate(input,dest=langconvert)
st.code(result.text)
button=col1.button("Translate")



#from win32com.client import Dispatch

#speak = Dispatch("SAPI.SpVoice").Speak

#speak("Hello Bro")