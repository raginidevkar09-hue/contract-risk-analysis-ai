def generate_explanation(clause_info):

    if clause_info["status"] == "Present":

        return {

            "reason":

                f"Clause detected with {clause_info['confidence_level']} confidence "

                f"({clause_info['confidence']:.2f}).",

            "evidence":

                clause_info["matched_chunk"]

        }

    return {

        "reason":

            f"Clause not detected. Best semantic similarity "

            f"was {clause_info['confidence']:.2f} "

            f"({clause_info['confidence_level']}).",

        "evidence":

            clause_info["matched_chunk"]

    }