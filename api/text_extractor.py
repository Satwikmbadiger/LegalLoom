import os
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from docx import Document
from ebooklib import epub
from ebooklib import ITEM_DOCUMENT
from bs4 import BeautifulSoup
from PIL import Image

class TextExtractor:
    def __init__(self, tesseract_cmd_path=None):
        if tesseract_cmd_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path

    def extract_text(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()

        try:
            if ext == ".pdf":
                return self._extract_pdf_text(file_path)
            elif ext in [".doc", ".docx"]:
                return self._extract_doc_text(file_path)
            elif ext == ".epub":
                return self._extract_epub_text(file_path)
            elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
                return self._extract_image_text(file_path)
            else:
                return f"Unsupported file extension: {ext}"
        except Exception as e:
            return f"Error extracting text: {str(e)}"

    def _extract_pdf_text(self, file_path):
        # Try pdfplumber first for text PDFs
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        if text.strip():
            return text

        # Fallback to OCR for scanned PDFs
        pages = convert_from_path(file_path)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page) + "\n"
        return text

    def _extract_doc_text(self, file_path):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    def _extract_epub_text(self, file_path):
        book = epub.read_epub(file_path)
        text = ""
        for item in book.get_items_of_type(ITEM_DOCUMENT):
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text() + "\n"
        return text

    def _extract_image_text(self, file_path):
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)

"""
if __name__ == "__main__":
    extractor = TextExtractor(tesseract_cmd_path=r"C:/Program Files/Tesseract-OCR/tesseract.exe")
    file_path = "test_data/Land Lease Agreement.pdf"  # Change to your file
    extracted_text = extractor.extract_text(file_path)
    print(extracted_text)
    """