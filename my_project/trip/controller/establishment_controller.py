from typing import Optional, Dict, Any, List

from my_project.trip.service import establishment_service
from .general_controller import GeneralController


class EstablishmentController(GeneralController):
    _service = establishment_service

    def find_by_owner(self, owner_id: int) -> List[Dict[str, Any]]:
        return [x.put_into_dto() for x in self._service.find_by_owner(owner_id)]

    def search(self, name: Optional[str], city: Optional[str], category: Optional[str]) -> List[Dict[str, Any]]:
        return [x.put_into_dto() for x in self._service.search(name, city, category)]

    def get_rating(self, establishment_id: int) -> Dict[str, Any]:
        return self._service.get_rating(establishment_id)
