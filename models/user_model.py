
# SQLAlchemy Models
from database import Base
# from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship



# create new user
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('BlogModel', back_populates='creator',  primaryjoin='foreign(BlogModel.user_id) == remote(UserModel.id)', lazy='joined')