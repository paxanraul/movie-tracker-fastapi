from fastapi import APIRouter, HTTPException

import repository
from auth import hash_password, verify_password, create_access_token
from db import SessionLocal
from schemas import UserRegister, UserLogin, UserOut, Token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=Token)
async def register(data: UserRegister):
    async with SessionLocal() as session:
        existing = await repository.get_user_by_username(session, data.username)
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")

        user = await repository.create_user(session, data.username, hash_password(data.password))
        token = create_access_token(user.id)
        return Token(access_token=token)


@router.post("/login", response_model=Token)
async def login(data: UserLogin):
    async with SessionLocal() as session:
        user = await repository.get_user_by_username(session, data.username)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        token = create_access_token(user.id)
        return Token(access_token=token)