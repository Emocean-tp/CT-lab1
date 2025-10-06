from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import func, CheckConstraint

from my_project import db
from .i_dto import IDto


class Review(db.Model, IDto):
    __tablename__ = "review"
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='ck_review_rating_range'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishment.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=True)
    body = db.Column(db.Text, nullable=True)
    reviewer_name = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())

    establishment = db.relationship("Establishment", back_populates="reviews")

    def __repr__(self) -> str:
        return f"Review({self.id}, est={self.establishment_id}, rating={self.rating})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "establishment_id": self.establishment_id,
            "rating": int(self.rating),
            "title": self.title or "",
            "body": self.body or "",
            "reviewer_name": self.reviewer_name or "",
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        return Review(**dto_dict)
