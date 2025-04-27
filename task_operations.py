from sqlalchemy.orm import Session
from pre_parcial2.models_sqlalchemy import TareaDB  # Importación absoluta
from pre_parcial2.models_pydantic import TareaCreate  # Importación absoluta

def adicionar_tarea(db: Session, tarea_in: TareaCreate) -> TareaDB:
    """
    Crea una nueva tarea en la base de datos.

    Args:
        db (Session): La sesión de la base de datos SQLAlchemy.
        tarea_in (TareaCreate): Los datos de la tarea a crear (modelo Pydantic).
                               Se espera que incluya nombre, descripción (opcional) y usuario_id.

    Returns:
        TareaDB: El objeto Tarea recién creado y guardado en la base de datos.

    Raises:
        ValueError: Si el usuario especificado por tarea_in.usuario_id no existe.
        Exception: Cualquier otra excepción que pueda ocurrir durante la operación de BD.
    """

    db_tarea = TareaDB(
        nombre=tarea_in.nombre,
        descripcion=tarea_in.descripcion,
        usuario_id=tarea_in.usuario_id
    )

    try:
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        return db_tarea

    except Exception as e:
        db.rollback()
        raise e