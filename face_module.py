import cv2
from deepface import DeepFace
import numpy as np

def analyze_face(image_array):
    """
    Analyzes emotion from an image array (numpy).
    """
    try:
        # DeepFace expects BGR for OpenCV
        results = DeepFace.analyze(image_array, actions=['emotion'], enforce_detection=False)
        # DeepFace returns a list if multiple faces are found
        return results[0]['dominant_emotion']
    except Exception as e:
        return f"Error: {str(e)}"