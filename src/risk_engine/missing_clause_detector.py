from src.risk_engine.clause_library import REQUIRED_CLAUSES


def detect_missing_clauses(contract_text: str):

    text = contract_text.lower()

    detected = []
    missing = []

    for clause, keywords in REQUIRED_CLAUSES.items():

        found = False

        for keyword in keywords:

            if keyword.lower() in text:
                found = True
                break

        if found:
            detected.append(clause)
        else:
            missing.append(clause)

    return {
        "detected": detected,
        "missing": missing
    }