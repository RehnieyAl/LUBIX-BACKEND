from fastapi import FastAPI
from app.routers import user_routers
from app.routers import health
from app.database.connection import Base,engine
import app.models
from app.middleware.auth_middleware import auth_middleware
from app.middleware.cors_middleware import setup_cors

app = FastAPI()
app.middleware("http")(auth_middleware)
setup_cors(app)
Base.metadata.create_all(bind=engine)
app.include_router(user_routers.router)
app.include_router(health.router)


