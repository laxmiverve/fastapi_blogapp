from sqlalchemy.orm import Session
import schemas
from fastapi import HTTPException, status
from models.user_model import UserModel
from hashing import Hash



def create_new_user(request: schemas.User, db:Session):
    new_user = UserModel(
        name = request.name,
        email = request.email,
        password = Hash.bcrypt(request.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




def show_user(id:int, db:Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")

    return user