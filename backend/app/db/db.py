###### USERS #####
users = [
    {
        "id": "1",
        "name": "Roopesh K P",
        "sub": "user_2wgBi77VZyM0JB52QyZPj8Rp7gA"
    }
]

###### HOTELS #####

hotels = [
    {
    "id": "67f76393197ac559e4089b72",
    "name": "Urbanza Suites",
    "address": "Main Road  123 Street , 23 Colony",
    "contact": "+0123456789",
    "owner": users[0],
    "city": "New York",
    "created_at": "2025-04-10T06:22:11.663Z",
    "updated_at": "2025-04-10T06:22:11.663Z",
    "__v": 0
}
]


###### ROOMS #####
rooms = [
    {
        "id": "67f7647c197ac559e4089b96",
        "hotel": hotels[0],
        "room_type": "Double Bed",
        "price_per_night": 399,
        "amenities": ["Room Service", "Mountain View", "Pool Access"],
        "images": ["assets/roomImg1.png", "assets/roomImg2.png", 'assets/roomImg3.png', "assets/roomImg4.png"],
        "is_available": True,
        "created_at": "2025-04-10T06:26:04.013Z",
        "updated_at": "2025-04-10T06:26:04.013Z",
        "__v": 0
    },
    {
        "id": "67f76452197ac559e4089b8e",
        "hotel": hotels[0],
        "room_type": "Double Bed",
        "price_per_night": 299,
        "amenities": ["Room Service", "Mountain View", "Pool Access"],
        "images": ["assets/roomImg2.png", 'assets/roomImg3.png', "assets/roomImg4.png", "assets/roomImg1.png"],
        "is_available": True,
        "created_at": "2025-04-10T06:25:22.593Z",
        "updated_at": "2025-04-10T06:25:22.593Z",
        "__v": 0
    },
    {
        "id": "67f76406197ac559e4089b82",
        "hotel": hotels[0],
        "room_type": "Double Bed",
        "price_per_night": 249,
        "amenities": ["Free WiFi", "Free Breakfast", "Room Service"],
        "images": ['assets/roomImg3.png', "assets/roomImg4.png", "assets/roomImg1.png", "assets/roomImg2.png"],
        "is_available": True,
        "created_at": "2025-04-10T06:24:06.285Z",
        "updated_at": "2025-04-10T06:24:06.285Z",
        "__v": 0
    },
    {
        "id": "67f763d8197ac559e4089b7a",
        "hotel": hotels[0],
        "room_type": "Single Bed",
        "price_per_night": 199,
        "amenities": ["Free WiFi", "Room Service", "Pool Access"],
        "images": ["assets/roomImg4.png", "assets/roomImg1.png", "assets/roomImg2.png", 'assets/roomImg3.png'],
        "is_available": True,
        "created_at": "2025-04-10T06:23:20.252Z",
        "updated_at": "2025-04-10T06:23:20.252Z",
        "__v": 0
    }
]