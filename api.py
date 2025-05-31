from fastapi import FastAPI
from pydantic import Basemodel

app = FastApi()

class User(BaseModel):
    id: int
    name: str
    age:int
    email: str

@app.post("/users/")
async def create_user(user: User):
    return user