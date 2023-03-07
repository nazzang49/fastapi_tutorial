from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db import Base
from . import hashing


class User(Base):
    __tablename__ = "emp"

    ######################
    # CREATE TABLE emp (
    # id SERIAL PRIMARY KEY,
    # name VARCHAR(50),
    # email VARCHAR(255) UNIQUE
    # );
    ######################

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)

    def __init__(self, name, email, *args, **kwargs):
        self.name = name
        self.email = email
        # self.password = hashing.get_password_hash(password)

    # def check_password(self, password):
    #     return hashing.verify_password(self.password, password)
