from fastapi import FastAPI, HTTPException
from app.models import User, UserIn
from app.database import db

app = FastAPI()

@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    result = await db["users"].insert_one(user.dict())
    user_out = user.dict()
    user_out["_id"] = str(result.inserted_id)
    return user_out

@app.get("/users/{email}", response_model=User)
async def get_user(email: str):
    user = await db["users"].find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])
    return user
