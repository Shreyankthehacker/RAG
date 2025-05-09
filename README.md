# 🔍 RAG System for PDFs and Image Summarization

A Retrieval-Augmented Generation (RAG) system built using LangChain, Chroma, Hugging Face Embeddings, and Gemini Pro/Gemini Flash for robust question-answering from PDFs, images, and image-based PDFs.

---

## 🚀 Features

- ✅ **Supports both text-based PDFs and image-based PDFs**
- 🖼️ **Image summarization using Gemini Vision (no OCR involved)**
- 🧠 **Embeds and stores content using Hugging Face + ChromaDB**
- 🔁 **Multi-query retrieval for broader semantic coverage**
- 🤖 **Fallback mechanism for hallucination detection and safe responses**

---

## 🧩 Architecture

1. **Document Router**
   - Routes uploaded files to appropriate handlers:
     - `text-based PDFs` → processed via `PyPDFLoader`
     - `image-based PDFs` → each page treated as an image and summarized using Gemini
     - `images` → directly summarized via Gemini Vision API

2. **Image Handler**
   - Converts image to base64 and sends it to Gemini for structured summarization.
   - Avoids OCR; relies on **Gemini Vision's visual understanding** for exhaustive output.
   - Output is saved and stored in the vector store.

3. **Vector Store**
   - Uses **Hugging Face Embeddings**
   - Stores document and image summaries in **Chroma DB**

4. **Multi-Query Retriever**
   - Automatically generates multiple semantically diverse queries from user input.
   - Improves context retrieval and reduces missed information.

5. **Answer Generator**
   - Uses Gemini Pro/Flash to generate answers based on retrieved content.

6. **Fallback Node**
   - Checks if the answer is well-grounded.
   - If hallucination or insufficient context is detected, provides a polite fallback message.

---

## 🖼 Architecture Diagram

![Architecture](https://github.com/Shreyankthehacker/RAG/raw/main/ImageRag/arch.png)


## 📽 Demo

[![Watch the Demo Video](https://img.youtube.com/vi/guTuc0DiNgQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=guTuc0DiNgQ)

