from typing import List
from schemas.librarian import LibrarianInfo
from fastapi import APIRouter, Depends
from config.db import db
from config.librarian_auth_config import get_current_active_user


router = APIRouter()
# collection = db.user

@router.get("/")
async def root():
    return {"response": "Welcome to your app!"}


@router.get("/api/users/me/", response_model=LibrarianInfo)
async def read_users_me(current_user: LibrarianInfo = Depends(get_current_active_user)):
    return current_user