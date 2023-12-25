from db import db

class NguongocModel(db.Model):
    __tablename__ = "nguongoc"

    id = db.Column(db.Integer, primary_key=True)
    id_hoa = db.Column(db.Integer, db.ForeignKey("flower.id"))
    diadiemphathien = db.Column(db.String(1028))
    phanloai = db.Column(db.String(1028))
    lichsupt = db.Column(db.String(1028))
    phanbohiennay = db.Column(db.String(1028))
    flower = db.relationship("FlowerModel", back_populates="nguongoc")