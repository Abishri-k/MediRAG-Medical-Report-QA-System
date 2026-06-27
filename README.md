# MediRAG: AI-Powered Medical Report Question Answering System Using Retrieval-Augmented Generation (RAG)

## Overview

MediRAG is an AI-powered Medical Report Question Answering System that leverages the Retrieval-Augmented Generation (RAG) framework to provide context-aware answers from uploaded medical reports. The application enables users to upload PDF medical documents and interact with them through natural language questions.

The system combines semantic document retrieval with the Groq Llama 3 Large Language Model to generate accurate and relevant responses based solely on the uploaded medical report. By integrating modern Natural Language Processing (NLP) techniques with vector search, MediRAG improves information accessibility while minimizing AI hallucinations.

This project was developed as part of the **Software Development Using Generative AI** course.

---

# Objectives

- Develop an AI-powered question answering system for medical reports.
- Extract textual information from PDF documents.
- Generate semantic embeddings using Sentence Transformers.
- Store document embeddings using the FAISS vector database.
- Retrieve contextually relevant information using semantic similarity search.
- Generate accurate answers using the Groq Llama 3 Large Language Model.
- Provide an intuitive and interactive Streamlit-based user interface.

---

# Key Features

- Upload medical reports in PDF format
- Automatic PDF text extraction
- Recursive text chunking using LangChain
- Semantic embedding generation
- High-speed vector search using FAISS
- Retrieval-Augmented Generation (RAG)
- Context-aware AI responses
- Interactive Streamlit web application
- Modular and scalable project architecture

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| Streamlit | User Interface |
| PyPDF | PDF Text Extraction |
| LangChain | Text Chunking and RAG Pipeline |
| Sentence Transformers | Embedding Generation |
| FAISS | Vector Database |
| Groq API (Llama 3) | Large Language Model |
| Git & GitHub | Version Control |

---

# System Architecture

```
                User
                  │
                  ▼
         Streamlit Web Interface
                  │
                  ▼
         Upload Medical Report
                  │
                  ▼
          PDF Text Extraction
                  │
                  ▼
      Recursive Text Chunking
                  │
                  ▼
      Sentence Transformer Model
                  │
                  ▼
        FAISS Vector Database
                  │
                  ▼
       Semantic Similarity Search
                  │
                  ▼
        Groq Llama 3 API
                  │
                  ▼
      AI Generated Response
```

---

# Project Structure

```
MediRAG-Medical-Report-QA-System
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── utils
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── rag.py
│
├── uploads
│
├── screenshots
│
└── sample_reports
```

---

# Installation Guide

## Clone the Repository

```bash
git clone https://github.com/Abishri-k/MediRAG-Medical-Report-QA-System.git
```

## Navigate to the Project Directory

```bash
cd MediRAG-Medical-Report-QA-System
```

## Create a Virtual Environment

```bash
python -m venv .venv
```

## Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Required Packages

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a file named `.env`

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

## Run the Application

```bash
streamlit run app.py
```

---

# Application Workflow

1. Upload a PDF medical report.
2. Extract text from the uploaded document.
3. Split the extracted text into smaller overlapping chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in the FAISS vector database.
6. Accept user questions in natural language.
7. Retrieve the most relevant document chunks.
8. Generate context-aware answers using Groq Llama 3.
9. Display the response through the Streamlit interface.

---

# Screenshots

### Home Screen

*(Add Home Screen Screenshot)*

### PDF Upload

*(Add Upload Screen Screenshot)*

### Dashboard

*(Add Dashboard Screenshot)*

### AI Generated Response

*(Add Response Screenshot)*

---

# Future Enhancements

- Optical Character Recognition (OCR) for scanned medical reports
- Support for DOCX and image-based reports
- Cloud deployment
- User authentication
- Chat history
- Multi-language support
- Medical knowledge base integration
- Mobile-friendly interface

---

# Academic Information

**Course:** Software Development Using Generative AI

**Project Title:** MediRAG: AI-Powered Medical Report Question Answering System Using Retrieval-Augmented Generation (RAG)

---

# Author

**Abishri K**

B.Tech Electronics and Communication Engineering

Specialization: Biomedical Engineering

Vellore Institute of Technology (VIT)

---

# License

This project has been developed solely for academic and educational purposes as part of the Software Development Using Generative AI course at VIT University.
