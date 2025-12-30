import whisper
import os

# Load model once to save memory
model = whisper.load_model("tiny") 

def transcribe_audio(audio_path):
    """
    Transcribes audio file to text using Whisper.
    """
    if not os.path.exists(audio_path):
        return None
    
    result = model.transcribe(audio_path)
    return result["text"]