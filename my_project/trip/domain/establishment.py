from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import func

from my_project import db
from .i_dto import IDto


class Establishment(db.Model, IDto):
    __tablename__ = "establishment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., hotel, restaurant, attraction
    address = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())

    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=True)
    owner = db.relationship("Owner", back_populates="establishments")

    average_rating = db.Column(db.Float, nullable=False, default=0.0)
    reviews_count = db.Column(db.Integer, nullable=False, default=0)

    reviews = db.relationship("Review", back_populates="establishment", lazy="dynamic", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Establishment({self.id}, '{self.name}', '{self.category}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "address": self.address or "",
            "city": self.city or "",
            "country": self.country or "",
            "owner_id": self.owner_id or "",
            "owner": self.owner.name if self.owner is not None else "",
            "average_rating": float(self.average_rating or 0.0),
            "reviews_count": int(self.reviews_count or 0),
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Establishment:
        return Establishment(**dto_dict)
