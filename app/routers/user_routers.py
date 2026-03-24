from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import createUser, userLogin, forgotPassword, ResetPassword
from app.models.user import Users
from app.database.connection import get_db
from app.utils.jwt import create_token
from app.utils.security import hash_password, verify_password
from app.utils.codes import create_code_and_send_code, verify_code
from app.utils.security import pwd_context

router = APIRouter(
    prefix=("/user"),
    tags=["User"]
)

@router.post("/register")
def registerUser(user: createUser,database: Session = Depends(get_db)):
    exists_user = database.query(Users).filter(Users.email == user.email).first()
    if exists_user:
        raise HTTPException(status_code=409, detail="usuario esta registrado...")
    hashed_password = hash_password(user.hashed_password)
    registerUser = Users(
        fullName = user.fullName,
        email = user.email,
        hashed_password = hashed_password,
        role = user.role,
        tell = user.tell,
        isActive = user.isActive
    )
    database.add(registerUser)
    database.commit()
    database.refresh(registerUser)
    return registerUser

@router.post("/singIn")
def singIn(user: userLogin, database: Session = Depends(get_db)):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo incorrecto")
    if not verify_password(user.password, search_user.hashed_password):
        raise HTTPException(status_code=401, detail="contraseña incorrecta")
    
    token = create_token({
        "sub": str(search_user.id)
    })

    return {
        "message": "Inicio de sesion correctamente",
        "acceso_token": token,
        "token_type": "bearer"
        }

@router.post("/forgot-password")
def forgot_password(data: forgotPassword, database: Session = Depends(get_db)):
    user = database.query(Users).filter(Users.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Correo incorrecto")
    
    result = create_code_and_send_code(database, user.id, user.email ,code_type="resetPassword")
    return {
        "message": "Se ha enviado un código de verificación a tu correo electrónico para restablecer tu contraseña.",
        "result": result
    }

@router.post("/reset-password")
def reset_password(data: ResetPassword, database: Session = Depends(get_db)):
    user = database.query(Users).filter(Users.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Correo incorrecto")
    
    if not verify_code(database, user.id, data.code, code_type="resetPassword"):
        raise HTTPException(status_code=400, detail="Código de verificación incorrecto o expirado")
    
    user.hashed_password = pwd_context.hash(data.new_password)
    database.commit()
    return {
        "message": "Contraseña restablecida correctamente"
    }