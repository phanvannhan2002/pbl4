
from flask import Flask, request
from flask_smorest import Api
import os

from db import db
from controller.flower import blp as FlowerBluePrint
from controller.home import blp as HomeBluePrint
from controller.nhandien import blp as NhandienBluePrint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/pbl4"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)
    api.register_blueprint(FlowerBluePrint)
    api.register_blueprint(HomeBluePrint)
    api.register_blueprint(NhandienBluePrint)

    with app.app_context():
        db.create_all()
    return app