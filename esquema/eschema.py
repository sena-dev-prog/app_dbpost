from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id_prod : Optional[int]
    nom_prod : str
    proveedor : str 
    
    class config:
        orm_mode = True
