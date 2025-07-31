from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    email: EmailStr

    model_config = {
        "populate_by_name": True, 
    }

class Token(BaseModel):
    access_token: str
    token_type: str
