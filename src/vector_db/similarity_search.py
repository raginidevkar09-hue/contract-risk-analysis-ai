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

query = input("Enter your question: ")

query_embedding = model.encode(
    query,
    normalize_embeddings=True
).astype("float32")

scores, indices = index.search(
    np.array([query_embedding]),
    k=5
)

print("\nTop Matches:\n")

for score, idx in zip(scores[0], indices[0]):

    print("-" * 60)
    print(f"Score : {score:.4f}")
    print(f"Document : {metadata[idx]['document_name']}")
    print(f"Section : {metadata[idx]['section']}")
    print(f"Text :\n{metadata[idx]['text']}\n")