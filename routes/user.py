from fastapi import APIRouter
from config.db import conexion #Conexion
from models.user import users #Tabla
from schemas.user import User #Clase user para introducir datos

from cryptography.fernet import Fernet #Encriptar

key = Fernet.generate_key()

f = Fernet(key)

user = APIRouter()

@user.get('/users', tags=["Users"])
def get_user():
    valores = []
    for filas in conexion.execute(users.select()).fetchall():
        dic = {
            "id": filas.id,
            "name": filas.name,
            "email": filas.email,
            "password": filas.password
        }
        valores.append(dic)
    return valores

@user.post('/users', tags=["Users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email, "password": f.encrypt(user.password.encode('utf-8'))}
    conexion.execute(users.insert().values(new_user))
    conexion.commit()
    return "Todo bien"

@user.put('/user', tags=["Users"])
def update(id: int, user: User):
    conexion.execute(users.update().values(name = user.name, email = user.email, password = f.encrypt(user.password.encode('utf-8'))).where(users.c.id == id))
    conexion.commit()
    return "Actualizado"

@user.delete('/user/{id}', tags=["Users"])
def delete(id: int):
    conexion.execute(users.delete().where(users.c.id == id))
    conexion.commit()
    return "Usuario con id ", {id}, "eliminado"


   
    

    
