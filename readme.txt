# RAG Streamlit App with File Upload

## Features:
- Upload DOCX or PDF files
- Chunk documents into 100-word chunks with 20-word overlap
- Store chunks in Chroma DB
- Ask questions based on uploaded docs
- View LLM response and top 5 retrieved document chunks

## Setup
1. Install requirements: pip install -r requirements.txt
2. Set your Groq API key as an environment variable: GROQ_API_KEY=your_key_here
3. Run the app: streamlit run main.py
