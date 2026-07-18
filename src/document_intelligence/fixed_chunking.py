from pathlib import Path
import json

CHUNK_SIZE = 500


def fixed_chunk_text(text: str, chunk_size: int = CHUNK_SIZE):
    """
    Split text into fixed-size chunks.
    Returns a list of text chunks.
    """
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


if __name__ == "__main__":

    INPUT_FOLDER = Path("data/cleaned")
    OUTPUT_FOLDER = Path("data/chunks/fixed")

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    for txt_file in INPUT_FOLDER.glob("*.txt"):

        text = txt_file.read_text(encoding="utf-8")

        chunks = fixed_chunk_text(text)

        data = [
            {
                "chunk_id": i + 1,
                "text": chunk
            }
            for i, chunk in enumerate(chunks)
        ]

        output_file = OUTPUT_FOLDER / f"{txt_file.stem}.json"

        output_file.write_text(
            json.dumps(data, indent=4, ensure_ascii=False),
            encoding="utf-8"
        )

    print("Fixed Chunking Completed")