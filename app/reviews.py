# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from . import models, schemas


# def review_sitter(db: Session, reviewer_id: int, user_id:int,sitterReview: schemas.SitterReviewCreate):
#     booking = db.query(models.Review).filter(
#         models.Review.booking_id == sitterReview.booking_id).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking not found")
#     db_review = models.Review(
#         **sitterReview.dict(), id=sitterReview.booking_id)
#     db_review.reviewer_id = reviewer_id
#     db.add(db_review)
#     db.commit()
#     db.refresh(booking)
    # return {"message": "Booking cancelled successfully"}


# def create_booking(db: Session, user_id: int, sitter_proffile_id: int, booking: schemas.BookingCreate):
#     db_booking = models.Booking(
#         **booking.dict(), user_id=user_id)
#     db_booking.sitter_profile_id = sitter_proffile_id
#     db.add(db_booking)
#     db.commit()
#     db.refresh(db_booking)
#     return db_booking
