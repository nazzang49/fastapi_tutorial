from fastapi import FastAPI
from src.user import router as emp_router

app = FastAPI()

@app.get("/")
async def root():
    return {
        "Hello": "World"
    }

app.include_router(emp_router.api_router)
