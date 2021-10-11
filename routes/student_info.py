from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List, Optional
from config.db import db
from config.librarian_auth_config import get_current_active_user
from schemas.student import StudentInfo

router = APIRouter()
collection = db.students


@router.get('/students', response_model=List[StudentInfo], response_description="List of all student profile")
async def get_all_students(current_user: StudentInfo = Depends(get_current_active_user)):
    document = await collection.find().to_list(10000)
    return JSONResponse(status_code=status.HTTP_200_OK, content=document)



