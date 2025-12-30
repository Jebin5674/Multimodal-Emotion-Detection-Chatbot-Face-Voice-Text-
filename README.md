Multimodal Emotion AI Chatbot
![alt text](https://img.shields.io/badge/Python-3.9+-blue.svg)

![alt text](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)

![alt text](https://img.shields.io/badge/PyTorch-1.x-red.svg)

![alt text](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
An advanced Affective Computing framework that synchronizes visual, auditory, and textual data to perceive human emotions. Unlike standard chatbots, this system "sees" facial expressions, "hears" vocal sentiment, and "understands" language context to provide emotionally resonant interactions.
✨ Key Features
🎥 Facial Emotion Recognition: Real-time analysis of micro-expressions using DeepFace.
🎙️ Vocal Sentiment Analysis: High-accuracy speech transcription via OpenAI Whisper combined with semantic emotion mapping.
✍️ Semantic Text Analysis: Nuanced emotion detection (Joy, Sadness, Anger, etc.) using a fine-tuned RoBERTa Transformer.
🧠 Contextual Conversation: Empathetic, history-aware responses powered by DialoGPT.
💻 Interactive Dashboard: A clean, user-friendly interface built with Streamlit.
🛠️ Tech Stack
Component	Technology
Language	Python 3.9+
Face Detection	DeepFace (VGG-Face / TensorFlow)
Speech-to-Text	OpenAI Whisper
Text Emotion	RoBERTa (cardiffnlp/twitter-roberta-base-emotion)
Chat Engine	DialoGPT-medium (Microsoft)
Frontend	Streamlit
📐 System Architecture
The system follows a Late Fusion multimodal approach:
Input Layer: Captures webcam snapshots, audio recordings, and text input.
Processing Layer: Three parallel AI models extract emotional features.
Fusion Layer: Emotional context is injected into a specialized prompt.
Interaction Layer: DialoGPT generates a response tailored to the detected mood.
📁 Project Structure
code
Text
multimodal-emotion-ai/
├── app.py              # Main Streamlit UI & Application Logic
├── face_module.py      # Face emotion detection (DeepFace)
├── voice_module.py     # Audio transcription (Whisper)
├── text_module.py      # Text emotion detection (RoBERTa)
├── chat_engine.py      # Conversational AI (DialoGPT)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
🚀 Installation & Setup
1. Prerequisites
Ensure you have Python 3.9 or higher.
Install FFmpeg (required for audio processing):
Windows: choco install ffmpeg
Mac: brew install ffmpeg
Linux: sudo apt install ffmpeg
2. Clone the Repository
code
Bash
git clone https://github.com/your-username/Sentience-X.git
cd Sentience-X
3. Install Dependencies
code
Bash
pip install -r requirements.txt
🎮 How to Use
Run the App:
code
Bash
streamlit run app.py
Interact:
Visuals: Grant camera access and click "Take Snapshot."
Audio: Click "Start Recording," speak, and click "Stop."
Chat: Type your message in the chat box.
Observe: The bot will analyze all three inputs to understand your emotional state and respond accordingly.
🤝 Contributing
Contributions are welcome![1] If you'd like to improve the emotion fusion logic or UI, please fork the repo and create a pull request.
