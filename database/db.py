from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv() # Loading environment variables from .env file

# Fetching the data from the database (PostGres)

engine = create_engine(
    os.getenv("SQLALCHEMY_DATABASE_URI")
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()