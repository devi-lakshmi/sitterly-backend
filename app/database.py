# import SQLAlchemy parts
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
database_url = os.environ.get("DATABASE_URL")
print("database_url:"+database_url)

# create SQLAlchemy engine
engine = create_engine(database_url)

# create SessionLocal class with sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class, will use later to create models or classes
Base = declarative_base()
