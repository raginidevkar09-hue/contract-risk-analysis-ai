from pathlib import Path
import json

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/paragraphs")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as file:
        text = file.read()

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    paragraph_data = []

    for i, paragraph in enumerate(paragraphs, start=1):
        paragraph_data.append({
            "paragraph_id": i,
            "text": paragraph
        })

    output_file = OUTPUT_FOLDER / f"{txt_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(paragraph_data, file, indent=4, ensure_ascii=False)

    print(f"Processed: {txt_file.name}")

print("Paragraph splitting completed.")