from pathlib import Path
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """

    embeddings = []

    for chunk in chunks:

        vector = model.encode(
            chunk,
            normalize_embeddings=True
        )

        embeddings.append(vector.tolist())

    return embeddings


if __name__ == "__main__":

    INPUT_FOLDER = Path("data/metadata")
    OUTPUT_FOLDER = Path("data/embeddings")

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    for json_file in INPUT_FOLDER.glob("*.json"):

        with open(json_file, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        texts = [chunk["text"] for chunk in chunks]

        vectors = generate_embeddings(texts)

        output = []

        for chunk, vector in zip(chunks, vectors):
            output.append({
                **chunk,
                "embedding": vector
            })

        with open(OUTPUT_FOLDER / json_file.name, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)

        print(f"Embedded: {json_file.name}")

    print("Embedding generation completed.")