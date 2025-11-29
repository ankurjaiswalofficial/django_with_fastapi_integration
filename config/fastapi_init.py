from fastapi import FastAPI
from apps.core.api.routers import router

fastapi_app = FastAPI(
    title="FastAPI Endpoints",
    version="1.0",
    docs_url="/fastapi/docs",
    openapi_url="/fastapi/openapi.json",
)

fastapi_app.include_router(router, prefix="/fastapi")

