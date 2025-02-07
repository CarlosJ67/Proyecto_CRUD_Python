"""
Este módulo define el modelo de préstamo para la base de datos.
"""

import enum
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from config.db import Base

class EstadoPrestamo(str, enum.Enum):
    """
    Enumeración para los estados de préstamo.
    """
    ACTIVO = "Activo"
    DEVUELTO = "Devuelto"
    VENCIDO = "Vencido"

class Prestamo(Base):
    """
    Modelo de préstamo para la base de datos.
    """
    __tablename__ = "tbb_prestamo"

    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('tbb_usuario.id'), nullable=False)
    id_material = Column(Integer, ForeignKey('tbb_material.id_material'), nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)
    estado = Column(Enum(EstadoPrestamo), nullable=False)

    def __repr__(self):
        return (
            f"<Prestamo(id_prestamo={self.id_prestamo}, "
            f"id_usuario={self.id_usuario}, id_material={self.id_material}, "
            f"fecha_prestamo={self.fecha_prestamo}, estado={self.estado})>"
        )

    def get_prestamo_info(self):
        """
        Devuelve la información del préstamo.
        """
        return (
            f"Préstamo {self.id_prestamo}: Usuario {self.id_usuario}, "
            f"Material {self.id_material}, Estado {self.estado}"
        )

# Aseguramos que haya una nueva línea al final del archivo
