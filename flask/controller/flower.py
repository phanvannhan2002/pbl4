from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import FlowerSchema
from db import db

from flask import render_template, request

from models import FlowerModel

blp = Blueprint("Flowers", "flowers", description="Operations on items")

@blp.route('/')
class Flower(MethodView):
    # @blp.response(200, FlowerSchema)
    def get(self):
        name = request.args.get('flower')
        if not name:
            return render_template("home.html")
        else:
            temp = name.split(" ")
            if temp[0] != "hoa" and name != "Hướng dương" and name != "Bồ công anh":
                temp.insert(0, "hoa")
                name = " ".join(temp)
            hoa = db.session.execute(db.select(FlowerModel).where(FlowerModel.tenthongthuong == name)).scalar()
            return render_template('hoa.html', data=hoa)