from .general_service import GeneralService
from my_project.trip.dao import establishment_dao


class EstablishmentService(GeneralService):
    _dao = establishment_dao

    def find_by_owner(self, owner_id: int):
        return self._dao.find_by_owner(owner_id)

    def search(self, name: str | None, city: str | None, category: str | None):
        query = establishment_dao._session.query(self._dao._domain_type)
        if name:
            query = query.filter(self._dao._domain_type.name.ilike(f"%{name}%"))
        if city:
            query = query.filter(self._dao._domain_type.city.ilike(f"%{city}%"))
        if category:
            query = query.filter(self._dao._domain_type.category.ilike(f"%{category}%"))
        return query.all()

    def get_rating(self, establishment_id: int):
        est = self._dao.find_by_id(establishment_id)
        return {
            "establishment_id": establishment_id,
            "average_rating": float(est.average_rating or 0.0) if est else 0.0,
            "reviews_count": int(est.reviews_count or 0) if est else 0,
        }
