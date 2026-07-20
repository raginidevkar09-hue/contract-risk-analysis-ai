from fastapi import APIRouter

from src.api.models.request_models import AnalyzeRequest
from src.api.models.response_models import AnalyzeResponse
from src.api.utils.exception_handler import ContractAnalysisException
from src.llm.rag_chain import run_rag

router = APIRouter(
    prefix="/analyze",
    tags=["Contract Analysis"]
)


@router.post(
    "/",
    summary="Analyze Contract",
    description="Analyze the contract and generate a detailed risk report."
)

def analyze_contract(request: AnalyzeRequest):
    if not request.question.strip():
        raise ContractAnalysisException(
            "Question cannot be empty."
        )
    
    result = run_rag(
        question=request.question,
        prompt_type=request.prompt_type,
        top_k=request.top_k
    )

    return AnalyzeResponse(**result)