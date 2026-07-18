import fitz


def extract_text(pdf_path: str) -> str:
    """
    Extract text from a single PDF file.
    """

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


if __name__ == "__main__":
    from pathlib import Path

    RAW_FOLDER = Path("data/raw")
    OUTPUT_FOLDER = Path("data/extracted")

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    pdf_files = list(RAW_FOLDER.glob("*.pdf"))

    print(f"Found {len(pdf_files)} PDF(s).")

    for pdf in pdf_files:
        text = extract_text(str(pdf))

        output_file = OUTPUT_FOLDER / f"{pdf.stem}.txt"

        output_file.write_text(text, encoding="utf-8")

        print(f"Saved: {output_file.name}")