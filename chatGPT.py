import openai
import os
from dotenv import load_dotenv


class ChatGPT:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.environ["OPENAI_API_KEY"]

    @staticmethod
    def generate_text(prompt, model='text-davinci-003', max_tokens=100, n=1, stop=None, temperature=0.5):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )

        return response.choices[0].text
