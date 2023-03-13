from flask import Flask, request
from SpeechRecognizer import SpeechRecognizer
from chatGPT import ChatGPT

app = Flask(__name__)

recognizer = SpeechRecognizer()


@app.route('/audio-to-text', methods=['POST'])
def audio_to_text():
    # Get the audio file from the request
    audio_file = request.files['audio']

    # Convert the audio to text using the SpeechRecognizer object
    text = recognizer.recognize_from_file(audio_file)

    response = ChatGPT().generate_text("Say hi for a post request")

    # Return the text as a response
    return response
