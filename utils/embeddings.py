from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    """
    Generate embeddings for text chunks.
    """
    embeddings = model.encode(chunks)
    return embeddings

def generate_query_embedding(question):
    """
    Generate an embedding for the user's question.
    """
    return model.encode([question])