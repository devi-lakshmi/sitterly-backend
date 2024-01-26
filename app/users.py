from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import (
    create_access_token,
    get_hashed_password,
    verify_password
)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_hashed_password(user.password)

    db_user = db.query(models.User).filter(
        models.User.email == user.email).first()

    if db_user:
        raise HTTPException(
            status_code=403,
            detail="Email address already exists"
        )
    db_user = models.User(
        email=user.email, password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def process_login(db: Session, user: schemas.UserCredentials):
    db_user = db.query(models.User).filter(
        models.User.email == user.email).first()

    user_password_error = "Incorrect email or password"

    if db_user is None:
        raise HTTPException(status_code=401, detail=user_password_error)

    if db_user.disabled:
        raise HTTPException(
            status_code=401,
            detail="Your account has been deactivated, please contact support."
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail=user_password_error)

    return {
        "access_token": create_access_token(
            f"{db_user.id}:{db_user.email}"
        ),
        "token_type": "bearer"
    }
