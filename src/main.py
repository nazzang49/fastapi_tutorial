from fastapi import FastAPI
from src.user import router as user_router

app = FastAPI()

@app.get("/")
async def root():
    return {
        "Hello": "World"
    }

app.include_router(user_router.router)
