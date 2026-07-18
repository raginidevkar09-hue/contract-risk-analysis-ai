import sys
import json
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from langchain_core.prompts import PromptTemplate

from src.retrieval.retriever import retrieve
from src.rag.prompt_factory import get_prompt
from src.llm.local_llm import generate_answer
from src.rag.output_schema import ContractAnalysis
from src.risk_engine.rule_engine import analyze_contract

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
    chunks = [
        chunk["text"]
        for chunk in results
    ]

    risk_report = analyze_contract(
        chunks,
        method="semantic"
    )
    clean_answer = answer.strip()
    clean_answer = re.sub(r"^```json", "", clean_answer, flags=re.IGNORECASE)
    clean_answer = re.sub(r"^```", "", clean_answer)
    clean_answer = re.sub(r"```$", "", clean_answer)

    clean_answer = clean_answer.strip()

    try:
        parsed_answer = json.loads(clean_answer)
    except Exception:
        parsed_answer = {
            "raw_response": answer
        }
    return {
        "question": question,
        "context": context,
        "answer": (
        parsed_answer.model_dump()
        if isinstance(parsed_answer, ContractAnalysis)
        else parsed_answer
        ),
        "risk_report": risk_report
    }