from .general_service import GeneralService
from my_project.trip.dao import review_dao


class ReviewService(GeneralService):
    _dao = review_dao

    def find_by_establishment(self, establishment_id: int):
        return self._dao.find_by_establishment(establishment_id)
