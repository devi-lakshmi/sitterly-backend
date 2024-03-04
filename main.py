from traceback import print_stack
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import ValidationError
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from app import database, schemas, sitterprofiles, bookings, reviews
from app.users import create_user, process_login
from app.deps import get_current_user
from app.schemas import UserBase, UserCreate, UserCredentials, Token

load_dotenv()  # take environment variables from .env.

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# sign up users
@app.get("/healthz", response_model=schemas.Healthz)
def healthz():
    return {"status": "ok"}

@app.post("/users", response_model=UserBase)
def sign_up_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, user=user)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e.msg))
    return user


# log in users


@app.post("/users/login", response_model=Token)
def login_user(user: UserCredentials, db: Session = Depends(get_db)):
    return process_login(db, user=user)


@app.post("/docslogin", response_model=Token)
def login_with_form_data(
    oauth_user: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = UserCredentials(email=oauth_user.username,
                           password=oauth_user.password)
    return process_login(db, user=user)


@app.get("/users/profile", response_model=UserBase)
def get_user_profile(user: UserBase = Depends(get_current_user)):
    return user

# Implement your own endpoints below

# get all sitterprofiles


@app.get("/getSitterProfiles", response_model=list[schemas.SitterProfile])
def read_sitter_profile(
        page: int,
        user: UserBase = Depends(get_current_user),
        db: Session = Depends(get_db)):
    results = sitterprofiles.get_sitter_profiles(
        db, user_id=user.id, page=page)
    if results is None:
        raise HTTPException(status_code=404, detail="No sitterprofiles found")
    return results

# get sitterprofile by city


@app.get("/getSitterProfileByCity", response_model=list[schemas.SitterProfile])
def read_sitter_profile(
        city: str,
        user: UserBase = Depends(get_current_user),
        db: Session = Depends(get_db)):
    results = sitterprofiles.get_sitter_profile_by_city(
        db, city=city)
    if results is None:
        raise HTTPException(status_code=404, detail="No sitterprofiles found")
    return results


# create sitterprofile


@app.post("/createSitterProfile", response_model=schemas.SitterProfile)
def create_sitter_profile(
    sitter_proffile: schemas.SitterProfileCreate,
    user: UserBase = Depends(get_current_user),   # get user from token
    db: Session = Depends(get_db)
):
    # create the list and pass in the user_id
    return sitterprofiles.create_sitter_profile(db, user_id=user.id, sitter_profile=sitter_proffile)


@app.get("/getSitterProfileById/{id}", response_model=schemas.SitterProfileBase)
def read_sitter_profile(id: int, db: Session = Depends(get_db),
                        user: UserBase = Depends(get_current_user)
                        ):
    results = sitterprofiles.get_sitter_profile(
        db, user_id=user.id, sitter_profile_id=id)
    if results is None:
        raise HTTPException(status_code=404, detail="SittterProfile not found")
    return results

# delete sitterprofile


@app.delete("/deleteSitterProfileById/{id}", response_model=schemas.SitterProfileBase)
def delete_sitter_profiles(id: int,
                           user: UserBase = Depends(get_current_user),
                           db: Session = Depends(get_db)):
    return sitterprofiles.delete_sitter_profile(db, user_id=user.id, sitter_profile_id=id)
# update sitterprofile


@app.put("/updateSitterProfile/{id}", response_model=schemas.SitterProfileBase)
def update_sitter_profile(id: int, sitter_proffile: schemas.SitterprofileUpdate,
                          user: UserBase = Depends(get_current_user),
                          db: Session = Depends(get_db)):
    results = sitterprofiles.update_sitter_profile(
        db, user_id=user.id, sitter_profile_id=id, sitter_proffile=sitter_proffile)
    if results is None:
        raise HTTPException(
            status_code=404, detail="SitterProfile not found")
    return results
# Booking API

# create bookings


@app.post("/createBookings", response_model=schemas.BookingCreate)
def create_booking(booking: schemas.BookingCreate,
                   user: UserBase = Depends(
        get_current_user),   # get user from token
    db: Session = Depends(get_db)
):
    print("booking", booking)

    # create the list and pass in the user_id
    return bookings.create_booking(db, user_id=user.id, sitter_profile_id=booking.sitter_profile_id, booking=booking)


@app.get("/bookings")
def browse_bookings(user: UserBase = Depends(
        get_current_user), db: Session = Depends(get_db)
):
    return bookings.browse_bookings(db, user_id=user.id)


@app.put("/cancelMyBooking/{id}")
def cancel_booking(id: int, user: UserBase = Depends(

        get_current_user), db: Session = Depends(get_db)
):
    return bookings.cancel_booking(db, user_id=user.id, bookingId=id)


@app.post("/reviews")
def review_sitter(sitterReview: schemas.SitterReviewCreate,  user: UserBase = Depends(
        get_current_user), db: Session = Depends(get_db)

):
    return reviews.review_sitter(db, sitterReview=sitterReview, user_id=user.id)


@app.get("/getReviews")
def browse_reviews(user: UserBase = Depends(
        get_current_user), db: Session = Depends(get_db)
):
    return reviews.browse_reviews(db, user_id=user.id)


# @app.post("/reviewParent")
# def cancel_booking(bookingId: int, user: UserBase = Depends(
#         get_current_user), db: Session = Depends(get_db)
# ):
#     return bookings.cancel_booking(db, user_id=user.id, bookingId=bookingId)
