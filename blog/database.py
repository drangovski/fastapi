from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# LOAD LOCAL SETTINGS
try:
    from .local_settings import *
except ImportError:
    pass

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Get the database and close connection when completed
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()