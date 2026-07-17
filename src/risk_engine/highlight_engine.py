def highlight_clause(match):

    if not match["found"]:

        return {
            "highlight": None,
            "start": -1,
            "end": -1
        }

    text = match["matched_chunk"]

    return {
        "highlight": text,
        "start": 0,
        "end": len(text)
    }
