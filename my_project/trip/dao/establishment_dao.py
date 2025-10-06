from .general_dao import GeneralDAO
from sqlalchemy import func

from my_project import db
from my_project.trip.domain import Establishment, Review


class EstablishmentDAO(GeneralDAO):
    _domain_type = Establishment

    def find_by_name(self, name: str):
        return self._session.query(self._domain_type).filter(self._domain_type.name.ilike(f"%{name}%")).all()

    def find_by_owner(self, owner_id: int):
        return self._session.query(self._domain_type).filter_by(owner_id=owner_id).all()

    def recalc_rating(self, establishment_id: int) -> None:
        avg, count = db.session.query(func.avg(Review.rating), func.count(Review.id)) \
            .filter(Review.establishment_id == establishment_id).one()
        est = db.session.query(Establishment).get(establishment_id)
        if est:
            est.average_rating = float(avg) if avg is not None else 0.0
            est.reviews_count = int(count or 0)
            db.session.commit()
