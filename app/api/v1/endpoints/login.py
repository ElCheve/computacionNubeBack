from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserCreate, UserLogin, UserAnswer
from services.user_service import create_user, authenticate_user

router = APIRouter()

@router.post("/register", response_model=UserAnswer)
def register(user: UserCreate):
    if not create_user(user):
        raise HTTPException(status_code=400, detail="User already exists")
    return {"success": True, "message": "User registered successfully"}

@router.post("/login", response_model=UserAnswer)
def login(user: UserLogin):
    token = authenticate_user(user)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"success": True, "message": "Login successful", "username": user.username}
