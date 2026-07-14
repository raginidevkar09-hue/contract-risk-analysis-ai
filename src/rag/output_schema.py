from pydantic import BaseModel


class ContractAnalysis(BaseModel):
    question: str
    answer: str
    clause: str
    risk_level: str
    confidence: str
    