from db import db

class ImgModel(db.Model):
    __tablename__ = "img"

    id = db.Column(db.Integer, primary_key=True)
    id_hoa = db.Column(db.Integer, db.ForeignKey("flower.id"))
    img_url = db.Column(db.String(1028))
    flower = db.relationship("FlowerModel", back_populates="img")