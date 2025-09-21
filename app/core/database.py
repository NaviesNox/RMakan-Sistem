from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""URL for the database connection."""
DATABASE_URL = "postgresql://postgres.kayxgxssweodqayhvgtm:us2dLzqJpiZueXTf@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres"

""""Create the SQLAlchemy engine."""
engine = create_engine(DATABASE_URL)

"""SessionLocal untuk dependency injection di FastAPI."""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""Base class untuk model ORM."""
Base = declarative_base()