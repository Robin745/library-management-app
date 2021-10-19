from typing import List
from fastapi import APIRouter, Depends
from config.db import db
from config.librarian_auth_config import get_current_active_user
from schemas.student import StudentInfo


router = APIRouter()
# collection = db.user

@router.get("/")
async def root():
    return {"response": "Welcome to your app!"}


@router.get("/api/users/me/", response_model=StudentInfo)
async def read_users_me(current_user: StudentInfo = Depends(get_current_active_user)):
    return current_user