from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import schemas
from repository import userfile


router = APIRouter()


@router.post('/user', response_model= schemas.ShowUser, tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userfile.create_new_user(request, db)


@router.get('/user/{id}', response_model= schemas.ShowUser, tags=["Users"])
def get_user(id: int, db: Session = Depends(get_db)):
    return userfile.show_user(id, db)