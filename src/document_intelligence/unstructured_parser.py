from pathlib import Path
from unstructured.partition.pdf import partition_pdf
import json

INPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER = Path("data/structured")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

for pdf in INPUT_FOLDER.glob("*.pdf"):

    elements = partition_pdf(
        filename=str(pdf),
        strategy="fast"
    )

    output = []

    for element in elements:
        output.append({
            "type": element.category,
            "text": str(element)
        })

    with open(
        OUTPUT_FOLDER / f"{pdf.stem}.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(pdf.name)

print("Completed")