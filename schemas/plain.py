from marshmallow import fields, Schema

class PlainItemSchemas(Schema):
    id = fields.Str(dump_only=True)
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)


class PlainLojaSchemas(Schema):
    id = fields.Str(dump_only=True)
    nome = fields.Str(required=True)