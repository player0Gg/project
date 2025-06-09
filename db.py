from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root@localhost:3306/last_project')
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()


def database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()