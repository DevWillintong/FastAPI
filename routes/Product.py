from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.productModel import products
from schemas.productSchema import *


product = APIRouter()


# LISTAR TODOS LOS PRODUCTOS.
@product.get('/product', response_model = list[Product], status_code = status.HTTP_200_OK)
def getProducts():
    query = conn.execute(products.select()).fetchall()
    print(len(query))
    if len(query) == 0:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "No se encontro contenido para mostrar")
    return query


# BUSCAR PRODUCTO POR ID
@product.get('/product/{id}', response_model = Product, status_code = status.HTTP_200_OK)
def getProductById(id:str):
    query = conn.execute(products.select().where(products.c.id == id)).fetchone()
    if query is None:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "Nothing")
    return query


# ELIMINAR PRODUCTO POR ID
@product.delete('/product/{id}', response_model = list[Product],status_code = 200)
def deleteProductById(id:str):
    product = getProductById(id)
    if product is None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "El producto ingresado no existe.")
    conn.execute(products.delete().where(products.c.id == id))
    query = getProducts()
    return query


# CREAR PRODUCTO 
@product.post('/product', response_model = Product, status_code = status.HTTP_200_OK)
def createProduct(product: CreateProduct):
    newProduct = {"name": product.name, "description": product.description}
    query = conn.execute(products.insert().values(newProduct))
    return getProductById(query.lastrowid)


# ACTUALIZAR PRODUCTO
@product.put('/product/{id}')
def updateProduct(id:str, product: CreateProduct):
    if id is None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "El ID proporcionado es invalido.")\

    validation = getProductById(id)

    if validation is None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "El producto no existe.")
        
    conn.execute(products.update().values(name = product.name, description = product.description).where(products.c.id == id))
    return getProductById(id)
