from fastapi import APIRouter
from .schemas import HealthCheck

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
def health_check():
    return HealthCheck(status=True, message="Service is up and running")