from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import render_template

from schemas import FlowerSchema
from db import db

from models import FlowerModel

blp = Blueprint("Home", "home", description="Operations on items")

@blp.route("/")
class Home(MethodView):
    def get(self):
        return render_template("home.html")