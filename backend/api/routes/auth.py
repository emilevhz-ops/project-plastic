import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.models import User
from core.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

users_db: dict[str, User] = {}


class RegisterRequest(BaseModel):
    email: str
    password: str
    role: str


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(request: RegisterRequest):
    if request.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        id=str(uuid.uuid4()),
        email=request.email,
        hashed_password=hash_password(request.password),
        role=request.role,
        is_active=True,
    )
    users_db[user.email] = user

    return {"message": "User registered successfully"}


@router.post("/login")
def login(request: LoginRequest):
    user = users_db.get(request.email)
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": user.email, "role": user.role})

    return {"access_token": access_token, "token_type": "bearer"}
