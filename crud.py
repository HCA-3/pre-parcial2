from sqlalchemy.orm import Session
from models import UsuarioDB, UsuarioCreate, TareaDB, TareaCreate, EstadoUsuario

def crear_usuario(db: Session, usuario: UsuarioCreate) -> UsuarioDB:
    db_usuario = UsuarioDB(
        nombre=usuario.nombre,
        email=usuario.email,
        premium=usuario.premium,
        estado=EstadoUsuario.ACTIVO
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def adicionar_tarea(db: Session, tarea_in: TareaCreate) -> TareaDB:
    db_tarea = TareaDB(
        nombre=tarea_in.nombre,
        descripcion=tarea_in.descripcion,
        usuario_id=tarea_in.usuario_id
    )
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea