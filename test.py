import requests

# Set up the URL for the POST request
url = "http://localhost:5000/audio-to-text"

# Set up the audio file as a dictionary with key 'audio' and value being the audio file object
audio_file = open("/home/bamberg/Downloads/audio.wav", "rb")
audio_dict = {'audio': audio_file}

# Make the POST request with the audio file
response = requests.post(url, files=audio_dict)

# Get the text from the response
text = response.text

# Print the text
print(text)
