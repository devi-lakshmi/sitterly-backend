from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def review_sitter(db: Session, sitterReview: schemas.SitterReviewCreate, user_id: int):
    db_booking = db.query(models.Booking).filter(
        models.Booking.id == sitterReview.booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=422, detail="Booking not found")
    db_review = models.Review(
        **sitterReview.dict())
    db_sitterProfile = db.query(models.SitterProfile).filter(
        models.SitterProfile.id == db_booking.sitter_profile_id).first()
    db_review.reviewer_id = user_id
    db_review.reviewee_id = db_sitterProfile.user_id
    db_review.sitter_profile_id = db_booking.sitter_profile_id
    db_review.for_role = "Parent"
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return {"message": "Review created successfully"}
