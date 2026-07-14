def generate_report(

        detected_clauses,
        missing_clauses,
        risk_result
):

    return {

        "detected_clauses": detected_clauses,

        "missing_clauses": missing_clauses,

        "total_detected": len(detected_clauses),

        "total_missing": len(missing_clauses),

        "overall_risk": risk_result["overall_risk"],

        "risk_score": risk_result["risk_score"],

        "risks": risk_result["risks"]
    }