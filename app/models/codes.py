from sqlalchemy import String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, timedelta
from app.database.connection import Base
from enum import Enum as typerEnum

class typeCode(str, typerEnum):
    resetPassword = "resetPassword",
    verifyEmail = "verifyEmail",

class Codes(Base):
    __tablename__ = "event_codes"
    id: Mapped[int] = mapped_column(
        primary_key=True, 
        autoincrement=True
    )

    code: Mapped[str] = mapped_column(
        String(6), 
        nullable=False
    )

    type: Mapped[typeCode] = mapped_column(
        Enum(typeCode, name="type_code_enum")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow    
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.utcnow() + timedelta(minutes=15)
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["Users"] = relationship(
        back_populates="codes"
    )
    
