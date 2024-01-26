from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

# get sitterprofiles


def get_sitter_profiles(db: Session, user_id: int, skip: int = 0, limit: int = 20):
    sitter_profiles = db.query(models.SitterProfile).filter(user_id == user_id).offset(
        skip).limit(limit).all()
    print(sitter_profiles)
    return sitter_profiles

# create  sitterprofle


def create_sitter_profile(db: Session, user_id: int, sitter_profile: schemas.SitterProfileCreate):
    db_sitter_profile = models.SitterProfile(
        **sitter_profile.dict(), user_id=user_id)
    db.add(db_sitter_profile)
    db.commit()
    db.refresh(db_sitter_profile)
    return db_sitter_profile

# get one sitterprofile


def get_sitter_profile(db: Session, user_id: int, sitter_profile_id: int):
    sitter_profile = db.query(models.SitterProfile).filter(
        models.SitterProfile.id == sitter_profile_id).filter(models.SitterProfile.user_id == user_id).first()
    return sitter_profile

# delete sitterprofile


def delete_sitter_profile(db: Session, user_id: int, sitter_profile_id: int):
    sitter_proffile = db.query(models.SitterProfile).filter(
        models.SitterProfile.id == sitter_profile_id).filter(models.SitterProfile.user_id == user_id).first()
    if sitter_proffile is None:
        raise HTTPException(status_code=404, detail="sitterProfile not found")
    db.delete(sitter_proffile)
    db.commit()
    return sitter_proffile
# get sitterprofile by name


def get_sitter_profile_by_city(db: Session, city: str):
    sitter_profiles = db.query(models.SitterProfile).filter(
        models.SitterProfile.city == city).first()
    print(sitter_profiles)
    return sitter_profiles
# update one sitterprofile


def update_sitter_profile(db: Session, user_id: int, sitter_profile_id: int,  sitter_profile_update: schemas.SitterprofileUpdate):
    updated_sitter_profile = db.query(models.SitterProfile).filter(
        models.SitterProfile.id == sitter_profile_id).filter(models.SitterProfile.user_id == user_id).first()

    updated_sitter_profile.city = sitter_profile_update.city

    if updated_sitter_profile is None:
        raise HTTPException(status_code=404, detail="sitterprofile not found")
    db.commit()
    db.refresh(updated_sitter_profile)
    return updated_sitter_profile
