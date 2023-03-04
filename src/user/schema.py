from pydantic import BaseModel, constr, EmailStr

class Emp(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr