'''Module to run emotion detector on a web server'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''Function to render index page from server'''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():
    '''Function to run emotion detector code on given input from server'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the data from response
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    output = "For the given statement, the system response is "
    for key, value in response.items():
        if key != 'dominiant_emotion':
            if key == 'sadness':
                output += "and '"+key+"': " + str(value) + "."
            else:
                output += "'"+key+"': " + str(value) + ","
    output += "The dominant emotion is " + response['dominant_emotion']
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
