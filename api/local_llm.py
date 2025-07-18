import requests

class LocalLLM:
    def __init__(self, model="mistral:7b-instruct-v0.3-q4_0", url="http://localhost:11434/api/generate"):
        self.model = model
        self.url = url

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()  # Raise error if request failed
        data = response.json()
        return data.get('response', '')
