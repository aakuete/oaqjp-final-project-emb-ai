from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emot = response['dominant_emotion']
    if dominant_emot == None:
        return "Invalid text! Please try again!"
    else:
        scores = {k: v for k, v in response.items() if k != "dominant_emotion"}
        system_response = ", ".join([f"'{k}': {v}" for k, v in scores.items()])
        return f"For the given statement, the system response is {system_response}. The dominant emoition is {dominant_emot}."

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)