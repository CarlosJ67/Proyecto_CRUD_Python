# Importación de los modelos y esquemas relacionados con Material
import models.material
import schemas.material
from sqlalchemy.orm import Session

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de materiales con paginación.
    
    :param db: Sesión de la base de datos.
    :param skip: Número de registros a omitir (por defecto 0).
    :param limit: Número máximo de registros a retornar (por defecto 10).
    :return: Lista de materiales.
    """
    return db.query(models.material.Material).offset(skip).limit(limit).all()

def get_material(db: Session, id: int):
    """
    Obtiene un material específico por su ID.
    
    :param db: Sesión de la base de datos.
    :param id: ID del material a buscar.
    :return: Objeto Material si se encuentra, de lo contrario None.
    """
    return db.query(models.material.Material).filter(models.material.Material.id_material == id).first()

def create_material(db: Session, material: schemas.material.MaterialCreate):
    """
    Crea un nuevo material en la base de datos.
    
    :param db: Sesión de la base de datos.
    :param material: Datos del material a crear, basado en el esquema MaterialCreate.
    :return: Objeto Material recién creado.
    """
    db_material = models.material.Material(**material.dict())  # Se crea la instancia del material con los datos recibidos
    db.add(db_material)  # Se agrega el material a la sesión de la base de datos
    db.commit()  # Se confirma la transacción
    db.refresh(db_material)  # Se actualiza la instancia con los datos finales de la BD
    return db_material

def update_material(db: Session, material: schemas.material.MaterialUpdate, id: int):
    """
    Actualiza los datos de un material existente en la base de datos.
    
    :param db: Sesión de la base de datos.
    :param material: Datos del material a actualizar, basado en el esquema MaterialUpdate.
    :param id: ID del material a actualizar.
    :return: Objeto Material actualizado o None si no se encontró.
    """
    db_material = db.query(models.material.Material).filter(models.material.Material.id_material == id).first()
    if db_material:
        # Se actualizan solo los campos que han sido proporcionados en la solicitud
        for key, value in material.dict(exclude_unset=True).items():
            setattr(db_material, key, value)
        db.commit()  # Se confirma la transacción
        db.refresh(db_material)  # Se actualiza la instancia con los cambios reflejados en la BD
    return db_material

def delete_material(db: Session, id: int):
    """
    Elimina un material de la base de datos por su ID.
    
    :param db: Sesión de la base de datos.
    :param id: ID del material a eliminar.
    :return: Objeto Material eliminado o None si no se encontró.
    """
    db_material = db.query(models.material.Material).filter(models.material.Material.id_material == id).first()
    if db_material:
        db.delete(db_material)  # Se marca el material para eliminación
        db.commit()  # Se confirma la transacción
    return db_material
