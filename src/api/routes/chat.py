from fastapi import APIRouter, Depends
from typing import Callable

from src.api.models.request_models import AnalyzeRequest
from src.api.services.chat_service import chat
from src.api.dependencies import get_chat_service
from src.api.utils.exception_handler import ContractAnalysisException

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/",
    summary="Chat with Contract",
    description="Ask questions about the uploaded contract using RAG."
)
def chat_api(
    request: AnalyzeRequest,
    chat_service: Callable = Depends(get_chat_service)
):

    if not request.question.strip():
        raise ContractAnalysisException(
            "Question cannot be empty."
        )

    return chat_service(
        question=request.question,
        prompt_type=request.prompt_type,
        top_k=request.top_k
    )