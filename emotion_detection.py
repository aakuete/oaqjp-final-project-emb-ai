import requests, json

# Function to run emotion detection
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    # Extracting and storing emotions into a dictionary called emotion  
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    # Finding the dominant emotion based on the emotion with highest score
    dominant_emotion = max(emotion, key=emotion.get)
    # Storing the dominant emotion into emotion dictionary
    emotion['dominant_emotion'] = dominant_emotion
    return emotion