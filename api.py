from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pre_parcial2 import task_operations, models_pydantic
from pre_parcial2.database import DatabaseConnection

db_connection = DatabaseConnection()

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = db_connection.get_db()
    try:
        yield next(db)
    finally:
        next(db)

@app.post("/tareas/", response_model=models_pydantic.Tarea)
def crear_tarea(tarea: models_pydantic.TareaCreate, db: Session = Depends(get_db)):
    try:
        return task_operations.adicionar_tarea(db=db, tarea_in=tarea)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ... (Aquí puedes agregar más rutas para obtener, actualizar, eliminar tareas, etc.)