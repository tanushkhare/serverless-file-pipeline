from fastapi import APIRouter
from backend.app.schemas.edge import EdgeInvocationRequest, EdgeInvocationResponse
from backend.app.services.edge_service import edge_service

router = APIRouter(prefix="/api/v1/edge", tags=["Serverless Edge Router"])

@router.post("/invoke", response_model=EdgeInvocationResponse)
async def invoke_edge_function(payload: EdgeInvocationRequest):
    return edge_service.route_invocation(payload)
