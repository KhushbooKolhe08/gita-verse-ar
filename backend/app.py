from fastapi import FastAPI
from pydantic import BaseModel

from rag.loader import load_gita_data
from rag.chunker import simple_chunk_text
from rag.embeddings import create_embeddings
from rag.retriever import retrieve_relevant_chunks
from rag.generator import generate_answer

# Initialize app
app = FastAPI()

# Request schema
class QueryRequest(BaseModel):
    question: str


# Load everything ONCE (important for performance)
print("Initializing RAG system...")

text = load_gita_data()
chunks = simple_chunk_text(text)
index, stored_chunks = create_embeddings(chunks)

print("RAG system ready!")


@app.post("/ask")
def ask_question(request: QueryRequest):
    import traceback

    try:
        query = request.question

        retrieved = retrieve_relevant_chunks(query, index, stored_chunks)

        print("Retrieved chunks:", len(retrieved))

        answer = generate_answer(query, retrieved)

        return {
            "answer": answer,
            "context": retrieved
        }

    except Exception as e:
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }