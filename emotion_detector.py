# Emotion Detector Agent – CrewAI
# Detects emotional tone based on keywords in text

def detect_emotion(text):
    text = text.lower()

    emotion_keywords = {
        "hopeless": ["nothing matters", "pointless", "empty", "no purpose"],
        "anxious": ["anxious", "worried", "nervous", "stressed", "panicking"],
        "exhausted": ["tired", "burned out", "drained", "fatigued"],
        "sad": ["sad", "down", "depressed", "low"],
        "angry": ["angry", "furious", "mad", "rage"],
        "lonely": ["lonely", "alone", "isolated"]
    }

    for emotion, keywords in emotion_keywords.items():
        for word in keywords:
            if word in text:
                return emotion

    return "neutral"
