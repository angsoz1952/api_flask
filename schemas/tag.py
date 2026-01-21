from schemas.plain import PlainTagSchemas, PlainLojaSchemas, PlainItemSchemas
from schemas.item import ItemSchema
from marshmallow import fields, Schema

class TagSchema(PlainTagSchemas):
    loja_id = fields.Int()
    loja = fields.Nested(PlainLojaSchemas(), dump_only=True)
    itens = fields.List(fields.Nested(PlainItemSchemas()),  dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)