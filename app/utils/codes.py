from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.codes import Codes, typeCode
from app.utils.email import send_code_email
import random
import uuid

def generate_code(length=6) -> str:
    return ''.join(random.choices('0123456789', k=length))

def create_code_and_send_code(database: Session, user_id: uuid.UUID, email: str, code_type: typeCode):
    code = generate_code(6)
    new_code = Codes(
        code=code,
        type=code_type,
        user_id=user_id,
        created_at=datetime.utcnow(),
        expires_at=datetime.utcnow() + timedelta(minutes=15)
    )

    database.add(new_code)
    database.commit()
    database.refresh(new_code)
    send_code_email(email, code)
    return {
        "message":"Código enviado correctamente",
        "code": code
    }

def verify_code(database: Session, user_id: uuid.UUID, code: str, code_type: typeCode) -> bool:
    code_entry = database.query(Codes).filter(
        Codes.user_id == user_id,
        Codes.code == code,
        Codes.type == code_type,
        Codes.expires_at > datetime.utcnow()
    ).first()

    if code_entry:
        database.delete(code_entry)
        database.commit()
        return True
    return False