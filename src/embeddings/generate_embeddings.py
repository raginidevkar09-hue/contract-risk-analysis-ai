from pathlib import Path
import json
from sentence_transformers import SentenceTransformer

INPUT_FOLDER = Path("data/metadata")
OUTPUT_FOLDER = Path("data/embeddings")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

for json_file in INPUT_FOLDER.glob("*.json"):

    with open(json_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embeddings = []

    for chunk in chunks:

        vector = model.encode(
            chunk["text"],
            normalize_embeddings=True
        )

        embeddings.append({
            **chunk,
            "embedding": vector.tolist()
        })

    output_file = OUTPUT_FOLDER / json_file.name

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(embeddings, f, indent=4)

    print(f"Embedded: {json_file.name}")

print("Embedding generation completed.")