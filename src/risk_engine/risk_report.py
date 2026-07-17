from src.risk_engine.recommendation_library import RECOMMENDATIONS
from src.risk_engine.contract_health import calculate_contract_health
from src.risk_engine.explainability import generate_explanation
from src.risk_engine.confidence import confidence_level
from src.risk_engine.highlight_engine import highlight_clause

def generate_report(
    clause_matches,
    risk_result
):

    detected = []
    missing = []

    health = calculate_contract_health(
        risk_result["risk_score"]
    )
    detailed_report = []

    for clause, info in clause_matches.items():

        if info["found"]:
            detected.append(clause)
            status = "Present"
        else:
            missing.append(clause)
            status = "Missing"

        risk = next(
            (
                r
                for r in risk_result["risks"]
                if r["clause"] == clause
            ),
            None
        )

        if risk:

            details = RECOMMENDATIONS.get(clause, {})

            severity = details.get("severity", risk["severity"])

            issue = details.get(
                "business_impact",
                risk["issue"]
            )

            recommendation = details.get(
                "recommendation",
                risk["recommendation"]
            )

        else:

            severity = "Low"
            issue = "Clause detected."
            recommendation = "No action required."

        confidence = confidence_level(
            info["score"]
        )
        explanation = generate_explanation({

            "status": status,

            "confidence": round(info["score"], 4),

            "confidence_level": confidence,

            "matched_chunk": info["matched_chunk"],

        })

        highlight = highlight_clause(info)

        detailed_report.append({

            "clause": clause,

            "status": status,

            "confidence_score": round(info["score"], 4),
            "confidence_level": confidence,

            "matched_chunk": info["matched_chunk"],

            "severity": severity,

            "issue": issue,

            "recommendation": recommendation,

            "reason": explanation["reason"],

            "evidence": explanation["evidence"],

            "highlight": highlight["highlight"],

            "highlight_start": highlight["start"],

            "highlight_end": highlight["end"]

        })

    return {

    "overall_risk": risk_result["overall_risk"],

    "risk_score": risk_result["risk_score"],

    "contract_health": health["contract_health"],

    "grade": health["grade"],

    "total_detected": len(detected),

    "total_missing": len(missing),

    "detected_clauses": detected,

    "missing_clauses": missing,

    "clauses": detailed_report

}