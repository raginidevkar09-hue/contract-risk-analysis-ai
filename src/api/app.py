from fastapi import FastAPI
from src.api.routes.analyze import router as analyze_router
from src.api.routes.health import router as health_router
from src.api.routes.upload import router as upload_router

app = FastAPI(
    title="Contract Risk Analysis AI",
    version="1.0.0",
    description="Professional AI-powered Contract Risk Analysis System"
)

app.include_router(health_router)
app.include_router(analyze_router)
app.include_router(upload_router)

@app.get("/")
def root():

    return {
        "message": "Contract Risk Analysis AI Backend Running"
    }