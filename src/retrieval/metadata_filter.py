from pathlib import Path
import json

INPUT_FILE = Path("data/vector_db/metadata.json")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    metadata = json.load(f)


def filter_chunks(
    contract_type=None,
    section=None,
    page_start=None,
    page_end=None
):

    results = []

    for chunk in metadata:

        if contract_type is not None:
            if chunk["contract_type"] != contract_type:
                continue

        if section is not None:
            if chunk["section"] != section:
                continue

        page = chunk.get("page")

        if (
            page is not None
            and page_start is not None
            and page < page_start
        ):
            continue

        if (
            page is not None
            and page_end is not None
            and page > page_end
        ):
            continue

        results.append(chunk)

    return results


if __name__ == "__main__":

    results = filter_chunks(
        contract_type="Unknown",
        section="Unknown"
    )

    print(f"Total Chunks : {len(results)}")