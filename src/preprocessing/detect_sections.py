from pathlib import Path
import json
import re

INPUT_FOLDER = Path("data/paragraphs")
OUTPUT_FOLDER = Path("data/sections")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

heading_pattern = re.compile(
    r'^(SECTION\s+\d+|ARTICLE\s+[IVXLC]+|\d+\.\s+.*|[A-Z][A-Z\s]{3,})$',
    re.IGNORECASE
)

for json_file in INPUT_FOLDER.glob("*.json"):

    with open(json_file, "r", encoding="utf-8") as file:
        paragraphs = json.load(file)

    sections = []
    current_section = "Unknown"

    for paragraph in paragraphs:

        text = paragraph["text"].strip()

        if heading_pattern.match(text):
            current_section = text
            continue

        sections.append({
            "section": current_section,
            "paragraph_id": paragraph["paragraph_id"],
            "text": text
        })

    output_file = OUTPUT_FOLDER / f"{json_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(sections, file, indent=4, ensure_ascii=False)

    print(f"Processed: {json_file.name}")

print("Section detection completed.")