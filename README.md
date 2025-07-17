# 🧾 Legal Document Analyzer (RAG + LLM)

This project is a Legal Document Analyzer that allows users to upload legal files (PDFs, Word documents, EPUBs, scanned images, etc.), extract text, and ask queries using a Retrieval-Augmented Generation (RAG) pipeline with a custom LLM.

---

## 🔍 Features

- Extracts text from:
  - PDF (text & scanned)
  - DOCX / DOC files
  - EPUB files
  - Images (JPG, PNG, TIFF, etc.)
- OCR support for scanned documents and images
- Clean text preprocessing
- Plug-and-play text input for vector database / RAG
- Easily extensible via FastAPI or CLI
