# CRUD_Python_MYSQL

Este proyecto es una API para gestionar usuarios, materiales y préstamos utilizando FastAPI, SQLAlchemy y MySQL.

## Estructura del Proyecto

```
CRUD_Python_MYSQL/
│-- crud/               # Operaciones CRUD para usuarios, materiales y préstamos
│-- models/             # Definición de modelos de base de datos
│-- schemas/            # Esquemas Pydantic para validación de datos
│-- database.py         # Configuración de la base de datos
│-- main.py             # Punto de entrada de la API
│-- requirements.txt    # Dependencias del proyecto
│-- README.md           # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/CarlosJ67/CRUD_Python_MYSQL.git
    cd CRUD_Python_MYSQL
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv EntornoPY
    source EntornoPY/bin/activate  # En Windows usa `EntornoPY\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura la base de datos en `database.py`:
    ```python
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"
    ```

## Uso

1. Inicia la aplicación:
    ```sh
    uvicorn main:app --reload
    ```

2. Abre tu navegador y ve a `http://127.0.0.1:8000/docs` para ver la documentación interactiva de la API generada por Swagger.

## Estructura de los Modelos

### Usuario (`models/user.py`)
Define el modelo de usuario con los siguientes campos:
- `id`
- `nombre`
- `primer_apellido`
- `segundo_apellido`
- `tipo_usuario`
- `nombre_usuario`
- `correo_electronico`
- `contrasena`
- `numero_telefono`
- `status`
- `fecha_registro`
- `fecha_actualizacion`

### Material (`models/material.py`)
Define el modelo de material con los siguientes campos:
- `id_material`
- `tipo_material`
- `marca`
- `modelo`
- `estado`

### Préstamo (`models/prestamo.py`)
Define el modelo de préstamo con los siguientes campos:
- `id_prestamo`
- `id_usuario`
- `id_material`
- `fecha_prestamo`
- `fecha_devolucion`
- `estado`

## Operaciones CRUD

### Usuarios (`crud/users.py`)
- `get_users`: Obtiene una lista de usuarios con paginación.
- `get_user`: Obtiene un usuario por su ID.
- `get_user_by_usuario`: Obtiene un usuario por su nombre de usuario.
- `create_user`: Crea un nuevo usuario.
- `update_user`: Actualiza un usuario existente.
- `delete_user`: Elimina un usuario por su ID.

### Materiales (`crud/materials.py`)
- `get_materials`: Obtiene una lista de materiales con paginación.
- `get_material`: Obtiene un material por su ID.
- `create_material`: Crea un nuevo material.
- `update_material`: Actualiza un material existente.
- `delete_material`: Elimina un material por su ID.

### Préstamos (`crud/prestamos.py`)
- `get_prestamos`: Obtiene una lista de préstamos con paginación.
- `get_prestamo`: Obtiene un préstamo por su ID.
- `create_prestamo`: Crea un nuevo préstamo.
- `update_prestamo`: Actualiza un préstamo existente.
- `delete_prestamo`: Elimina un préstamo por su ID.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en GitHub.
