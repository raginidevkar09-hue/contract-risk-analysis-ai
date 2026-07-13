import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from langchain_core.prompts import PromptTemplate

from src.retrieval.retriever import retrieve
from src.rag.prompt_factory import get_prompt
from src.llm.local_llm import generate_answer


def run_rag(question: str, prompt_type: str = "zero_shot", top_k: int = 5):

    # Retrieve relevant chunks
    results = retrieve(question, top_k)

    context = "\n\n".join(
        chunk["text"]
        for chunk in results
    )

    # Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=get_prompt(prompt_type)
    )

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    # LLM
    answer = generate_answer(final_prompt)

    return {
        "question": question,
        "context": context,
        "answer": answer
    }