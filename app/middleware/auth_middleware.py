from fastapi import Request
from starlette.responses import JSONResponse
from app.database.connection import SessionLocal
from app.models.event_token import EventToken
from app.models.user import Users


PUBLIC_ROUTES = [
    "/user/login",
    "/user/register",
    "/user/verify-email",
    "/health/database",
]

async def auth_middleware(request: Request, call_next):
    if request.url.path in PUBLIC_ROUTES:
        return await call_next(request)

    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse(status_code=401, content={"detalle": "Token de autenticación requerido"})

    db = SessionLocal()
    event_token = db.query(EventToken).filter(EventToken.token == token).first()
    if not event_token:
        return JSONResponse(status_code=401, content={"detalle": "token invalido"})

    user = db.query(Users).filter(Users.id == event_token.user_id).first()
    if not user:
        return JSONResponse(status_code=401, content={"detalle": "Usuario no encontrado"})

    request.state.user = user
    response = await call_next(request)
    return response
