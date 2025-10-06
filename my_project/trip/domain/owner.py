from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import func

from my_project import db
from .i_dto import IDto


class Owner(db.Model, IDto):
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())

    establishments = db.relationship("Establishment", back_populates="owner", lazy="dynamic")

    def __repr__(self) -> str:
        return f"Owner({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "contact_email": self.contact_email or "",
            "phone": self.phone or "",
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owner:
        return Owner(**dto_dict)
