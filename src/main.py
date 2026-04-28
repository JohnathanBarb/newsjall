from fastapi import FastAPI

from src.auth.router import auth_router
from src.health.router import health_router
from src.users.router import users_router

app = FastAPI()

app.include_router(
    health_router,
    prefix="/api/health",
)
app.include_router(users_router, prefix="/api/users")
app.include_router(auth_router, prefix="/auth")
