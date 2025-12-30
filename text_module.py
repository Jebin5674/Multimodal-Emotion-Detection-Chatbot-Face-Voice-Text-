from transformers import pipeline

# Load the emotion classification pipeline
# Model: twitter-roberta-base-emotion (detects joy, optimism, anger, sadness)
classifier = pipeline("text-classification", 
                      model="cardiffnlp/twitter-roberta-base-emotion", 
                      return_all_scores=False)

def analyze_text_emotion(text):
    """
    Detects emotion from string using RoBERTa.
    """
    if not text:
        return "neutral"
    
    mapping = {
        "label_0": "anger",
        "label_1": "joy",
        "label_2": "optimism",
        "label_3": "sadness"
    }
    
    prediction = classifier(text)[0]
    label = prediction['label']
    return mapping.get(label, label)