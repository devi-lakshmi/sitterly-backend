import datetime
from enum import Enum
from .database import Base
from sqlalchemy import Boolean, CheckConstraint, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    role = Column(String, nullable=False, default="")
    # Relationship with SitterProfile (one-to-one)
    sitter_profile = relationship("SitterProfile", back_populates="user")
    # Relationship with  Booking( one -to one)
    bookings = relationship("Booking", back_populates="user")
    given_reviews = relationship(
        "Review", foreign_keys="[Review.reviewer_id]", back_populates="reviewer")
    # received_reviews = relationship(
    #     "Review", foreign_keys="[Review.reviewee_id]", back_populates=" reviewee")


class SitterProfile(Base):
    __tablename__ = "sitterprofiles"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    city = Column(String)
    hourly_rate_euro = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
 # Relationship with User (many-to-one)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="sitter_profile")
 # Relationship with Booking( one to one)

    bookings = relationship("Booking", back_populates="sitter_profile")
    # received_reviews = relationship(
    #     "Review", foreign_keys="[Review.reviewee_id]", back_populates="sitter_profile")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    starts_at = Column(DateTime, default=datetime.datetime.utcnow)
    ends_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_canceled = Column(Boolean, default=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="bookings")
# Relationship with User (many-to-one)
    sitter_profile_id = Column(Integer, ForeignKey("sitterprofiles.id"))
    sitter_profile = relationship("SitterProfile", back_populates="bookings")
    review = relationship("Review", back_populates="booking")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    score = Column(Integer, CheckConstraint('score >= 1 AND score <= 5'))
    message = Column(String, nullable=True)
    for_role = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
    reviewer_id = Column(Integer, ForeignKey("users.id"))
    reviewer = relationship(
        "User", foreign_keys="[Review.reviewer_id]", back_populates="given_reviews")
    reviewee_id = Column(Integer, ForeignKey("users.id"))
    reviewee = relationship(
        "User", foreign_keys="[Review.reviewee_id]", back_populates="received_reviews")
    # sitter_profile = relationship(
    #     "SitterProfile", foreign_keys="[Review.reviewee_id]", back_populates="received_reviews")
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    booking = relationship("Booking", back_populates="review")

# ... (remaining code)
