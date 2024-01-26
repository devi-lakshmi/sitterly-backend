from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Union
from typing import List

# Note how this base model does not expose the password.


class UserBase(BaseModel):
    id: int
    email: str
    role: str

# We allow users to sign up with email and password


class UserCreate(BaseModel):
    email: str
    password: str
    role: str

    @model_validator(mode='after')
    def check_email(self) -> 'UserCreate':
        email = self.email

        if email is None:
            raise ValueError('email is required')

        # this is not how you validate email addresses
        if email is not None and len(email) < 5:
            raise ValueError('please enter a valid email address')

        return self

    @model_validator(mode='after')
    def check_password_length(self) -> 'UserCreate':
        password = self.password

        if password is None:
            raise ValueError('password is required')

        if password is not None and len(password) < 4:
            raise ValueError('password must be at least 4 characters long')

        return self

    @model_validator(mode='after')
    def check_role(self) -> 'UserCreate':
        role = self.role
        if role is None:
            raise ValueError('role is required')
        return self


class UserCredentials(BaseModel):
    email: str
    password: str

# This is the schema for the database model


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    exp: int
    sub: str


class SitterProfileBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    city: str
    hourly_rate_euro: float
    created_at: datetime
    updated_at: datetime


class SitterProfileCreate(BaseModel):
    first_name: str
    last_name: str
    city: str
    hourly_rate_euro: float


class SitterprofileUpdate(BaseModel):
    city: str


class SitterProfile(SitterProfileBase):
    user_id: int

    class Config:
        from_attributes = True


class BookingBase(BaseModel):
    id: int
    starts_at: datetime
    ends_at: datetime
    is_canceled: bool
    description: str
    created_at: datetime
    updated_at: datetime


class User(UserBase):
    id: int
    sitter_profile: SitterProfileCreate
    bookings: List[BookingBase] = []

    class Config:
        from_attributes = True


class BookingCreate(BaseModel):
    starts_at: datetime
    ends_at: datetime
    is_canceled: bool = False
    sitter_profile_id: int


class Booking(BookingBase):
    user: User
    sitter_profile: SitterProfileCreate

    class Config:
        from_attributes = True


class ReviewBase(BaseModel):
    id: int
    score: int
    message: str
    for_role: str
    created_at: datetime
    updated_at: datetime


class SitterReviewCreate(BaseModel):
    score: int
    message: str
    booking_id: int


class ParentReviewCreate(BaseModel):
    reviewee_id: int
    booking_id: int
