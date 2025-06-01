from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from typing import Annotated
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import uvicorn
from email_validator import validate_email, EmailNotValidError
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr


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

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)