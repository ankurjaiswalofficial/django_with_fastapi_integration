from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: bool = False
    message: str = "Service is down"
