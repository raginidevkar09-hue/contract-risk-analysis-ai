from pathlib import Path
import json
import numpy as np
import faiss

INPUT_FOLDER = Path("data/embeddings")
OUTPUT_FOLDER = Path("data/vector_db")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

all_embeddings = []
metadata = []

for json_file in INPUT_FOLDER.glob("*.json"):

    with open(json_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    for chunk in chunks:
        all_embeddings.append(chunk["embedding"])
        metadata.append(chunk)

embeddings = np.array(all_embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    str(OUTPUT_FOLDER / "contracts.index")
)

with open(
    OUTPUT_FOLDER / "metadata.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(metadata, f, indent=4, ensure_ascii=False)

print("FAISS index created successfully.")