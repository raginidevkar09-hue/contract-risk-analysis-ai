from pathlib import Path
import nltk
from nltk.tokenize import word_tokenize
import json

nltk.download("punkt")
nltk.download("punkt_tab")

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/tokens")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    tokens = word_tokenize(text)

    output_file = OUTPUT_FOLDER / f"{txt_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=4, ensure_ascii=False)

    print(f"Tokenized: {txt_file.name}")

print("Tokenization completed.")