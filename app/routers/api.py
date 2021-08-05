from fastapi import APIRouter

from app.routers import index
from app.routers import authentication
from app.routers import registration

router = APIRouter()

router.include_router(index.router)
router.include_router(authentication.router)
router.include_router(registration.router)