def generate_executive_summary(report):

    lines = []

    lines.append("EXECUTIVE SUMMARY")
    lines.append("=" * 60)

    lines.append(
        f"Overall Risk      : {report['overall_risk']}"
    )

    lines.append(
        f"Risk Score        : {report['risk_score']}/100"
    )

    lines.append(
        f"Contract Health   : {report['contract_health']}/100"
    )

    lines.append(
        f"Grade             : {report['grade']}"
    )

    lines.append("")

    lines.append("Detected Clauses")

    if report["detected_clauses"]:

        for clause in report["detected_clauses"]:

            lines.append(f"  ✓ {clause}")

    else:

        lines.append("  None")

    lines.append("")

    lines.append("Missing Clauses")

    if report["missing_clauses"]:

        for clause in report["missing_clauses"]:

            lines.append(f"  ✗ {clause}")

    else:

        lines.append("  None")

    lines.append("")

    lines.append("Top Recommendations")

    for clause in report["clauses"]:

        if clause["status"] == "Missing":

            lines.append(
                f"- {clause['recommendation']}"
            )

    return "\n".join(lines)