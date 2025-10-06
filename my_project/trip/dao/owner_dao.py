from .general_dao import GeneralDAO

from my_project.trip.domain import Owner


class OwnerDAO(GeneralDAO):
    _domain_type = Owner
