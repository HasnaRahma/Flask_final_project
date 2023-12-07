from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Extract values
    emotion_values = ', '.join(f"'{key}': {value}" for key, value in response.items() if key != 'dominant_emotion')
    dominant_emotion = response['dominant_emotion']
    # Format the string
    output_string = f"For the given statement, the system response is {emotion_values}. The dominant emotion is {dominant_emotion}."
    return output_string

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)