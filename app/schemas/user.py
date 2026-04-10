from pydantic import BaseModel, EmailStr, field_validator
from app.models.user import RoleType
from app.models.event_token import TokenType
import re
import uuid

class createUser(BaseModel):
    fullName: str
    email: EmailStr
    password: str
    role: RoleType = RoleType.user
    tell: str
    isActive: bool = True
    verified: bool = False

    @field_validator('fullName')
    def validate_fullName(cls, v: str):
        if len(v) < 3:
            raise ValueError('el nombre completo debe tener al menos 3 caracteres')
        if len(v) > 60:
            raise ValueError('el nombre completo no debe exceder los 50 caracteres')
        return v

    @field_validator('password')
    def validate_password(cls, v: str):
        if len(v) < 8:
            raise ValueError('la contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('la contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', v):
            raise ValueError('la contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('la contraseña debe contener al menos un número')
        return v
    
    @field_validator('tell')
    def validate_tell(cls, v: str):
        if len(v) < 10:
            raise ValueError('el número de teléfono debe tener al menos 10 caracteres')
        return v

class verifyEmail(BaseModel):
    email: EmailStr
    code: str

    @field_validator('code')
    def validate_code(cls, v: str):
        if len(v) != 6:
            raise ValueError('el código debe tener exactamente 6 caracteres')
        if not v.isdigit():
            raise ValueError('el código debe contener solo números')
        return v

class userLogin(BaseModel):
    email: EmailStr
    password: str
    

class forgotPassword(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    email: EmailStr
    code: str
    new_password: str

    @field_validator('code')
    def validate_code(cls, v: str):
        if len(v) != 6:
            raise ValueError('el código debe tener exactamente 6 caracteres')
        if not v.isdigit():
            raise ValueError('el código debe contener solo números')
        return v

    @field_validator('new_password')
    def validate_new_password(cls, v: str):
        if len(v) < 8:
            raise ValueError('la contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('la contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', v):
            raise ValueError('la contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('la contraseña debe contener al menos un número')
        return v
    
class AddToken(BaseModel):
    id: int
    token: TokenType.access

class DeleteToken(BaseModel):
    id: int
    token: TokenType.access