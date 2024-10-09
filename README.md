# API CRUD Usuarios

Esta API está diseñada para gestionar una base de datos de usuarios utilizando FastAPI y SQLAlchemy. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios, esta API fue creada para practicar y familiarizarme con FastAPI y python.

## Características

- **Usuarios:** Gestión de información de usuarios.

## Tecnologías Usadas

- **FastAPI**: Framework web para construir APIs.
- **SQLAlchemy**: ORM para interactuar con bases de datos.
- **Pydantic**: Para la validación de datos para hacer uso de BaseModel.

## Rutas de la API

### Usuarios (`/users`)

- **GET** `/users`: Obtiene todos los usuarios.
- **POST** `/users`: Crea un nuevo usuarios.
- **PUT** `/users`: Actualiza un usuarios existente (requiere ID).
- **DELETE** `/users/{id}`: Elimina un usuario por ID.

## Ejecución del Proyecto

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/AlejandroJimenez16/CRUD-con-FastAPI.git

2. Navega al directorio del proyecto:
   ```bash
   cd CRUD-con-FastAPI
   
3. Asegúrate de tener Python y las dependencias necesarias instaladas.
4. Ejecuta el siguiente comando para iniciar el servidor:
   ```bash
   uvicorn app:app --reload

## Acceso a Swagger

Swagger UI está disponible para facilitar la interacción con la API y para la documentación automática de las rutas. Puedes acceder a Swagger en la siguiente URL:

`http://localhost:8000/docs`

![image](https://github.com/user-attachments/assets/bc7584b2-3de0-478b-b6fb-9eb842268c7d)

