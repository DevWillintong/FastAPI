from fastapi import FastAPI
from routes.User import user
from routes.Product import  product
from routes.Pokemon import pokemon
from routes.Auth import auth

app = FastAPI(
    title = "First API",
    description = "This is my firts API with FastAPI",
    version = "0.0.1", 
    openapi_tags = [{"name": "Users", "description": "Users Routes"},
                    {"name": "App", "description": "App Routes"}]
)
app.include_router(user, tags = ["Users"]) 
app.include_router(auth, tags = ["Auth"]) 
app.include_router(product, tags = ["Product"]) 
app.include_router(pokemon, tags = ["Pokemon"]) 

@app.get('/', tags = ["App"])
def home():
    return 'Home'
