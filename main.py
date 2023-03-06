from SpeechRecognizer import SpeechRecognizer

sr = SpeechRecognizer()

text = sr.recognize_from_mic()
print(text)


from flask import Flask, request
import requests

app = Flask(__name__)

# Define the ChatGPT API endpoint
chatgpt_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Define your OpenAI API key
openai_key = "YOUR_OPENAI_API_KEY"

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's message from the request data
    message = request.form['message']

    # Set the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_key}'
    }

    # Set the request data
    data = {
        'prompt': f'{message}\nAI:',
        'temperature': 0.7,
        'max_tokens': 50
    }

    # Send a POST request to the ChatGPT API endpoint
    response = requests.post(chatgpt_endpoint, headers=headers, json=data)

    # Get the AI's response from the API response
    ai_response = response.json()['choices'][0]['text'].strip()

    # Return the AI's response as the API response
    return {'message': ai_response}

if __name__ == '__main__':
    app.run()
