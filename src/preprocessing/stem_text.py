from pathlib import Path
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

INPUT_FOLDER = Path("data/cleaned")
OUTPUT_FOLDER = Path("data/stemmed")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

stemmer = PorterStemmer()

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    tokens = word_tokenize(text)

    stems = [stemmer.stem(token) for token in tokens]

    output_file = OUTPUT_FOLDER / txt_file.name

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(" ".join(stems))

    print(f"Stemmed: {txt_file.name}")

print("Stemming completed.")