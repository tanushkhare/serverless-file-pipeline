from pydantic import BaseModel

class ContainerStatus(BaseModel):
    container_name: str
    image_tag: str
    status: str
    port_mapping: str