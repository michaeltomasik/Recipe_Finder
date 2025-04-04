import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import models


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
Base = declarative_base()


def get_engine():
    return create_engine(DATABASE_URL, echo=True)


def get_db():
    engine = get_engine()  # Get the engine when the DB is needed
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()