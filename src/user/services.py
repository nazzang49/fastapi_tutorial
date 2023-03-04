from fastapi import HTTPException, status
from . import models

async def register_emp(request, database) -> models.Emp:
    emp = models.Emp(name=request.name, email=request.email)
    database.add(emp)
    database.commit()
    database.refresh(emp)
    return emp