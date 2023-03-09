from typing import Optional

from fastapi import HTTPException, status
from . import models

async def create_user(request, database) -> models.User:
    """
    A method for creating new user

    :param request:
    :param database:
    :return:
    """
    emp = models.User(name=request.name, email=request.email)
    database.add(emp)
    database.commit()
    database.refresh(emp)
    return emp

async def get_user_by_id(user_id, database) -> Optional[models.User]:
    """
    A method for getting user by id

    :param user_id:
    :param database:
    :return:
    """
    user = database.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT_FOUND_USER")
    return user


async def get_users(database):
    """
    A method for getting users

    :param database:
    :return:
    """
    users = database.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EMPTY_USERS")
    return users