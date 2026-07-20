from fastapi import Request
from fastapi.responses import JSONResponse


class ContractAnalysisException(Exception):
    def __init__(self, message: str):
        self.message = message


async def contract_exception_handler(
    request: Request,
    exc: ContractAnalysisException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": exc.message
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": str(exc)
        }
    )