from pydantic import BaseModel, constr, EmailStr

"""
Schema = DTO
"""
class User(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr

class UserItem(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True