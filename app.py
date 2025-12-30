import streamlit as st
import cv2
import numpy as np
from PIL import Image
from streamlit_mic_recorder import mic_recorder
import os

# Import custom modules
from face_module import analyze_face
from voice_module import transcribe_audio
from text_module import analyze_text_emotion
from chat_engine import generate_response

st.set_page_config(page_title="Multimodal Emotion AI", layout="wide")
st.title("🤖 Multimodal Emotion Chatbot")

# Initialize Session States
if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for Multimodal Inputs
with st.sidebar:
    st.header("Input Channels")
    
    # 1. Camera Input
    img_file = st.camera_input("Take a snapshot for face emotion")
    
    # 2. Audio Input
    st.write("Record your voice:")
    audio_record = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", key='recorder')

# Main Layout: Two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Emotion Analysis")
    face_emo = "Not detected"
    voice_emo = "Not detected"
    
    # Process Face
    if img_file:
        img = Image.open(img_file)
        img_array = np.array(img)
        face_emo = analyze_face(img_array)
        st.info(f"Facial Emotion: **{face_emo}**")

    # Process Voice
    if audio_record:
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_record['bytes'])
        
        transcribed_text = transcribe_audio("temp_audio.wav")
        voice_emo = analyze_text_emotion(transcribed_text)
        st.info(f"Voice Transcription: *{transcribed_text}*")
        st.info(f"Voice Sentiment: **{voice_emo}**")

with col2:
    st.subheader("Chatbot Interaction")
    
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Say something..."):
        # Detect text emotion
        text_emo = analyze_text_emotion(prompt)
        
        # Combine Context
        full_context = f"[Context: User looks {face_emo} and sounds {voice_emo}]. User says: {prompt}"
        
        # Add user message to UI
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Response
        with st.chat_message("assistant"):
            response, history = generate_response(prompt, st.session_state.chat_history_ids)
            st.session_state.chat_history_ids = history
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.caption(f"Detected Emotion: {text_emo}")