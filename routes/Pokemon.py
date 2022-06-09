from fastapi import APIRouter, HTTPException, status
from pydantic import Json
from requests.auth import HTTPBasicAuth
from getpass import getpass
from schemas.userSchema import CreateUser
import requests

pokemon = APIRouter()

@pokemon.post('/generacion')
def generacion(user: CreateUser):
    data = {"name": user.name, "email": user.email, "password": user.password}
    result = requests.post('http://127.0.0.1:8000/auth/signup', json = data)
    return result.content

    


# data = {"name": "willintong@hotmail.com", "password": "string"}
# params = {"id": "1"}
# result = requests.post("url", data = data) # Enviamos un cuerpo a la peticion
# result = requests.post("url", params = params) # Enviamos parametros a la peticion.
# print(result.text)

# requests.get('https://api.github.com/user',auth=HTTPBasicAuth('username', getpass()))