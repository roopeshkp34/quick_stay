
from fastapi import APIRouter

router = APIRouter(prefix="/room")

user_dummy_data = {
    "id": "user_2unqyL4diJFP1E3pIBnasc7w8hP",
    "username": "Great Stack",
    "email": "user.greatstack@gmail.com",
    "image": "https://img.clerk.com/eyJ0eXBlIjoicHJveHkiLCJzcmMiOiJodHRwczovL2ltYWdlcy5jbGVyay5kZXYvdXBsb2FkZWQvaW1nXzJ2N2c5YVpSSEFVYVUxbmVYZ2JkSVVuWnFzWSJ9",
    "role": "hotelOwner",
    "created_at": "2025-03-25T09:29:16.367Z",
    "updated_at": "2025-04-10T06:34:48.719Z",
    "__v": 1,
    "recent_searched_cities": [
        "New York"
    ]
}

hotel_dummy_data = {
    "id": "67f76393197ac559e4089b72",
    "name": "Urbanza Suites",
    "address": "Main Road  123 Street , 23 Colony",
    "contact": "+0123456789",
    "owner": user_dummy_data,
    "city": "New York",
    "created_at": "2025-04-10T06:22:11.663Z",
    "updated_at": "2025-04-10T06:22:11.663Z",
    "__v": 0
}

hotel_dummy_data = {
    "id": "67f76393197ac559e4089b72",
    "name": "Urbanza Suites",
    "address": "Main Road  123 Street , 23 Colony",
    "contact": "+0123456789",
    "owner": user_dummy_data,
    "city": "New York",
    "created_at": "2025-04-10T06:22:11.663Z",
    "updated_at": "2025-04-10T06:22:11.663Z",
    "__v": 0
}

@router.get("")
async def get_rooms():
    return [
    {
        "id": "67f7647c197ac559e4089b96",
        "hotel": hotel_dummy_data,
        "room_type": "Double Bed",
        "price_per_night": 399,
        "amenities": ["Room Service", "Mountain View", "Pool Access"],
        "images": ["roomImg1.png", "roomImg2.png", 'roomImg3.png', "roomImg4.png"],
        "is_available": True,
        "created_at": "2025-04-10T06:26:04.013Z",
        "updated_at": "2025-04-10T06:26:04.013Z",
        "__v": 0
    },
    {
        "id": "67f76452197ac559e4089b8e",
        "hotel": hotel_dummy_data,
        "room_type": "Double Bed",
        "price_per_night": 299,
        "amenities": ["Room Service", "Mountain View", "Pool Access"],
        "images": ["roomImg2.png", 'roomImg3.png', "roomImg4.png", "roomImg1.png"],
        "is_available": True,
        "created_at": "2025-04-10T06:25:22.593Z",
        "updated_at": "2025-04-10T06:25:22.593Z",
        "__v": 0
    },
    {
        "id": "67f76406197ac559e4089b82",
        "hotel": hotel_dummy_data,
        "room_type": "Double Bed",
        "price_per_night": 249,
        "amenities": ["Free WiFi", "Free Breakfast", "Room Service"],
        "images": ['roomImg3.png', "roomImg4.png", "roomImg1.png", "roomImg2.png"],
        "is_available": True,
        "created_at": "2025-04-10T06:24:06.285Z",
        "updated_at": "2025-04-10T06:24:06.285Z",
        "__v": 0
    },
    {
        "id": "67f763d8197ac559e4089b7a",
        "hotel": hotel_dummy_data,
        "room_type": "Single Bed",
        "price_per_night": 199,
        "amenities": ["Free WiFi", "Room Service", "Pool Access"],
        "images": ["roomImg4.png", "roomImg1.png", "roomImg2.png", 'roomImg3.png'],
        "is_available": True,
        "created_at": "2025-04-10T06:23:20.252Z",
        "updated_at": "2025-04-10T06:23:20.252Z",
        "__v": 0
    }
]
