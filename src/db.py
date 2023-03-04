from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import config

db_username = config.DATABASE_USERNAME
db_password = config.DATABASE_PASSWORD
db_host = config.DATABASE_HOST
db_name = config.DATABASE_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()