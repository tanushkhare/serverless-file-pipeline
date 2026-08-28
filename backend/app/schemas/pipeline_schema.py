from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime

class S3EventNotification(BaseModel):
    bucket_name: str = Field(..., description="Target AWS/LocalStack S3 Bucket")
    object_key: str = Field(..., description="Uploaded file object key/path")
    file_size_kb: float = Field(default=124.5, ge=0.1)
    mime_type: Optional[str] = Field(default="application/pdf")

class PipelineProcessingResponse(BaseModel):
    event_id: str
    bucket: str
    key: str
    status: str
    stage_latencies_ms: Dict[str, float]
    total_execution_ms: float
    output_destination: str
    timestamp: str
