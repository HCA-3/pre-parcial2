import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Enums
class EstadoTarea(str, enum.Enum):
    PENDIENTE = "Pendiente"
    EN_EJECUCION = "En ejecución"
    REALIZADA = "Realizada"
    CANCELADA = "Cancelada"

class EstadoUsuario(str, enum.Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    ELIMINADO = "Eliminado"

# Modelo SQLAlchemy - Usuario
class UsuarioDB(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    estado = Column(Enum(EstadoUsuario), default=EstadoUsuario.ACTIVO)
    premium = Column(Boolean, default=False)
    tareas = relationship("TareaDB", back_populates="usuario")

# Modelo SQLAlchemy - Tarea
class TareaDB(Base):
    __tablename__ = "tareas"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estado = Column(Enum(EstadoTarea), default=EstadoTarea.PENDIENTE)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("UsuarioDB", back_populates="tareas")

# Modelos Pydantic
class UsuarioBase(BaseModel):
    nombre: str
    email: str
    premium: bool = False

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    estado: EstadoUsuario
    
    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes

class TareaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class TareaCreate(TareaBase):
    usuario_id: int

class Tarea(TareaBase):
    id: int
    fecha_creacion: datetime
    fecha_modificacion: datetime
    estado: EstadoTarea
    usuario_id: int
    
    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes