from pydantic import BaseModel
from typing import Any


class AnalyzeResponse(BaseModel):

    question: str

    context: str

    answer: Any

    risk_report: dict