from api.text_extractor import TextExtractor
from api.local_llm import LocalLLM

class TextExtractionApp:
    def __init__(self, tesseract_cmd_path=None, llm_model=None, llm_url=None):
        self.extractor = TextExtractor(tesseract_cmd_path=tesseract_cmd_path)
        self.llm = LocalLLM(model=llm_model or "mistral:7b-instruct-v0.3-q4_0", url=llm_url or "http://localhost:11434/api/generate")

    def run(self):
        file_path = input("Enter the path to the file: ")
        extracted_text = self.extractor.extract_text(file_path)
        print("\n--- Extracted Text ---")
        print(extracted_text)

        prompt = input("\nEnter the prompt for the LLM: ")
        response = self.llm.generate(prompt)
        print("\n--- LLM Response ---")
        print(response)


if __name__ == "__main__":
    app = TextExtractionApp(tesseract_cmd_path=r"C:/Program Files/Tesseract-OCR/tesseract.exe")
    app.run()
