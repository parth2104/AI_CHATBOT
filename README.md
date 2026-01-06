# 📄 RAG Application (PDF-based Question Answering)

A simple **Retrieval-Augmented Generation (RAG)** application built using **Streamlit**, **LangChain**, **Groq LLM**, and **HuggingFace embeddings**.
This app allows users to ask questions about a PDF document and receive answers grounded in the document content.

---

## 🚀 Features

* Load and process PDF documents
* Split documents into manageable text chunks
* Store embeddings in a vector database (Chroma)
* Retrieve relevant document context for each query
* Chat-based interface using Streamlit
* Cached vector store for fast performance
* Uses Groq’s `llama-3.1-8b-instant` model

---

## Tech Stack

* **Python**
* **Streamlit** – UI
* **LangChain** – RAG framework
* **Groq** – LLM inference
* **HuggingFace Sentence Transformers** – Embeddings
* **ChromaDB** – Vector store
* **PyPDFLoader** – PDF ingestion

---

## Project Structure

```
.
├── app.py
├── prompt/
│   └── prompt_template.py
├── documents/
│   └── NIPS-2017-attention-is-all-you-need-Paper.pdf
├── .env
├── requirements.txt
└── README.md

```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Make sure `sentence-transformers` is installed:

```bash
pip install sentence-transformers
```


## How It Works (RAG Flow)

1. PDF is loaded using `PyPDFLoader`
2. Text is split into chunks
3. Chunks are converted into embeddings
4. Embeddings are stored in Chroma vector DB
5. User query triggers similarity search
6. Relevant context is passed to the LLM
7. LLM generates an answer based on document context

---

### Notes

* Vector store is cached using `st.cache_resource` for efficiency
* Uses a **public embedding model**:

  ```
  sentence-transformers/all-MiniLM-L6-v2
  ```
* Designed for **learning and experimentation**

---

## Future Improvements

* Multiple PDF upload
* Source citation in answers
* Strict document-only answers
* Persistent vector storage
* Chat history-aware responses


---

## Support

If you find this project helpful, please ⭐ star the repository!
