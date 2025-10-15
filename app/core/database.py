from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
# ================= CONFIG =================
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


""""Create the SQLAlchemy engine."""
engine = create_engine(DATABASE_URL)

"""SessionLocal untuk dependency injection di FastAPI."""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""Base class untuk model ORM."""
Base = declarative_base()