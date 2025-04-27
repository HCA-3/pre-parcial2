from database import DatabaseConnection
from crud import crear_usuario, adicionar_tarea
from models import UsuarioCreate, TareaCreate

def main():
    db_conn = DatabaseConnection()
    
    with db_conn.get_db() as db:
        # Crear usuario
        usuario = crear_usuario(db, UsuarioCreate(
            nombre="Ejemplo",
            email="ejemplo@test.com",
            premium=False
        ))
        
        # Crear tarea
        tarea = adicionar_tarea(db, TareaCreate(
            nombre="Mi primera tarea",
            descripcion="Descripción de ejemplo",
            usuario_id=usuario.id
        ))
        
        print(f"Usuario creado: {usuario.nombre}")
        print(f"Tarea creada: {tarea.nombre}")

if __name__ == "__main__":
    main()