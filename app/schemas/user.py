from pydantic import BaseModel, EmailStr
from app.models.user import RoleType

    
class createUser(BaseModel):
    fullName: str
    email: EmailStr
    hashed_password: str
    role: RoleType = RoleType.user
    tell: str
    isActive: bool = True
    verified: bool = False

class verifyEmail(BaseModel):
    email: EmailStr
    code: str

class userLogin(BaseModel):
    email: EmailStr
    password: str

class forgotPassword(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    email: EmailStr
    code: str
    new_password: str