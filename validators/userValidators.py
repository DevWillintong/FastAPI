from distutils.log import Log
from schemas.userSchema import *

def validationEmail(mail: str)-> bool:
    if "@" in mail:
        return True
    return False

def validationUser(user: CreateUser)-> bool:
    if user.name is "" or user.email is "" or user.password is "": 
        return False
    return True
        
def empty(string:str):
    if string != "":
        return True
    return False