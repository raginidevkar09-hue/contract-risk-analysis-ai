from pathlib import Path
import spacy

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/lemmatized")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

nlp = spacy.load("en_core_web_sm")

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    lemmas = [token.lemma_ for token in doc]

    output_file = OUTPUT_FOLDER / txt_file.name

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(" ".join(lemmas))

    print(f"Lemmatized: {txt_file.name}")

print("Lemmatization completed.")