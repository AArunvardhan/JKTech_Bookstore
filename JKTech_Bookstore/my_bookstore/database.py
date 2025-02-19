from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, SQLModel
# database.py
from sqlalchemy.orm import declarative_base  # New import location

DATABASE_URL = "sqlite:///./test.db"  # Example using SQLite
Base = declarative_base()


class UserCredentials(SQLModel, table=True):
    __tablename__ = "user_credentials"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(index=True, unique=True)
    password: str


# database.py
# database.py
class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(index=True)  # Change from 'name' to 'title'
    author: str = Field(index=True)
    published_year: int
    book_summary: str


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLModel.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
