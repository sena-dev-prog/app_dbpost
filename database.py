from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Construir la URL de conexión
# DB_URL = f"mysql+pymysql://prueba:prueba@localhost:3306/prueba"
DB_URL = f"mysql+pymysql://root:zFtBcyIKPGjwqcxYAuRvSSVCtYaZQNal@nozomi.proxy.rlwy.net:38890/railway"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
