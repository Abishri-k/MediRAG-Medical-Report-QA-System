import faiss
import numpy as np


def create_faiss_index(embeddings):

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


def search_similar_chunks(index, query_embedding, chunks, top_k=2):

    query_embedding = np.array(query_embedding).astype("float32")

    k = min(top_k, len(chunks))

    distances, indices = index.search(query_embedding, k)

    retrieved_chunks = []

    for idx in indices[0]:
        if idx < len(chunks):
            retrieved_chunks.append(chunks[idx])

    return retrieved_chunks