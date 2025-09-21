from app.core.database import SessionLocal

def get_db():
    """Dependency untuk mendapatkan sesi database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()