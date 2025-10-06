from .general_service import GeneralService
from my_project.trip.dao import owner_dao


class OwnerService(GeneralService):
    _dao = owner_dao
