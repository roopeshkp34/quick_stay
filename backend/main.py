from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import api


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api.router, prefix="/api")

@app.get("/")
async def index() -> str:
    return "Welcome to Quick Stay"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)