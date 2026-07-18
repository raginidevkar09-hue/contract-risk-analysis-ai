from pathlib import Path
import json
import numpy as np
import faiss


def create_faiss_index(chunks, embeddings):
    """
    Create a FAISS index from chunks and their embeddings.
    """

    vectors = np.array(embeddings).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(vectors)

    output_folder = Path("data/vector_db")
    output_folder.mkdir(parents=True, exist_ok=True)

    faiss.write_index(
        index,
        str(output_folder / "contracts.index")
    )

    metadata = []

    for chunk, embedding in zip(chunks, embeddings):
        metadata.append({
            "text": chunk,
            "embedding": embedding
        })

    with open(
        output_folder / "metadata.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)

    print("FAISS index created successfully.")

    return index


if __name__ == "__main__":

    INPUT_FOLDER = Path("data/embeddings")
    OUTPUT_FOLDER = Path("data/vector_db")

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    all_chunks = []
    all_embeddings = []

    for json_file in INPUT_FOLDER.glob("*.json"):

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            all_chunks.append(item["text"])
            all_embeddings.append(item["embedding"])

    create_faiss_index(all_chunks, all_embeddings)