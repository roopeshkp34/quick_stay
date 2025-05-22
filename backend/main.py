from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def index() -> str:
    return "Welcome to Quick Stay"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)