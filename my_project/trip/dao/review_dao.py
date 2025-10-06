from .general_dao import GeneralDAO
from sqlalchemy import func

from my_project import db
from my_project.trip.domain import Review, Establishment


class ReviewDAO(GeneralDAO):
    _domain_type = Review

    def find_by_establishment(self, establishment_id: int):
        return self._session.query(self._domain_type).filter_by(establishment_id=establishment_id).all()

    def _recalc_for_establishment(self, establishment_id: int) -> None:
        avg, count = db.session.query(func.avg(Review.rating), func.count(Review.id)) \
            .filter(Review.establishment_id == establishment_id).one()
        est = db.session.query(Establishment).get(establishment_id)
        if est:
            est.average_rating = float(avg) if avg is not None else 0.0
            est.reviews_count = int(count or 0)
            db.session.commit()

    def create(self, obj: object) -> object:
        review = super().create(obj)
        self._recalc_for_establishment(review.establishment_id)
        return review

    def delete(self, key: int) -> None:
        review = self.find_by_id(key)
        est_id = review.establishment_id if review else None
        super().delete(key)
        if est_id:
            self._recalc_for_establishment(est_id)

    def update(self, key: int, in_obj: object) -> None:
        super().update(key, in_obj)
        review = self.find_by_id(key)
        if review:
            self._recalc_for_establishment(review.establishment_id)

    def patch(self, key: int, field_name: str, value: object) -> None:
        super().patch(key, field_name, value)
        review = self.find_by_id(key)
        if review:
            self._recalc_for_establishment(review.establishment_id)
