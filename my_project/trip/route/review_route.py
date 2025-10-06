from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.trip.controller import review_controller
from my_project.trip.domain import Review

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@review_bp.get('')
def get_all_reviews() -> Response:
    establishment_id = request.args.get('establishment_id', type=int)
    if establishment_id:
        return make_response(jsonify(review_controller.find_by_establishment(establishment_id)), HTTPStatus.OK)
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_review() -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    created = review_controller.create(review)
    return make_response(jsonify(created), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
