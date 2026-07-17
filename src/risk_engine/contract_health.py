GRADE_MAPPING = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
]


def calculate_contract_health(risk_score: int):

    health_score = max(0, 100 - risk_score)

    for minimum, grade in GRADE_MAPPING:

        if health_score >= minimum:

            return {
                "contract_health": health_score,
                "grade": grade
            }

    return {
        "contract_health": health_score,
        "grade": "F"
    }