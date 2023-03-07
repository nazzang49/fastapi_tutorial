from sqlalchemy.orm import Session

from . services import *

async def get_user(request, database: Session):
    database.get()