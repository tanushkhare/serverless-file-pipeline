from pydantic import BaseModel, Field
from typing import List

class EdgeInvocationRequest(BaseModel):
    payload: str = Field(default="production edge event payload")
    target_region: str = Field(default="auto-geo")

class RegionalEdgeMetric(BaseModel):
    region_code: str
    edge_location: str
    latency_ms: float
    cold_start: bool
    status: str

class EdgeInvocationResponse(BaseModel):
    invocation_id: str
    routed_region: str
    execution_time_ms: float
    memory_used_mb: float
    cold_start_detected: bool
    active_edge_nodes: List[RegionalEdgeMetric]
