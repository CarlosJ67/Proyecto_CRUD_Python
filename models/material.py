"""
Este módulo define el modelo de material para la base de datos.
"""

import enum
from sqlalchemy import Column, Integer, String, Enum
from config.db import Base

class EstadoMaterial(str, enum.Enum):
    """
    Enumeración para los estados de material.
    """
    DISPONIBLE = "Disponible"
    PRESTADO = "Prestado"
    MANTENIMIENTO = "En Mantenimiento"

class Material(Base):
    """
    Modelo de material para la base de datos.
    """
    __tablename__ = "tbb_material"

    id_material = Column(Integer, primary_key=True, autoincrement=True)
    tipo_material = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=True)
    modelo = Column(String(100), nullable=True)
    estado = Column(Enum(EstadoMaterial), nullable=False)

    def __repr__(self):
        return (
            f"<Material(id_material={self.id_material}, tipo_material={self.tipo_material}, "
            f"marca={self.marca}, modelo={self.modelo}, estado={self.estado})>"
        )

    def get_material_info(self):
        """
        Devuelve la información del material.
        """
        return (
            f"Material {self.id_material}: Tipo {self.tipo_material}, "
            f"Marca {self.marca}, Modelo {self.modelo}, Estado {self.estado}"
        )

# Aseguramos que haya una nueva línea al final del archivo
