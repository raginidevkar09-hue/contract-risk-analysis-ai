import json


def export_json(report, output_file):

    with open(output_file, "w", encoding="utf-8") as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"Report exported to: {output_file}")