import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.risk_engine.missing_clause_detector import detect_missing_clauses
from src.risk_engine.semantic_clause_detector import detect_semantic_clauses
from src.risk_engine.risk_scoring import calculate_risk
from src.risk_engine.risk_report import generate_report
from src.risk_engine.executive_summary import generate_executive_summary
from src.risk_engine.json_export import export_json

def analyze_contract(data, method="keyword"):

    if method == "keyword":

        clause_result = detect_missing_clauses(data)

    elif method == "semantic":

        clause_result = detect_semantic_clauses(data)

    else:

        raise ValueError("method must be 'keyword' or 'semantic'")

    risk_result = calculate_risk(
        clause_result["missing"]
    )

    report = generate_report(
        clause_matches=clause_result["matches"],
        risk_result=risk_result
    )

    report["executive_summary"] = generate_executive_summary(report)

    return report


if __name__ == "__main__":

    chunks = [

        "This agreement may be terminated by either party upon thirty days written notice.",

        "Payment shall be made within thirty days.",

        "The governing law shall be the laws of California."

    ]

    from pprint import pprint

    report = analyze_contract(
        chunks,
        method="semantic"
    )

    from pprint import pprint

    pprint(report)

    print("\n")
    print("=" * 80)
    print(report["executive_summary"])

    export_json(
        report,
        "data/structured/risk_report.json"
    )