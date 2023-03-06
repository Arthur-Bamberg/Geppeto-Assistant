import SpeechRecognizer

sr = SpeechRecognizer()

text = sr.recognize_from_mic()
print(text)
