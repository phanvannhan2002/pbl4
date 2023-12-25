from marshmallow import Schema, fields

class PlainFlowerSchema(Schema):
    id = fields.Int(dump_only=True)
    tenthongthuong = fields.Str()
    tenkhoahoc = fields.Str()
    mausac = fields.Str()
    mota = fields.Str()
    phanbo = fields.Str()
    sudung = fields.Str()

class PlainCachchamsoSchema(Schema):
    id = fields.Int(dump_only=True)
    anhsang = fields.Str()
    dat = fields.Str()
    nuoc = fields.Str()
    phan = fields.Str()
    saubenh = fields.Str()
    cattia = fields.Str()

class PlainNguongocSchema(Schema):
    id = fields.Int(dump_only=True)
    diadiemphathien = fields.Str()
    phanloai = fields.Str()
    lichsupt = fields.Str()
    phanbohiennay = fields.Str()

class PlainImgSchema(Schema):
    id = fields.Int(dump_only=True)
    img_url = fields.Str()

class FlowerSchema(PlainFlowerSchema):
    nguongoc = fields.Nested(PlainNguongocSchema, dump_only=True)
    cachchamsoc = fields.Nested(PlainCachchamsoSchema, dump_only=True)
    img = fields.List(fields.Nested(PlainImgSchema, dump_only=True))

