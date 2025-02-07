"""
Este módulo define las operaciones CRUD para el modelo de usuario.
"""

from datetime import datetime
from sqlalchemy.orm import Session
from models.user import User
from schemas.users import UserCreate, UserUpdate

def get_users(db: Session, skip: int = 0, limit: int = 0):
    """
    Obtiene una lista de usuarios con paginación.
    """
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    """
    Obtiene un usuario por su ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_usuario(db: Session, nombre_usuario: str):
    """
    Obtiene un usuario por su nombre de usuario.
    """
    return db.query(User).filter(User.nombre_usuario == nombre_usuario).first()

def create_user(db: Session, user: UserCreate):
    """
    Crea un nuevo usuario.
    """
    db_user = User(
        nombre=user.nombre,
        primer_apellido=user.primer_apellido,
        segundo_apellido=user.segundo_apellido,
        tipo_usuario=user.tipo_usuario,
        nombre_usuario=user.nombre_usuario,
        correo_electronico=user.correo_electronico,
        contrasena=user.contrasena,
        nombre_telefono=user.nombre_telefono,
        status=user.status,
        fecha_registro=datetime.utcnow(),
        fecha_actualizacion=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    """
    Actualiza un usuario existente.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for var, value in vars(user).items():
            if value:
                setattr(db_user, var, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """
    Elimina un usuario por su ID.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Aseguramos que haya una nueva línea al final del archivo
