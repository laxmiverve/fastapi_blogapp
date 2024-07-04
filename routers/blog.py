from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import schemas, oauth2
from database import get_db
from repository import blogfile



from fastapi_pagination import Page, paginate



router = APIRouter(
    # prefix="/blog",     // you can remove all the blog word from the route
    tags=["Blogs"]
)



# GET -> get all data from database
@router.get('/blog', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogfile.get_all(db)


@router.get('/blog/{id}', status_code = 200, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db)):
    return blogfile.show(id, db)


@router.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blogfile.create(request, db)


@router.put('/blog/{id}')    #  tags=["blogs"] -> These sre called Doc tag 
def update(id:int, request: schemas.BlogUpdate, db: Session = Depends(get_db)):
    return blogfile.update(id, request, db)



@router.delete('/blog/{id}')
def delete(id, db: Session = Depends(get_db)):
    return blogfile.delete(id,db)




# fetch blogs by user id 
# implement pagination

# @router.get('/blogs/{user_id}', response_model=List[schemas.ShowBlog])
# def get_user_blogs(user_id: int, skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
#     return blogfile.get_user_blogs(user_id, skip, limit, db)




@router.get('/blogs/{user_id}', response_model=Page[schemas.ShowBlog])
def get_user_blogs(user_id: int, db: Session = Depends(get_db)):
    blogs = blogfile.get_user_blogs(user_id, db)
    return paginate(blogs)