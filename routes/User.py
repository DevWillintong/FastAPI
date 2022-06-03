from fastapi import APIRouter #Definir las rutas por separado.
from config.db import conn
from models.userModel import users
from schemas.userSchema import User
from werkzeug.security import check_password_hash, generate_password_hash

user = APIRouter()

@user.get('/users')
def getUsers():
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def createUser(user:User):
    newUser = {"name": user.name, "email": user.email, "password": generate_password_hash(user.password)}
    result = conn.execute(users.insert().values(newUser))
    print(result.lastrowid)
    return 'Received'
