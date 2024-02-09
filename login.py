
import streamlit as st
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

def text_to_speech(text, language='en', speed=1, slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.speed = speed
    with NamedTemporaryFile(delete=False) as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name

def login(username, password):
    return username == 'dharmaraj' and password == 'soundatte'

st.title("Text-to-Speech App")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if login(username, password):
    input_text = st.text_input("Enter the text you want to convert to speech:")
    slow_speed = st.checkbox("Slow down speech")
    speed = st.slider("Adjust Speed", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

    if st.button("Convert to Speech"):
        if input_text:
            st.write("Converting text to speech...")
            audio_file = text_to_speech(input_text, slow=slow_speed, speed=speed)
            st.audio(audio_file, format='audio/mp3')
            playsound(audio_file, block=False)
        else:
            st.warning("Please enter some text!")
else:
    st.error("Incorrect username or password. Please try again.")
