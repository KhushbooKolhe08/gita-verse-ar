from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Convert text chunks into embeddings and store in FAISS
    """

    print("Creating embeddings...")

    # Convert text → vectors
    embeddings = model.encode(chunks)

    # Convert to numpy array
    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings
    index.add(embeddings)

    print(f"Stored {len(chunks)} chunks in FAISS index")

    return index, chunks