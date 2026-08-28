from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import pipeline_router
import uvicorn

app = FastAPI(
    title="Serverless Event-Driven File Pipeline API",
    description="Asynchronous S3 event notification handling, payload normalization, and sink delivery.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pipeline_router.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "serverless-file-pipeline"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
