import React, { useEffect, useState } from "react"
import { useAuth } from "@clerk/clerk-react";
import HotelCard from "./HotelCard"
import Title from "./Title"
import { useNavigate } from "react-router-dom"
import axios, { all } from "axios"

const BASE_URL = import.meta.env.VITE_API_BASE_URL

const FeaturedDestination = () => {
    const navigate = useNavigate()
    const [rooms, setRooms] = useState([])

    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth();
 
    useEffect(() => {
        const fetchData = async () => {
        try {
            const token = await getToken();

            const response = await axios.get(`${BASE_URL}/api/room`, {
                headers: {
                    Authorization: token ? `Bearer ${token}` : "",
                },
            });

            setRooms(response.data);
        } catch (error) {
            console.log(error);
        }
    };
        fetchData();
    }, [])

    return (
        <div className="flex flex-col items-center px-6 md:px-16 lg:px-24 bg-slate-50 py-20">
            <Title title="Featured Destination" subTitle="Discover our handpicked selection of exceptional properties around the world, offering unparalleled luxury and unforgettable experience. " />
            <div className="flex flex-wrap items-center justify-center gap-6 mt-20">
                {rooms.slice(0, 4).map((room, index) => (
                    <HotelCard key={room.id} room={room} index={index} />
                ))}
            </div>
            <button className="my-16 px-4 py-2 text-sm font-medium border border-gray-300 rounded bg-white hover:bg-gray-50 transition-all cursor-pointer" onClick={() => {navigate("/rooms"); scrollTo(0, 0)}}>
                View All Destinations
            </button>
        </div>
    )
}

export default FeaturedDestination;