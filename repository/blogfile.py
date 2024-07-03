from sqlalchemy.orm import Session, joinedload, Query
import schemas
from models.blog_model import BlogModel
from models.user_model import UserModel
from fastapi import HTTPException, status

# def get_all(db: Session):
#     blogs =  db.query(BlogModel).all()
#     return blogs



def get_all(db: Session):
    blogs = db.query(BlogModel).options(
        joinedload(BlogModel.creator).load_only(UserModel.id, UserModel.name, UserModel.email)
    ).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = BlogModel(
        title=request.title,
        body=request.body,
        user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    



def update(id:int, request: schemas.BlogUpdate, db:Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()

    if request.title and request.title!=None and request.title!="":
        blog.title = request.title
    
    if request.body and request.body!=None and request.body!="":
        blog.body = request.body

    db.commit()
    db.refresh(blog)
    return blog



def show(id:int, db:Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    return blog



def delete(id:int, db:Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    db.delete(blog)
    db.commit()
    return blog



# Fetch blogs by user id
# def get_user_blogs(user_id: int, db: Session):
#     blogs = db.query(BlogModel).filter(BlogModel.user_id == user_id).all()
#     return blogs


def get_user_blogs(user_id: int, skip: int, limit: int, db:Session):
      blogs = db.query(BlogModel).options(
        joinedload(BlogModel.creator).load_only(UserModel.id, UserModel.name, UserModel.email)
    ).filter(BlogModel.user_id == user_id).offset(skip).limit(limit).all()
      return blogs