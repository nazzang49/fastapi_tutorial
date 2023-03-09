from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src import db
from . import schema
from . import validator
from . import services

router = APIRouter(tags=["user"], prefix="/user")

@router.post("", status_code=status.HTTP_200_OK)
async def create_user(request: schema.User, database: Session = Depends(db.get_db)):
    """
    A method for creating new user

    :param request:
    :param database:
    :return:
    """
    user = await validator.is_email_exist(request.email, database)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Email Already Exist. Try Another!"
        )

    registered_user = await services.create_user(request, database)
    return registered_user

@router.get("/{user_id}", response_model=schema.UserItem)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, database)

@router.get("", response_model=List[schema.UserItem])
async def get_users(database: Session = Depends(db.get_db)):
    return await services.get_users(database)