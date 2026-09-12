from fastapi import APIRouter, HTTPException
from backend.app.schemas.pipeline_schema import S3EventNotification, PipelineProcessingResponse
from backend.app.services.pipeline_service import pipeline_engine

router = APIRouter(prefix="/api/v1/pipeline", tags=["Serverless Event File Pipeline"])

@router.post("/process-event", response_model=PipelineProcessingResponse)
async def process_event_notification(payload: S3EventNotification):
    try:
        res = await pipeline_engine.process_file_event(
            payload.bucket_name, payload.object_key, payload.file_size_kb, payload.mime_type or "application/pdf"
        )
        return PipelineProcessingResponse(**res)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def pipeline_health():
    return {"status": "healthy", "service": "serverless-file-pipeline"}
