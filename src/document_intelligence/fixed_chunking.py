from pathlib import Path
import json

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/chunks/fixed")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

CHUNK_SIZE = 500

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [
        text[i:i + CHUNK_SIZE]
        for i in range(0, len(text), CHUNK_SIZE)
    ]

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

print("Fixed Chunking Completed")