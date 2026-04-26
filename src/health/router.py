from fastapi import APIRouter

from src.health.schemas import HealthOut, StatusEnum

health_router = APIRouter()


@health_router.get("")
async def health_check() -> HealthOut:
    return HealthOut(
        app=StatusEnum.OK,
    )
