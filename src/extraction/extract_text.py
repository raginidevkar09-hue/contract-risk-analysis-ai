import fitz
from pathlib import Path

RAW_FOLDER = Path("data/raw")
OUTPUT_FOLDER = Path("data/extracted")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

pdf_files = list(RAW_FOLDER.glob("*.pdf"))

if not pdf_files:
    print("No PDF files found in data/raw/")
else:
    print(f"Found {len(pdf_files)} PDF(s).\n")

for pdf_file in pdf_files:
    print(f"Processing: {pdf_file.name}")

    try:
        doc = fitz.open(pdf_file)

        text = ""

        for page in doc:
            text += page.get_text()

        output_file = OUTPUT_FOLDER / f"{pdf_file.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Saved: {output_file.name}")

    except Exception as e:
        print(f"Error processing {pdf_file.name}: {e}")

print("\nAll PDFs processed successfully.")