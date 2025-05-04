
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", response_model=schemas.ApplicationOut)
def create_application(application: schemas.ApplicationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_app = models.Application(
        event_name=application.event_name,
        motivation_text=application.motivation_text,
        user_id=current_user.id
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@router.get("/", response_model=list[schemas.ApplicationOut])
def get_my_applications(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Application).filter(models.Application.user_id == current_user.id).all()
