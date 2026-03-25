from fastapi import HTTPException,Depends
from app.database.connection import get_db
from app.models.user import Users
from app.schemas.user import createUser, verifyEmail, userLogin, forgotPassword, ResetPassword
from sqlalchemy.orm import Session
from app.utils.jwt import create_token
from app.utils.security import hash_password, verify_password
from app.utils.codes import create_code_and_send_code, verify_code
from app.utils.security import pwd_context

def register_user_service(user: createUser, database: Session):
    exists_user = database.query(Users).filter(Users.email == user.email).first()
    if exists_user:
        raise HTTPException(status_code=409, detail="usuario esta registrado...")
    hashed_password = hash_password(user.hashed_password)
    new_user = Users(
        fullName = user.fullName,
        email = user.email,
        hashed_password = hashed_password,
        role = user.role,
        tell = user.tell,
        isActive = user.isActive,
        verified = user.verified
    )
    
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    confirm_id_user = database.query(Users).filter(Users.email == user.email).first()
    create_code_and_send_code(database, confirm_id_user.id, email=user.email, code_type="verifyEmail")
    return new_user


def verify_email_service(code: verifyEmail, database: Session):
    user = database.query(Users).filter(Users.email == code.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Correo incorrecto")
    
    if not verify_code(database, user.id, code.code, code_type="verifyEmail"):
        code = create_code_and_send_code(database, user.id, user.email, code_type="verifyEmail")
        return {
            "message": "Código de verificación incorrecto o expirado. Se ha enviado un nuevo código a tu correo electrónico.",
            "code": code,
        }
    
    user.verified = True
    database.commit()

    return {
        "verified": user.verified,
        "message": "Correo electrónico verificado correctamente"
    }

def login_user_service(user: userLogin, database: Session):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    if not verify_password(user.password, search_user.hashed_password):
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    if not search_user.verified:
        raise HTTPException(status_code=400, detail="Correo no verificado. Por favor verifica tu correo electrónico antes de iniciar sesión.")
    
    token = create_token({
        "sub": str(search_user.id)
    })

    return {
        "message": "Inicio de sesión exitoso",
        "access_token": token,
        "token_type": "bearer",
        "email": search_user.email,
        "role": search_user.role
    }

def forgot_password_service(user: forgotPassword, database: Session):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo no registrado")
    create_code_and_send_code(database, search_user.id, user.email, code_type="resetPassword")
    return {
        "message": "se ha enviado un código de recuperación de contraseña a tu correo electrónico."
    }

def reset_password_service(user: ResetPassword, database: Session):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo no registrado")
    
    if not verify_code(database, search_user.id, user.code, code_type="resetPassword"):
        raise HTTPException(status_code=400, detail="Código de recuperación de contraseña incorrecto o expirado.")
    
    hashed_password = hash_password(user.new_password)
    search_user.hashed_password = hashed_password
    database.commit()
    
    return {
        "message": "Contraseña restablecida correctamente"
    }