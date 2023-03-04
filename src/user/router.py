from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src import db
from . import schema
from . import validator
from . import services

api_router = APIRouter(tags=["emp"], prefix="/emp")

@api_router.post("/register", status_code=status.HTTP_200_OK)
async def create_emp_registration(request: schema.Emp, database: Session = Depends(db.get_db)):
    emp = await validator.is_email_exist(request.email, database)
    if emp:
        raise HTTPException(
            status_code=400,
            detail="Email Already Exist. Try Another!"
        )

    registered_emp = await services.register_emp(request, database)
    return registered_emp
