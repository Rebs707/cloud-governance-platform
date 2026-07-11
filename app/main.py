from fastapi import FastAPI
from app.api.governance import router as governance_router

app = FastAPI(
    title="Cloud Governance Platform",
    version="1.0.0"
)

app.include_router(governance_router)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "platform": "Cloud Governance Platform"
    }
