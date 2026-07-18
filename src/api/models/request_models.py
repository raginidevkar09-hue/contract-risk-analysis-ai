from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):

    question: str = Field(
        ...,
        description="User question"
    )

    prompt_type: str = Field(
        default="risk_analysis",
        description="Prompt template"
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of retrieved chunks"
    )