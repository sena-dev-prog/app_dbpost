from database import Base
from sqlalchemy import Column, Integer, String

class Producto(Base):
    __tablename__ = "producto"
    id_prod = Column(Integer , primary_key = True, index = True)
    nom_prod = Column(String(100))
    proveedor = Column(String(150))

class Proveedor(Base):
    __tablename__ = "Proveedor"
    id_prov = Column(Integer , primary_key = True, index = True)
    nom_prov = Column(String(100))
    mail = Column(String(100))