from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the data from response
    output = []
    for each in response:
        output.append("'"+each+"': " + str(response[each]))

    # Return a formatted string with the sentiment label and score
    return "For the given statement, the system response is {}, {}, {}, {}, {}. The dominant emotion is {}".format(output[0], output[1], output[2], output[3], output[4], response['dominant_emotion'])

    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)