from fastapi import APIRouter

from app.router.endpoints import room

router = APIRouter()

router.include_router(room.router, tags=["Rooms"])