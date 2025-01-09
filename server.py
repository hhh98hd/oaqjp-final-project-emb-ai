"""This module is the server of the project."""

import json

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET'])
def index():
    """Return the home page.

    Returns: The index.html file.
    """

    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def setiment_analyze():
    """Receive a text and return the emotion detected in it.

    Returns:
        Dict: A dictionay with proabilities of each emotion and the dominant emotion.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    res = emotion_detector(text_to_analyze)
    dominant_emotion = res['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!.'

    res_str = (
        'For the given statement, the system response is ' + json.dumps(res) + '.\n'
        'The dominant emotion is ' + dominant_emotion + '.'
    )

    return res_str

app.run(port=5000, debug=False)
