from my_project.trip.service import owner_service
from .general_controller import GeneralController


class OwnerController(GeneralController):
    _service = owner_service
