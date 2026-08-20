from fastapi import APIRouter
from app.schemas.docker_meta import ContainerStatus
from app.services.docker_service import get_container_info

router = APIRouter(prefix="/api", tags=["Container Suite"])

@router.get("/status", response_model=ContainerStatus)
def container_status():
    return get_container_info()