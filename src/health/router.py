from fastapi import APIRouter

from src.health.schemas import HealthOut, StatusEnum

health_router = APIRouter()


@health_router.get("", response_model=HealthOut)
async def health_check():
    return HealthOut(
        app=StatusEnum.OK,
    )
