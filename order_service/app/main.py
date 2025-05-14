from fastapi import FastAPI
from app.interfaces.routes import order_routes
from app.config import Base, engine

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(order_routes.router)

# Alembic se encargará ahora de crear las tablas mediante migraciones