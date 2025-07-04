# 📚 RAG Chat App with File Upload (Streamlit + Groq + ChromaDB)

A lightweight Retrieval-Augmented Generation (RAG) app built with **Streamlit**, powered by **Groq's Mixtral-8x7B** LLM and **ChromaDB** for vector storage. Users can upload DOCX or PDF files, which are chunked and embedded into a vector database. The app then allows users to ask questions based on the document content and retrieves both the LLM-generated response and the top 5 relevant chunks.

---

## 🚀 Features

- ✅ Upload support for `.pdf` and `.docx` files
- ✅ Chunking of documents into 100-word windows with 20-word overlap
- ✅ Vector storage using **ChromaDB**
- ✅ Semantic search and retrieval of top 5 matching chunks
- ✅ LLM response generation using **Groq API** (Mixtral-8x7B model)
- ✅ Clean and interactive UI using **Streamlit**
- ✅ No dependency on OpenAI (uses HuggingFace embeddings)

---

## 🧠 Tech Stack

- [Streamlit](w)
- [Groq](w) (`mixtral-8x7b-32768`)
- [LangChain](w)
- [ChromaDB](w)
- [Sentence Transformers](w)
- [PyMuPDF](w) for PDF parsing
- [python-docx](w) for DOCX parsing

---

## 📁 Project Structure

rag_chat_app/
│
├── main.py # Streamlit UI + App logic
├── rag_class.py # RAG pipeline (embedding, vector store, querying)
├── llm.py # Groq LLM wrapper
├── utils.py # PDF/DOCX parsing and text chunking
├── requirements.txt # All required Python dependencies
└── README.md # Documentation



## 🛠️ Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/rag-chat-app.git
cd rag-chat-app


2.Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt


4.Run the app
streamlit run main.py
