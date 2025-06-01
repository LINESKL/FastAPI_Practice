from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from typing import Annotated
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import uvicorn
from email_validator import validate_email, EmailNotValidError
from items_views import router as items_router
from users.views import router as users_router
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)



@app.get("/")
def hello_index():
    return {
        "message": "Hello World"
    }

@app.get("/hello/ ")
def hello(name: str = "World"):
    name = name.strip().title()
    return {
        "message": f"Hello {name}"
    }



@app.post("/cals/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)