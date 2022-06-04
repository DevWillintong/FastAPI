from fastapi import FastAPI
from routes.User import user

app = FastAPI(
    title = "First API",
    description = "This is my firts API with FastAPI",
    version = "0.0.1", 
    openapi_tags = [{"name": "Users", "description": "Users Routes"},
                    {"name": "App", "description": "App Routes"}]
)
app.include_router(user, tags = ["Users"]) #Incluimos las rutas de user.

@app.get('/', tags = ["App"])
def home():
    return 'Home'