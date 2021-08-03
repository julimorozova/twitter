from fastapi import APIRouter

from app.routers import authentication


router = APIRouter()

router.include_router(authentication.router)