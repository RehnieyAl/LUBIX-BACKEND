from fastapi import FastAPI
from app.routers import user_routers
from app.routers import health
from app.database.connection import Base,engine
import app.models

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user_routers.router)
app.include_router(health.router)
