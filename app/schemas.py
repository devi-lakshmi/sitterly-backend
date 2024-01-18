from pydantic import BaseModel, model_validator

# Note how this base model does not expose the password.


class UserBase(BaseModel):
    id: int
    email: str

# We allow users to sign up with email and password


class UserCreate(BaseModel):
    email: str
    password: str

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


class UserCredentials(BaseModel):
    email: str
    password: str

# This is the schema for the database model


class User(UserBase):
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    exp: int
    sub: str
