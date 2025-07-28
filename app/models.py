from pydantic import BaseModel, EmailStr
from typing import Optional

class UserIn(BaseModel):
    name: str
    email: EmailStr

class User(UserIn):
    _id: Optional[str]
