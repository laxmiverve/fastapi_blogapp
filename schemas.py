
# Pydantic models

from pydantic import BaseModel
from typing import Optional, List


class Login(BaseModel):
    email: str
    password: str


class Blog(BaseModel):
    title: str
    body: str
    user_id: int
   


class BlogCreate(BaseModel):
    pass



class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None



# User create
class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True



class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    # user_id: int  
    
    class Config():
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


