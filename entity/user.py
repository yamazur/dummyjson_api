from pydantic import BaseModel


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
