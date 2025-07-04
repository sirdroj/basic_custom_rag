from langchain.schema import HumanMessage
from llm import get_groq_llm

class RAGPipeline:
    def __init__(self,api_key=None):
        self.retriever = None
        self.llm = get_groq_llm(api_key)
        self.docs = []

    def process_text(self, text, source_name):
        from langchain.vectorstores import Chroma
        from langchain.embeddings import HuggingFaceEmbeddings
        from langchain.docstore.document import Document

        from utils import chunk_text
        chunks = chunk_text(text)
        docs = [Document(page_content=chunk, metadata={"source": source_name}) for chunk in chunks]
        self.vectorstore = Chroma.from_documents(docs,HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 5})

    def query(self, question):
        if not self.retriever:
            return "No document uploaded yet.", []
        docs = self.retriever.get_relevant_documents(question)
        context = "\n\n".join([doc.page_content for doc in docs])
        full_prompt = f"Use the following context to answer the question:\n\n{context}\n\nQuestion: {question}"
        answer = self.llm(full_prompt)
        return answer, docs
