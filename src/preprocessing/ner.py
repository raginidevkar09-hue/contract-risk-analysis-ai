from pathlib import Path
import spacy
import json

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/entities")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

nlp = spacy.load("en_core_web_sm")

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char
        })

    output_file = OUTPUT_FOLDER / f"{txt_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(entities, f, indent=4, ensure_ascii=False)

    print(f"NER Completed: {txt_file.name}")

print("Named Entity Recognition completed.")