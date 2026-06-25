from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    username: str
    password: str
    expiresInMins: Optional[int] = 60

class LoginResponse(BaseModel):
    accessToken: str
    refreshToken: str
    id: int
    username: str

class User(BaseModel):
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str
