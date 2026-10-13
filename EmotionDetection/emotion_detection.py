"""Emotion detection application backed by the Watson NLP library.

The module sends the text to be analysed to the Watson NLP EmotionPredict
service and returns the emotion scores together with the dominant emotion.
"""

import json

import requests


def emotion_detector(text_to_analyse):
    """Detect the emotions expressed in the given text.

    Args:
        text_to_analyse (str): the text that has to be analysed.

    Returns:
        dict: the scores for anger, disgust, fear, joy and sadness together
        with the name of the dominant emotion. Every value is None when the
        text passed to the service is blank, that is when the Watson NLP
        service replies with status code 400.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=input_json, headers=header, timeout=10)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
