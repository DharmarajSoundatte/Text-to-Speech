import streamlit as st
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

def text_to_speech(text, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    with NamedTemporaryFile(delete=False) as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name

st.title("Text-to-Speech App")

input_text = st.text_input("Enter the text you want to convert to speech:")
slow_speed = st.checkbox("Slow down speech")

if st.button("Convert to Speech"):
    if input_text:
        st.write("Converting text to speech...")
        audio_file = text_to_speech(input_text, slow=slow_speed)
        st.audio(audio_file, format='audio/mp3')
        playsound(audio_file, block=False)
    else:
        st.warning("Please enter some text!")
