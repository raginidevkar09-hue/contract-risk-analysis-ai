from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def embed_text(text: str):
    return model.encode(
        text,
        normalize_embeddings=True
    ).astype("float32")


def cosine_similarity(a, b):
    return float(np.dot(a, b))