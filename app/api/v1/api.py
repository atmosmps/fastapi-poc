from fastapi import APIRouter

from app.api.v1.endpoints import cupom, login, users, utils, healthcheck

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(cupom.router, prefix="/cupons", tags=["cupons"])
api_router.include_router(
    healthcheck.router, prefix="/healthcheck", tags=["healthcheck"]
)
