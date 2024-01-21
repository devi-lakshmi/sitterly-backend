from fastapi import HTTPException
from sqlalchemy.orm import Session
import datetime
from . import models, schemas


def create_booking(db: Session, user_id: int, sitter_proffile_id: int, booking: schemas.BookingCreate):
    db_booking = models.Booking(
        **booking.dict(), user_id=user_id)
    db_booking.sitter_profile_id = sitter_proffile_id
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def browse_bookings(db: Session, user_id: int):
    user = db.query(models.User).filter(user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    bookings = db.query(models.Booking).filter(
        models.Booking.user_id == user_id).all()

    print(bookings)
    return bookings


def cancel_booking(db: Session, user_id: int, bookingId: int):
    booking = db.query(models.Booking).filter(
        models.Booking.id == bookingId).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.user_id != user_id:
        raise HTTPException(
            status_code=403, detail="You are not allowed to cancel")
    if booking.starts_at >= datetime.datetime.utcnow():
        raise HTTPException(
            status_code=422, detail="Cannot cancel past bookings")
    if booking.is_canceled:
        raise HTTPException(
            status_code=422, detail="Booking already cancelled")

    booking.is_canceled = True
    db.commit()
    db.refresh(booking)
    return {"message": "Booking cancelled successfully"}
