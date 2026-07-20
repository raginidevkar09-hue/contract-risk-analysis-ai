from fastapi import FastAPI
from src.api.routes.analyze import router as analyze_router
from src.api.routes.health import router as health_router
from src.api.routes.upload import router as upload_router
from src.api.routes.chat import router as chat_router
from src.api.utils.exception_handler import (
    ContractAnalysisException,
    contract_exception_handler,
    generic_exception_handler
)

app = FastAPI(
    title="Contract Risk Analysis AI API",
    description="""
AI-powered Contract Risk Analysis System.

Features:
- Upload Contracts
- Automatic Processing
- RAG-based Question Answering
- Risk Detection
- Clause Analysis
- Executive Summary
""",
    version="1.0.0",
    contact={
        "name": "Ragini Devkar",
        "email": "your-email@example.com"
    },
    license_info={
        "name": "MIT License"
    }
)

app.add_exception_handler(
    ContractAnalysisException,
    contract_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)
app.include_router(health_router)
app.include_router(analyze_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def root():

    return {
        "message": "Contract Risk Analysis AI Backend Running"
    }