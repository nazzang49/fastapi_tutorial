from typing import Optional
from sqlalchemy.orm import Session
from . models import User

async def is_email_exist(email: str, db_session: Session) -> Optional[User]:
    """
    A  method for checking email duplication

    :param email:
    :param db_session:
    :return:
    """
    return db_session.query(User).filter(User.email == email).first()
