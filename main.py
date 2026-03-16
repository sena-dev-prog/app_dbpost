from fastapi import FastAPI, Depends

from app_dbpost.metodos import consultarApi

app = FastAPI()
app.include_router( consultarApi.router, prefix="/productos")

