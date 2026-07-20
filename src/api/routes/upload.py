from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from src.api.services.upload_service import save_uploaded_file
from src.api.services.analyzer_service import process_contract

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post(
    "/",
    summary="Upload Contract",
    description="Upload a PDF contract and automatically process it."
)
def upload_contract(file: UploadFile = File(...)):

    path = save_uploaded_file(file)

    result = process_contract(path)

    return {

        "message": "Contract processed successfully.",

        "filename": file.filename,

        "saved_to": path,

        "processing": result

    }
