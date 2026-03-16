from sqlalchemy import Column, Integer, String
from database import Base, get_db
from fastapi import APIRouter, Query, Depends, HTTPException, status 
from typing import List
from sqlalchemy.orm import Session
from modelos import modelo_producto
from app_dbpost.esquema import eschema

router = APIRouter()
@router.get("/")
async def consultar():
    return "Consultar productos listados...."

@router.get("/prod_all")
async def leer_datos( db : Session = Depends(get_db)):
    producto=  db.query(modelo_producto.Producto).all()
    return producto

@router.get("/prov_all")
async def leer_datos( db : Session = Depends(get_db)):
    proveedor=  db.query(modelo_producto.Proveedor).all()
    return proveedor

@router.get("/prod/{id_prod}")
async def buscar_prod(id_prod : int ,  db : Session = Depends(get_db)):
    producto=  db.query(modelo_producto.Producto).get(id_prod)
    if (producto):
        return producto
    else:
        raise HTTPException(status_code=404, detail=f"Producto con id {id_prod} no encontrado")

@router.post( "/add", response_model = eschema.Producto, status_code=status.HTTP_201_CREATED)
async def crearProducto( producto : eschema.Producto, session  : Session = Depends(get_db)):
    productoAdd = modelo_producto.Producto (
       id_prod =  producto.id_prod,
       nom_prod = producto.nom_prod,
       proveedor = producto.proveedor
    )
    session.add(productoAdd)
    session.commit()
    session.refresh(productoAdd)
    return productoAdd

## metodo put para actualizar

@router.put("/update/{id_prod}" , response_model = eschema.Producto)
async def update_Prod(id_prod : int , producs : eschema.Producto, db : Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_prod == id_prod
        ).first()
    if not producto:
        raise HTTPException(status_code = 404 , detail="Producto no encontrado....")
    
    producto.id_prod = producs.id_prod
    producto.nom_prod = producs.nom_prod
    producto.proveedor = producs.proveedor
    db.commit()
    db.refresh(producto)
    return producto

## metodo de borrado
@router.delete("/borrar/{id_prod}")
async def borrarProd( id_prod : int, db : Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_prod == id_prod
        ).first()
    if not producto:
         raise HTTPException(status_code = 404 , detail="Producto no encontrado....")
     
    db.delete(producto)
    db.commit()
    return f"El campo {id_prod} ha sido borrado"
