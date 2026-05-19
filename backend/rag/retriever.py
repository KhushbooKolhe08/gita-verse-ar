import numpy as np
from sentence_transformers import SentenceTransformer

# Load same model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_relevant_chunks(query, index, chunks, top_k=3):
    """
    Retrieve top_k most relevant chunks for a given query
    """

    # Convert query to embedding
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS index
    distances, indices = index.search(query_embedding, top_k)

    # Get relevant chunks
    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results 