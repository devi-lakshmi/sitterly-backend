import datetime
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
   # Indicates if a User is active and is allowed to log in.
    disabled = Column(Boolean, default=False)
    # Relationship with SitterProfile (one-to-one)
    sitter_profile = relationship("SitterProfile", back_populates="user")


class SitterProfile(Base):
    __tablename__ = "sitterprofiles"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    city = Column(String)
    hourly_rate_euro = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
 # Relationship with User (many-to-one)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="sitter_profile")
