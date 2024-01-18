from .database import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    # Indicates if a User is active and is allowed to log in.
    disabled = Column(Boolean, default=False)
