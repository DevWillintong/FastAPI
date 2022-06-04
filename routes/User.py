from distutils.log import error
from fastapi import APIRouter, Response, status #Definir las rutas por separado.
from config.db import conn
from models.userModel import users
from schemas.userSchema import User, UserUpdateName
from werkzeug.security import check_password_hash, generate_password_hash

user = APIRouter()

@user.get('/users', response_model = list[User])
def getUsers():
    return conn.execute(users.select()).fetchall()


@user.post('/users', response_model = User)
def createUser(user:User):
    newUser = {"name": user.name, "email": user.email, "password": generate_password_hash(user.password)}
    result = conn.execute(users.insert().values(newUser))
    print(result.lastrowid)
    return conn.execute(users.select()).fetchone()


@user.get('/users/{id}', response_model = User)
def getUserById(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete('/users/{id}', status_code = status.HTTP_200_OK)
def deleteUserById(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code = status.HTTP_200_OK) 


@user.put('/users/{id}')
def updateUserById(id: str ,user : User):
    # conn.execute(users.select().where(users.c.id == id)).first()
    conn.execute(users.update().values(name = user.name, email = user.email, password = generate_password_hash(user.password)).where(users.c.id == id))
    return "Updated"

@user.put('/users/test/{id}')
def updateUserById(id: str ,user : UserUpdateName):
    conn.execute(users.update().values(name = user.name).where(users.c.id == id))
    return "Updated"
