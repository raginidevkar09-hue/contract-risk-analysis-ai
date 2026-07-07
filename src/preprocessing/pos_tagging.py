from pathlib import Path
import spacy
import json

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/pos_tags")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

nlp = spacy.load("en_core_web_sm")

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    pos_data = []

    for token in doc:
        if not token.is_space:
            pos_data.append({
                "word": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_,
                "tag": token.tag_
            })

    output_file = OUTPUT_FOLDER / f"{txt_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pos_data, f, indent=4, ensure_ascii=False)

    print(f"POS Tagged: {txt_file.name}")

print("POS Tagging completed.")