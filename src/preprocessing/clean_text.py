from pathlib import Path
import re
import html


def clean_text(text: str) -> str:
    """
    Clean extracted contract text.
    """

    text = html.unescape(text)

    text = text.lower()

    text = re.sub(r'page\s+\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)

    text = re.sub(r'[@#$%^*~`|]', '', text)

    text = re.sub(r'[ \t]+', ' ', text)

    text = re.sub(r'\n\s*\n+', '\n\n', text)

    text = text.strip()

    return text


if __name__ == "__main__":

    INPUT_FOLDER = Path("data/extracted")
    OUTPUT_FOLDER = Path("data/cleaned")

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    for txt_file in INPUT_FOLDER.glob("*.txt"):

        text = txt_file.read_text(encoding="utf-8")

        cleaned = clean_text(text)

        output_file = OUTPUT_FOLDER / txt_file.name
        output_file.write_text(cleaned, encoding="utf-8")

        print(f"Cleaned: {txt_file.name}")

    print("All files cleaned successfully.")