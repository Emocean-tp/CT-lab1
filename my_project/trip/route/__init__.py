from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for TripAdvisor-like module
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .owner_route import owner_bp
    from .establishment_route import establishment_bp
    from .review_route import review_bp

    app.register_blueprint(owner_bp)
    app.register_blueprint(establishment_bp)
    app.register_blueprint(review_bp)
