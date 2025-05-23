from fastapi import FastAPI

from app.router import api


app = FastAPI()

app.include_router(api.router, prefix="/api")

@app.get("/")
async def index() -> str:
    return "Welcome to Quick Stay"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)