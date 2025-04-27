from database import DatabaseConnection
from crud import crear_usuario, adicionar_tarea
from models import UsuarioCreate, TareaCreate

def main():
    db_conn = DatabaseConnection()
    
    # Usamos get_session() que devuelve un Session directamente
    with db_conn.get_session() as db:
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
        
        print(f"Usuario creado: {usuario.nombre} (ID: {usuario.id})")
        print(f"Tarea creada: {tarea.nombre} (Estado: {tarea.estado})")

if __name__ == "__main__":
    main()