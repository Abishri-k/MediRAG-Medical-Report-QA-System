# 🩺 MediRAG

### AI-Powered Medical Report Question Answering System using Retrieval-Augmented Generation (RAG)

MediRAG is a Retrieval-Augmented Generation (RAG) application that enables users to upload medical reports in PDF format and ask questions in natural language. The system retrieves the most relevant information from the uploaded report using semantic search and generates context-aware responses with the Groq Llama 3 Large Language Model.

Developed using **Python**, **Streamlit**, **LangChain**, **FAISS**, **Sentence Transformers**, and the **Groq API**, the application demonstrates the integration of Large Language Models with vector-based information retrieval for document question answering.

---

## ✨ Features

* Upload medical reports in PDF format
* Extract text from PDF documents
* Split documents into semantic chunks
* Generate embeddings using Sentence Transformers
* Store embeddings in a FAISS vector database
* Retrieve relevant document context
* Generate AI-powered answers using Groq Llama 3
* Interactive Streamlit-based user interface

---

## 🛠️ Tech Stack

| Technology            | Usage               |
| --------------------- | ------------------- |
| Python 3.11           | Backend Development |
| Streamlit             | Web Interface       |
| LangChain             | RAG Pipeline        |
| PyPDF                 | PDF Processing      |
| Sentence Transformers | Text Embeddings     |
| FAISS                 | Vector Database     |
| Groq API (Llama 3)    | Answer Generation   |
| Git & GitHub          | Version Control     |

---

## 📁 Project Structure

```text
MediRAG-Medical-Report-QA-System
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── utils/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── rag.py
│
├── screenshots/
└── sample_reports/
```

---

## 🚀 Getting Started

Clone the repository.

```bash
git clone https://github.com/Abishri-k/MediRAG-Medical-Report-QA-System.git
```

Navigate to the project.

```bash
cd MediRAG-Medical-Report-QA-System
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application.

```bash
streamlit run app.py
```

---

## 🔄 Workflow

```text
PDF Upload
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Embedding Generation
     │
     ▼
FAISS Vector Store
     │
     ▼
Semantic Retrieval
     │
     ▼
Groq Llama 3
     │
     ▼
Generated Answer
```

---

## 📸 Application Preview

Add screenshots of:

* Home Page
* PDF Upload
* Dashboard
* AI Generated Answer

---

## 🔮 Future Scope

* OCR support for scanned reports
* Multi-language support
* Cloud deployment
* Conversation history
* User authentication
* Support for additional document formats

## 📄 License

This project was developed for academic and educational purposes as part of the **Software Development Using Generative AI** course.
