from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/chunks/recursive")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = splitter.split_text(text)

    chunk_data = []

    for i, chunk in enumerate(chunks, start=1):
        chunk_data.append({
            "chunk_id": i,
            "text": chunk
        })

    output_file = OUTPUT_FOLDER / f"{txt_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunk_data, f, indent=4, ensure_ascii=False)

    print(f"Chunked: {txt_file.name}")

print("Chunking completed.")