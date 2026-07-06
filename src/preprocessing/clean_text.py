from pathlib import Path
import re
import html

INPUT_FOLDER = Path("data/extracted")
OUTPUT_FOLDER = Path("data/cleaned")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    text = html.unescape(text)

    text = text.lower()

    text = re.sub(r'page\s+\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)

    text = re.sub(r'[@#$%^*~`|]', '', text)

    text = re.sub(r'[ \t]+', ' ', text)

    text = re.sub(r'\n\s*\n+', '\n\n', text)

    text = text.strip()

    output_file = OUTPUT_FOLDER / txt_file.name

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Cleaned: {txt_file.name}")

print("All files cleaned successfully.")