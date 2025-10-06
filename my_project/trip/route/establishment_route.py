from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.trip.controller import establishment_controller, review_controller
from my_project.trip.domain import Establishment, Review

establishment_bp = Blueprint('establishments', __name__, url_prefix='/establishments')


@establishment_bp.get('')
def get_all_establishments() -> Response:
    return make_response(jsonify(establishment_controller.find_all()), HTTPStatus.OK)


@establishment_bp.post('')
def create_establishment() -> Response:
    content = request.get_json()
    establishment = Establishment.create_from_dto(content)
    created = establishment_controller.create(establishment)
    return make_response(jsonify(created), HTTPStatus.CREATED)


@establishment_bp.get('/<int:establishment_id>')
def get_establishment(establishment_id: int) -> Response:
    return make_response(jsonify(establishment_controller.find_by_id(establishment_id)), HTTPStatus.OK)


@establishment_bp.put('/<int:establishment_id>')
def update_establishment(establishment_id: int) -> Response:
    content = request.get_json()
    establishment = Establishment.create_from_dto(content)
    establishment_controller.update(establishment_id, establishment)
    return make_response("Establishment updated", HTTPStatus.OK)


@establishment_bp.patch('/<int:establishment_id>')
def patch_establishment(establishment_id: int) -> Response:
    content = request.get_json()
    establishment_controller.patch(establishment_id, content)
    return make_response("Establishment updated", HTTPStatus.OK)


@establishment_bp.delete('/<int:establishment_id>')
def delete_establishment(establishment_id: int) -> Response:
    establishment_controller.delete(establishment_id)
    return make_response("Establishment deleted", HTTPStatus.OK)


@establishment_bp.get('/search')
def search_establishments() -> Response:
    name = request.args.get("name")
    city = request.args.get("city")
    category = request.args.get("category")
    results = establishment_controller.search(name=name, city=city, category=category)
    return make_response(jsonify(results), HTTPStatus.OK)


@establishment_bp.get('/by-owner/<int:owner_id>')
def establishments_by_owner(owner_id: int) -> Response:
    results = establishment_controller.find_by_owner(owner_id)
    return make_response(jsonify(results), HTTPStatus.OK)


@establishment_bp.get('/<int:establishment_id>/rating')
def get_establishment_rating(establishment_id: int) -> Response:
    rating = establishment_controller.get_rating(establishment_id)
    return make_response(jsonify(rating), HTTPStatus.OK)


@establishment_bp.get('/<int:establishment_id>/reviews')
def list_reviews(establishment_id: int) -> Response:
    reviews = review_controller.find_by_establishment(establishment_id)
    return make_response(jsonify(reviews), HTTPStatus.OK)


@establishment_bp.post('/<int:establishment_id>/reviews')
def add_review(establishment_id: int) -> Response:
    content = request.get_json()
    review = Review.create_from_dto({**content, "establishment_id": establishment_id})
    created = review_controller.create(review)
    return make_response(jsonify(created), HTTPStatus.CREATED)
