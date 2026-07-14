RISK_WEIGHTS = {

    "Termination": 15,
    "Confidentiality": 15,
    "Indemnity": 15,
    "Limitation of Liability": 15,
    "Payment": 10,
    "Governing Law": 10,
    "Force Majeure": 10,
    "Dispute Resolution": 5,
    "Intellectual Property": 3,
    "Data Protection": 2
}


def calculate_risk(missing_clauses):

    score = 0

    risks = []

    for clause in missing_clauses:

        weight = RISK_WEIGHTS.get(clause, 5)

        score += weight

        if weight >= 15:
            severity = "High"

        elif weight >= 10:
            severity = "Medium"

        else:
            severity = "Low"

        risks.append({

            "clause": clause,

            "severity": severity,

            "issue": f"{clause} clause is missing.",

            "recommendation":
            f"Add a proper {clause} clause."
        })

    score = min(score, 100)

    if score >= 70:
        overall = "High"

    elif score >= 40:
        overall = "Medium"

    else:
        overall = "Low"

    return {

        "risk_score": score,

        "overall_risk": overall,

        "risks": risks
    }