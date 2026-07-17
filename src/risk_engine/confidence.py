def confidence_level(score: float):

    if score >= 0.90:
        return "Very High"

    elif score >= 0.80:
        return "High"

    elif score >= 0.70:
        return "Medium"

    elif score >= 0.60:
        return "Low"

    return "Very Low"