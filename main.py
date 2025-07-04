import streamlit as st
from rag_class import RAGPipeline
from utils import read_pdf, read_docx

st.set_page_config(page_title="RAG Chat with File Upload")

st.title("📄 RAG Chat Interface")
st.write("Upload a DOCX or PDF file, ask questions, and get intelligent responses.")

# --- API Key Input ---
if "api_key" not in st.session_state:
    api_key = st.text_input("🔑 Enter your Groq API Key", type="password")
    if api_key:
        st.session_state.api_key = api_key
        st.success("✅ API Key set successfully!")

# --- Only show app after API key is set ---
if "api_key" in st.session_state:
    rag = RAGPipeline(st.session_state.api_key)

    uploaded_file = st.file_uploader("📤 Upload a DOCX or PDF file", type=["pdf", "docx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            text = read_pdf(uploaded_file)
        else:
            text = read_docx(uploaded_file)
        rag.process_text(text, uploaded_file.name)
        st.success("✅ File processed and stored in vector DB.")

    query = st.text_input("❓ Ask a question based on the uploaded document")

    if st.button("Submit") and query:
        response, docs = rag.query(query)
        st.subheader("💬 LLM Response")
        st.write(response)

        st.subheader("📚 Top 5 Retrieved Chunks")
        for i, doc in enumerate(docs):
            st.markdown(f"**Chunk {i+1}:**")
            st.write(doc.page_content)
