from fastapi import APIRouter

from src.api.models.request_models import AnalyzeRequest
from src.api.models.response_models import AnalyzeResponse

from src.llm.rag_chain import run_rag

router = APIRouter(
    prefix="/analyze",
    tags=["Contract Analysis"]
)


@router.post(
    "/",
    response_model=AnalyzeResponse
)
def analyze_contract(request: AnalyzeRequest):

    result = run_rag(
        question=request.question,
        prompt_type=request.prompt_type,
        top_k=request.top_k
    )

    return AnalyzeResponse(**result)