Multimodal Emotion Detection Chatbot (Face, Voice & Text)
![alt text](https://img.shields.io/badge/Python-3.9+-blue.svg)

![alt text](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)

![alt text](https://img.shields.io/badge/PyTorch-1.x-red.svg)

![alt text](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
📝 Project Overview
This project is a sophisticated Multimodal AI Chatbot designed to detect and respond to human emotions across three primary channels: Face, Voice, and Text. By fusing computer vision, audio processing, and natural language understanding, the system creates a holistic emotional profile of the user to enable more empathetic and intelligent human-computer interactions.
Developed using Deep Learning architectures, the chatbot doesn't just process what you type—it understands how you look and how you sound, making it a true "Affective Computing" application.
✨ Key Features
Facial Emotion Detection: Uses DeepFace to analyze real-time snapshots, identifying expressions such as happiness, sadness, anger, and surprise.
Vocal Transcription & Analysis: Leverages OpenAI Whisper to convert speech to text and analyze the underlying emotional tone.
Textual Sentiment Analysis: Utilizes a fine-tuned RoBERTa model to extract nuanced emotional cues from text input.
Context-Aware Conversational AI: Integrated with DialoGPT to maintain interaction history and provide responses that adapt to the detected emotional state.
Scalable Deployment: Built with Streamlit and TensorFlow, providing a user-friendly, interactive web interface.
🛠️ Tech Stack & AI Models
Domain	Model/Technology	Description
Face	DeepFace (VGG-Face)	Real-time facial expression recognition
Voice	OpenAI Whisper	High-accuracy speech-to-text processing
Text	RoBERTa-Base	Semantic emotion classification
Chat Engine	Microsoft DialoGPT	Generative conversational transformer
Frontend	Streamlit	Web-based interactive dashboard
Backend	Python / TensorFlow / PyTorch	Deep Learning framework support
📐 System Architecture
Capture: The system takes a webcam snapshot, an audio recording, and a text prompt from the user.
Analysis:
The Face Module processes the image for visual emotions.
The Voice Module transcribes audio to text.
The Text Module evaluates the sentiment of both transcribed and typed text.
Context Fusion: The emotional data is combined to create a "contextual prompt."
Response: DialoGPT processes the context and generates a human-like, empathetic reply.
📁 Project Structure
code
Text
├── app.py              # Main Streamlit application and UI logic
├── face_module.py      # Facial emotion analysis using DeepFace
├── voice_module.py     # Speech-to-text processing using Whisper
├── text_module.py      # Sentiment analysis using RoBERTa
├── chat_engine.py      # Conversational response generation via DialoGPT
├── requirements.txt    # List of required Python libraries
└── temp_audio.wav      # Temporary storage for voice processing
🚀 Installation & Setup
1. Prerequisites
Python 3.9 or higher.
FFmpeg must be installed on your system for audio processing:
Windows: choco install ffmpeg
Mac: brew install ffmpeg
Linux: sudo apt install ffmpeg
2. Clone the Repository
code
Bash
git clone https://github.com/your-username/multimodal-emotion-chatbot.git
cd multimodal-emotion-chatbot
3. Install Dependencies
code
Bash
pip install -r requirements.txt
4. Run the Application
code
Bash
streamlit run app.py
🎮 How to Use
Grant Permissions: Allow the browser to access your camera and microphone.
Visual Input: Take a snapshot using the sidebar camera component.
Audio Input: Record a short voice clip to analyze your tone.
Text Input: Type your message in the chat box.
Interaction: The assistant will display the detected emotions from all three sources and reply based on your current mood.
Developed by Jebin
Deep Learning – Multimodal AI Project
