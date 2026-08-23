from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers.edge import router as edge_router
import uvicorn

app = FastAPI(
    title="Serverless Edge Compute & Function Router API",
    description="Sub-10ms edge function dispatch, cold start telemetry, and global region routing.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(edge_router)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "serverless-edge-router"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
