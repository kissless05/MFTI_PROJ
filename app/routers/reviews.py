
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, database, auth

router = APIRouter(prefix="/reviews", tags=["Reviews"])
get_db = database.get_db

@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    application = db.query(models.Application).filter(models.Application.id == review.application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    db_review = models.Review(
        content=review.content,
        application_id=review.application_id,
        user_id=current_user.id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

from app import models


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(review)
    db.commit()
