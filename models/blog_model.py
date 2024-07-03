from database import Base
# from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class BlogModel(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(50))
    body = Column(String(100))
    
    user_id = Column(Integer, ForeignKey('users.id'))    # Relationships between columns of two tables 
    creator = relationship('UserModel', back_populates= 'blogs', primaryjoin='foreign(BlogModel.user_id) == remote(UserModel.id)', lazy='joined') 