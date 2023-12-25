from db import db

class FlowerModel(db.Model):
    __tablename__ = "flower"

    id = db.Column(db.Integer, primary_key=True)
    tenthongthuong = db.Column(db.String(1028), unique=True, nullable=False)
    tenkhoahoc = db.Column(db.String(1028), unique=True)
    mausac = db.Column(db.String(1028))
    mota = db.Column(db.String(1028))
    phanbo = db.Column(db.String(1028))
    sudung = db.Column(db.String(1028))
    nguongoc = db.relationship("NguongocModel", back_populates="flower", uselist=False)
    cachchamsoc = db.relationship("CachchamsocModel", back_populates="flower", uselist=False)
    img = db.relationship("ImgModel", back_populates="flower", lazy="dynamic")