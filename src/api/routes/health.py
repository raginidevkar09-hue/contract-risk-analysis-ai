from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get(
    "/",
    summary="Health Check",
    description="Verify that the backend API is running."
)
def health_check():

    return {
        "status": "healthy",
        "service": "Contract Risk Analysis AI",
        "version": "1.0.0"
    }