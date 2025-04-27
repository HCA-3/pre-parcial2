from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pre_parcial2.enums import EstadoTarea, EstadoUsuario  # Importación absoluta

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
        orm_mode = True

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
        orm_mode = True