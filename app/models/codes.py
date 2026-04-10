from sqlalchemy import String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, timedelta
from app.database.connection import Base
from enum import Enum as typerEnum
from sqlalchemy.dialects.postgresql import UUID
import uuid

class typeCode(str, typerEnum):
    resetPassword = "resetPassword",
    verifyEmail = "verifyEmail",

class Codes(Base):
    __tablename__ = "event_codes"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
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
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["Users"] = relationship(
        back_populates="codes"
    )
    
