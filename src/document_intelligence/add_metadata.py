from pathlib import Path
import json

INPUT_FOLDER = Path("data/chunks/recursive")
OUTPUT_FOLDER = Path("data/metadata")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for json_file in INPUT_FOLDER.glob("*.json"):

    with open(json_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    metadata_chunks = []

    for chunk in chunks:

        metadata_chunks.append({
            "chunk_id": chunk["chunk_id"],
            "document_name": json_file.stem,
            "page": None,
            "section": "Unknown",
            "contract_type": "Unknown",
            "text": chunk["text"]
        })

    output_file = OUTPUT_FOLDER / json_file.name

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(metadata_chunks, f, indent=4, ensure_ascii=False)

    print(f"Processed: {json_file.name}")

print("Metadata generation completed.")