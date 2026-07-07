from pathlib import Path
import json

from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/chunks/semantic")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

splitter = SemanticChunker(embeddings)

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = splitter.split_text(text)

    data = []

    for i, chunk in enumerate(chunks, start=1):
        data.append({
            "chunk_id": i,
            "text": chunk
        })

    with open(
        OUTPUT_FOLDER / f"{txt_file.stem}.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

print("Semantic Chunking Completed")