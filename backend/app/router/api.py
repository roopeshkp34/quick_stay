from fastapi import APIRouter

from app.router import room

router = APIRouter()

router.include_router(room.router, tags=["Rooms"])