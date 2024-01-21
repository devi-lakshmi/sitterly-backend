from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def review_sitter(db: Session, sitterReview: schemas.SitterReviewCreate, reviewer_id: int):
    booking = db.query(models.Review).filter(
        models.Review.booking_id == sitterReview.booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    db_review = models.Review(
        **sitterReview.dict(), id=sitterReview.booking_id)
    db_review.reviewer_id = reviewer_id
    db.add(db_review)
    db.commit()
    db.refresh(booking)
    return {"message": "Booking cancelled successfully"}
