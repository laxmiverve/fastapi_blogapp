from fastapi import FastAPI
from database import engine
from database import Base
from routers import blog, user, authentication
from fastapi_pagination import Page, add_pagination, paginate



app = FastAPI()
add_pagination(app)


Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)