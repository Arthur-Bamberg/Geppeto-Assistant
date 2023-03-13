import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.r = sr.Recognizer()

    def recognize_from_mic(self):
        with sr.Microphone() as source:
            print("Speak now...")
            audio = self.r.listen(source)
            text = self.recognize_audio(audio)
            return text

    def recognize_from_file(self, filename):
        with sr.AudioFile(filename) as source:
            audio = self.r.record(source)
            text = self.recognize_audio(audio, source)
            return text

    def recognize_audio(self, audio, source: str) -> str:
        try:
            text = self.r.recognize_google(audio, language='pt-BR')
            print("Recognized text:", text)
            return text
        except sr.UnknownValueError:
            print(f"Could not understand audio of {source}")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
