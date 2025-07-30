from fastapi import FastAPI, HTTPException, Depends
from app.models import UserIn, UserOut, Token
from app.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
)
from app.database import db
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


@app.post("/auth/signup", response_model=UserOut)
async def signup(user: UserIn):
    if await db["users"].find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user.password)
    result = await db["users"].insert_one(user_dict)
    user_out = {
        "_id": str(result.inserted_id),
        "name": user.name,
        "email": user.email,
    }
    return user_out


@app.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db["users"].find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
