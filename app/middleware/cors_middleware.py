from fastapi.middleware.cors import CORSMiddleware
from app.config import config

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[config.URL_FRONTEND],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )