from fastapi import FastAPI, HTTPException, Depends
from app.models import UserIn, UserOut, Token
from app.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
)
from app.database import db
from app.cache import get_user_from_cache, set_user_to_cache, invalidate_user_cache
from fastapi.security import OAuth2PasswordRequestForm
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/auth/signup", response_model=UserOut)
async def signup(user: UserIn):
    if await db["users"].find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user.password)
    result = await db["users"].insert_one(user_dict)

    # Invalidate cache after signup
    await invalidate_user_cache(user.email)

    user_out = {
        "_id": str(result.inserted_id),
        "name": user.name,
        "email": user.email,
    }
    return UserOut(**user_out)


@app.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db["users"].find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    email = current_user["email"]

    # Try cache first
    cached_user = await get_user_from_cache(email)
    if cached_user:
        return UserOut(**cached_user)

    # Fallback to DB
    user = await db["users"].find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user["_id"] = str(user["_id"])  # convert ObjectId to str

    user_out = UserOut(**user)

    # Cache the output using alias fields (e.g. "_id")
    await set_user_to_cache(email, user_out.dict(by_alias=True))

    return user_out
