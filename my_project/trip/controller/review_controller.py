from typing import List, Dict, Any

from my_project.trip.service import review_service
from .general_controller import GeneralController


class ReviewController(GeneralController):
    _service = review_service

    def find_by_establishment(self, establishment_id: int) -> List[Dict[str, Any]]:
        return [x.put_into_dto() for x in self._service.find_by_establishment(establishment_id)]
