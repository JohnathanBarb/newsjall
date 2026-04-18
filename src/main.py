from fastapi import FastAPI

from src.health.router import health_router

app = FastAPI()

app.include_router(
    health_router,
    prefix="/api/health",
)
