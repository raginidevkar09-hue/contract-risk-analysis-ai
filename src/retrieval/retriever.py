from pathlib import Path
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

DB_FOLDER = Path("data/vector_db")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

index = faiss.read_index(str(DB_FOLDER / "contracts.index"))

with open(DB_FOLDER / "metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)


def retrieve(query, top_k=5):
    # Convert query to embedding
    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    ).astype("float32")

    scores, indices = index.search(
        np.array([query_embedding]),
        top_k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):
        results.append({
            "score": float(score),
            "document": metadata[idx]["document_name"],
            "section": metadata[idx]["section"],
            "text": metadata[idx]["text"]
        })

    return results


if __name__ == "__main__":

    query = input("Enter your question: ")
    top_k = int(input("Enter Top-k value: "))
    results = retrieve(query, top_k)

    print("\nRetrieved Chunks:\n")

    for i, result in enumerate(results, start=1):

        print("=" * 60)
        print(f"Rank     : {i}")
        print(f"Score    : {result['score']:.4f}")
        print(f"Document : {result['document']}")
        print(f"Section  : {result['section']}")
        print("Text:")
        print(result["text"])