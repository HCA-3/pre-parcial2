from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    def __init__(self, db_url: str = "sqlite:///./tareas_usuarios.db"):
        self.engine = create_engine(
            db_url,
            connect_args={"check_same_thread": False} if "sqlite" in db_url else {}
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()