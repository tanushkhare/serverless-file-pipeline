from fastapi import APIRouter, HTTPException
from backend.app.schemas.pipeline_schema import S3EventNotification, PipelineProcessingResponse
from backend.app.services.pipeline_service import file_pipeline

router = APIRouter(prefix="/api/v1/pipeline", tags=["Serverless File Pipeline"])

@router.post("/process-event", response_model=PipelineProcessingResponse)
async def handle_s3_event(payload: S3EventNotification):
    try:
        result = await file_pipeline.process_file_event(
            payload.bucket_name, payload.object_key, payload.file_size_kb, payload.mime_type
        )
        return PipelineProcessingResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
