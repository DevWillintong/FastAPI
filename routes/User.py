from tabnanny import check
from fastapi import APIRouter, status, HTTPException #Definir las rutas por separado.
from config.db import conn
from models.userModel import users
from schemas.userSchema import *
from werkzeug.security import check_password_hash, generate_password_hash
from validators.userValidators import *

user = APIRouter()

# LISTAR TODOS LOS USUARIO
@user.get('/users', response_model = list[User])
def getUsers():
    return conn.execute(users.select()).fetchall()


# CREAR UN NUEVO USUARIO
@user.post('/signup', response_model = User, status_code = status.HTTP_200_OK)
def signup(user:CreateUser):
    if not validationUser(user): raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Los campos no deben ser vacios.")

    if not validationEmail(user.email):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Correo no valido.")

    query = conn.execute(users.select().where(users.c.email == user.email)).fetchone()
    
    if query is not None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "El correo ya se encuentra registrado.")

    newUser = {"name": user.name, "email": user.email, "password": generate_password_hash(user.password)}
    result = conn.execute(users.insert().values(newUser))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).fetchone()


# VALIDAR USUARIO
@user.post('/login')
def login(user: Login):
    if not validationLogin(user):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "No se permiten campos vacios.")

    query = conn.execute(users.select().where(users.c.email == user.email)).fetchone()

    if not check_password_hash(query['password'], user.password):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = 'Usuario o contrasena incorrectos.')

    return query


# ACTUALIZAR USUARIO
@user.put('/users/{id}')
def updateUserById(id: str ,user : UserUpdateName):
    conn.execute(users.update().values(name = user.name).where(users.c.id == id))
    return "Updated"
