import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse : str):
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json=data, headers=HEADER)
    
    status = response.status_code
    if(400 == status):
        predicitions = {}

        predicitions['anger'] = None
        predicitions['disgust'] = None
        predicitions['fear'] = None
        predicitions['joy'] = None
        predicitions['sadness'] = None
        predicitions['dominant_emotion'] = None

        return predicitions

    predicitions = json.loads(response.text)['emotionPredictions'][0]['emotion']

    max_score = 0
    dominant_emotion = ''
    for emotion in predicitions:
        score = predicitions[emotion]

        if(score > max_score):
            max_score = score
            dominant_emotion = emotion
    predicitions['dominant_emotion'] = dominant_emotion

    return predicitions
