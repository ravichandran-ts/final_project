# Import the requests library to handle HTTP requests
import requests 

import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
     # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers required for the API request 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create a dictionary with the text to be analyzed 
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header)

    # Send a POST request to the API with the text and headers
    #return response.text # Return the response text from the API

    # 1. Parse the JSON string into a Python dictionary
    # Parsing the JSON response from the API
    unformatted_response = json.loads(response.text)

    # 2. Extract the emotion dictionary 
    # Navigating: emotionPredictions -> first element [0] -> emotion
    emotions = unformatted_response['emotionPredictions'][0]['emotion']
    
    # 3. Format and print the scores
    print("Full Emotion Breakdown:")
    for emotion, score in emotions.items():
        print(f" - {emotion}: {score}")
    
    # 4. Identify the dominant emotion
    # Using the 'max' function with the dictionary's values as the key
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
    
    print("-" * 30)
    print(f"Dominant Emotion: {dominant_emotion} (Score: {dominant_score})")
    
    return dominant_emotion
