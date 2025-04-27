from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime
from pre_parcial2.enums import EstadoTarea, EstadoUsuario  # Importación absoluta

Base = declarative_base()

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    estado = Column(Enum(EstadoUsuario), default=EstadoUsuario.ACTIVO)
    premium = Column(Boolean, default=False)

    tareas = relationship("TareaDB", back_populates="usuario")

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