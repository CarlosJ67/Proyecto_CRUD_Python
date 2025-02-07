"""
Este módulo define el modelo de usuario para la base de datos.
"""

import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base

class TipoUsuario(str, enum.Enum):
    """
    Enumeración para los tipos de usuario.
    """
    ALUMNO = "Alumno"
    PROFESOR = "Profesor"
    SECRETARIA = "Secretaria"
    LABORATORISTA = "Laboratorista"
    DIRECTIVO = "Directivo"
    ADMINISTRATIVO = "Administrativo"

class Status(str, enum.Enum):
    """
    Enumeración para los estados de usuario.
    """
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    BLOQUEADO = "Bloqueado"
    SUSPENDIDO = "Suspendido"

class User(Base):
    """
    Modelo de usuario para la base de datos.
    """
    __tablename__ = "tbb_usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primer_apellido = Column(String(60))
    segundo_apellido = Column(String(60))
    tipo_usuario = Column(Enum(TipoUsuario))
    nombre_usuario = Column(String(60), unique=True, index=True)
    correo_electronico = Column(String(100), unique=True, index=True)
    contrasena = Column(String(100))
    nombre_telefono = Column(String(20))
    status = Column(Enum(Status))
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    def __repr__(self):
        return (
            f"<User(nombre_usuario={self.nombre_usuario}, "
            f"correo_electronico={self.correo_electronico})>"
        )

    def get_full_name(self):
        """
        Devuelve el nombre completo del usuario.
        """
        return f"{self.nombre} {self.primer_apellido} {self.segundo_apellido}"

# Aseguramos que haya una nueva línea al final del archivo
