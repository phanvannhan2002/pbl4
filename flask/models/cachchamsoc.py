from db import db

class CachchamsocModel(db.Model):
    __tablename__ = "cachchamsoc"

    id = db.Column(db.Integer, primary_key=True)
    id_hoa = db.Column(db.Integer, db.ForeignKey("flower.id"))
    anhsang = db.Column(db.String(1028))
    dat = db.Column(db.String(1028))
    nuoc = db.Column(db.String(1028))
    phan = db.Column(db.String(1028))
    saubenh = db.Column(db.String(1028))
    cattia = db.Column(db.String(1028))
    flower = db.relationship("FlowerModel", back_populates="cachchamsoc")