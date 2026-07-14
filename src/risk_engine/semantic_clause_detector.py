import sys
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.risk_engine.clause_library import REQUIRED_CLAUSES
from src.risk_engine.clause_embeddings import embed_text


def detect_semantic_clauses(
    chunks: list[str],
    threshold: float = 0.65
):
    """
    Detect clauses using semantic similarity.

    Parameters
    ----------
    chunks : list[str]
        Contract chunks.

    threshold : float
        Similarity threshold.

    Returns
    -------
    dict
    """

    chunk_embeddings = [
        embed_text(chunk)
        for chunk in chunks
    ]

    detected = []
    missing = []

    clause_matches = {}

    for clause_name, keywords in REQUIRED_CLAUSES.items():

        best_score = -1.0
        best_chunk = ""

        for keyword in keywords:

            keyword_embedding = embed_text(keyword)

            similarities = np.dot(
                chunk_embeddings,
                keyword_embedding
            )

            index = int(np.argmax(similarities))

            score = float(similarities[index])

            if score > best_score:
                best_score = score
                best_chunk = chunks[index]

        if best_score >= threshold:

            detected.append(clause_name)

        else:

            missing.append(clause_name)

        clause_matches[clause_name] = {

            "score": round(best_score, 4),

            "matched_chunk": best_chunk,

            "found": best_score >= threshold

        }

    return {

        "detected": detected,

        "missing": missing,

        "matches": clause_matches

    }


if __name__ == "__main__":

    chunks = [

        "This agreement may be terminated by either party upon thirty days written notice.",

        "Payment shall be made within thirty days.",

        "The governing law shall be the laws of California."

    ]

    from pprint import pprint

    pprint(
        detect_semantic_clauses(chunks)
    )