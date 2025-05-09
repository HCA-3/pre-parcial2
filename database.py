from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base

class DatabaseConnection:
    def __init__(self, db_url: str = "sqlite:///./tareas.db"):
        self.engine = create_engine(
            db_url,
            connect_args={"check_same_thread": False} if "sqlite" in db_url else {}
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def get_session(self) -> Session:
        """Devuelve una sesión de base de datos que puede usarse con with"""
        return self.SessionLocal()