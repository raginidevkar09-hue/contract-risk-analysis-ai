from pathlib import Path
from unstructured.partition.pdf import partition_pdf
import json

INPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER = Path("data/structured")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for pdf_file in INPUT_FOLDER.glob("*.pdf"):

    elements = partition_pdf(
        filename=str(pdf_file),
        strategy="fast"
    )

    document = []

    for element in elements:
        document.append({
            "type": element.category,
            "text": str(element)
        })

    output_file = OUTPUT_FOLDER / f"{pdf_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(document, f, indent=4, ensure_ascii=False)

    print(f"Processed: {pdf_file.name}")

print("Document parsing completed.")