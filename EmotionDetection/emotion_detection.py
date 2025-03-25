import requests  
import json 

def emotion_detector(text_to_analyse):
    #Create output dict
    out = {}

    #Get data from Watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    text_obj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = text_obj, headers=header)

    #Convert response text into a json object
    json_response = json.loads(response.text)

    #Populate output dict with extracted emotions and corresponding values
    for each in json_response['emotionPredictions'][0]['emotion']:
        out[each] = json_response['emotionPredictions'][0]['emotion'][each]
    out['dominant_emotion'] = max(out, key=out.get)
    return out

