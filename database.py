from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()

Base = declarative_base()

user = 'root'
password = 'login12*'
host = 'localhost'
database = 'demo'


connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()