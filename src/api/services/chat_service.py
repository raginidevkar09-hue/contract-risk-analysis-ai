from src.llm.rag_chain import run_rag


def chat(question: str,
         prompt_type: str = "risk_analysis",
         top_k: int = 5):

    return run_rag(
        question=question,
        prompt_type=prompt_type,
        top_k=top_k
    )