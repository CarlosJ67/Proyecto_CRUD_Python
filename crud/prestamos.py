# Importación de los modelos y esquemas relacionados con Prestamo
import models.prestamo
import schemas.prestamo
from sqlalchemy.orm import Session

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de préstamos con paginación.
    
    :param db: Sesión de la base de datos.
    :param skip: Número de registros a omitir (por defecto 0).
    :param limit: Número máximo de registros a retornar (por defecto 10).
    :return: Lista de préstamos.
    """
    return db.query(models.prestamo.Prestamo).offset(skip).limit(limit).all()

def get_prestamo(db: Session, id: int):
    """
    Obtiene un préstamo específico por su ID.
    
    :param db: Sesión de la base de datos.
    :param id: ID del préstamo a buscar.
    :return: Objeto Prestamo si se encuentra, de lo contrario None.
    """
    return db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id_prestamo == id).first()

def create_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoCreate):
    """
    Crea un nuevo préstamo en la base de datos.
    
    :param db: Sesión de la base de datos.
    :param prestamo: Datos del préstamo a crear, basado en el esquema PrestamoCreate.
    :return: Objeto Prestamo recién creado.
    """
    db_prestamo = models.prestamo.Prestamo(**prestamo.dict())  # Se crea la instancia del préstamo con los datos recibidos
    db.add(db_prestamo)  # Se agrega el préstamo a la sesión de la base de datos
    db.commit()  # Se confirma la transacción
    db.refresh(db_prestamo)  # Se actualiza la instancia con los datos finales de la BD
    return db_prestamo

def update_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoUpdate, id: int):
    """
    Actualiza los datos de un préstamo existente en la base de datos.
    
    :param db: Sesión de la base de datos.
    :param prestamo: Datos del préstamo a actualizar, basado en el esquema PrestamoUpdate.
    :param id: ID del préstamo a actualizar.
    :return: Objeto Prestamo actualizado o None si no se encontró.
    """
    db_prestamo = db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id_prestamo == id).first()
    if db_prestamo:
        # Se actualizan solo los campos que han sido proporcionados en la solicitud
        for key, value in prestamo.dict(exclude_unset=True).items():
            setattr(db_prestamo, key, value)
        db.commit()  # Se confirma la transacción
        db.refresh(db_prestamo)  # Se actualiza la instancia con los cambios reflejados en la BD
    return db_prestamo

def delete_prestamo(db: Session, id: int):
    """
    Elimina un préstamo de la base de datos por su ID.
    
    :param db: Sesión de la base de datos.
    :param id: ID del préstamo a eliminar.
    :return: Objeto Prestamo eliminado o None si no se encontró.
    """
    db_prestamo = db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id_prestamo == id).first()
    if db_prestamo:
        db.delete(db_prestamo)  # Se marca el préstamo para eliminación
        db.commit()  # Se confirma la transacción
    return db_prestamo
