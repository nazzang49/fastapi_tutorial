from typing import Optional
from sqlalchemy.orm import Session
from . models import Emp

async def is_email_exist(email: str, db_session: Session) -> Optional[Emp]:
    """
    A  method for checking email duplication

    :param email:
    :param db_session:
    :return:
    """
    return db_session.query(Emp).filter(Emp.email == email).first()
