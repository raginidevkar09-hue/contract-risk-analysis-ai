from pathlib import Path
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi

DB_FOLDER = Path("data/vector_db")

# Load embedding model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Load FAISS index
index = faiss.read_index(str(DB_FOLDER / "contracts.index"))

# Load metadata
with open(DB_FOLDER / "metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

# Build BM25 corpus
documents = [item["text"] for item in metadata]
tokenized_docs = [doc.lower().split() for doc in documents]

bm25 = BM25Okapi(tokenized_docs)


def hybrid_search(query, top_k=5):

    # ---------- Semantic Search ----------
    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    ).astype("float32")

    semantic_scores, semantic_indices = index.search(
        np.array([query_embedding]),
        len(metadata)
    )

    semantic_score_map = {}

    for score, idx in zip(semantic_scores[0], semantic_indices[0]):
        semantic_score_map[idx] = float(score)

    # ---------- Keyword Search ----------
    keyword_scores = bm25.get_scores(query.lower().split())

    # ---------- Hybrid Score ----------
    final_scores = []

    for i in range(len(metadata)):

        semantic = semantic_score_map.get(i, 0.0)
        keyword = float(keyword_scores[i])

        hybrid = 0.7 * semantic + 0.3 * keyword

        final_scores.append((hybrid, i))

    final_scores.sort(reverse=True)

    results = []

    for score, idx in final_scores[:top_k]:

        results.append({
            "score": score,
            "document": metadata[idx]["document_name"],
            "section": metadata[idx]["section"],
            "text": metadata[idx]["text"]
        })

    return results


if __name__ == "__main__":

    query = input("Enter your question: ")
    top_k = int(input("Enter Top-k: "))

    results = hybrid_search(query, top_k)

    print("\nHybrid Search Results\n")

    for i, item in enumerate(results, start=1):

        print("=" * 60)
        print(f"Rank : {i}")
        print(f"Score : {item['score']:.4f}")
        print(f"Document : {item['document']}")
        print(f"Section : {item['section']}")
        print(item["text"])