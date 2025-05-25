from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status

from app.db import rooms
from app.router import dependency

router = APIRouter(prefix="/room")


@router.get("")
async def get_rooms(
    user: Optional[Dict] = Depends(dependency.get_optional_user),
) -> List[Dict]:
    return rooms

@router.get("/{room_id}")
async def get_a_room(
    room_id: str,
    user: Optional[Dict] = Depends(dependency.get_optional_user)
) -> Dict:
    for room in rooms:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
