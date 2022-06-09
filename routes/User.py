from fastapi import APIRouter, status, HTTPException #Definir las rutas por separado.
from config.db import conn
from models.userModel import users
from schemas.userSchema import *
from werkzeug.security import check_password_hash, generate_password_hash
from validators.userValidators import *

user = APIRouter()

# LISTAR TODOS LOS USUARIO
@user.get('/user/list_user', response_model = list[User])
def getUsers():
    return conn.execute(users.select()).fetchall()

# ACTUALIZAR USUARIO
@user.patch('/user/change_password/{id}')
def updatePassword(id: str ,user : PasswordUpdate):
    if empty(user.oldPassword) == False or empty(user.newPassword) == False or empty(id) == False:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Los campos no pueden ser vacios.") 

    query = conn.execute(users.select().where(users.c.id == id)).fetchone()

    if query is None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Usuario no existe.")
    
    if not check_password_hash(query['password'], user.oldPassword):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "La contrasena anterior es erronea.")

    conn.execute(users.update().values(password = generate_password_hash(user.newPassword)).where(users.c.id == id))
    return "Updated"


# CAMBIAR LA CONTRASENA, DEBERIA SER PATH YA QUE ES UN UNICO ATRIBUTO
