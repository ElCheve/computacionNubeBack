from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str


class UserAnswer(BaseModel):
    success: bool
    message: str
    username: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str
