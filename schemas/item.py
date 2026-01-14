from marshmallow import Schema, fields
from schemas.plain import PlainItemSchemas

class ItemSchema(PlainItemSchemas):
	loja_id = fields.Str(required=True)


class ItemSchemaUpdate(Schema):
	nome = fields.Str(required=False)
	preco = fields.Float(required=False)
	loja_id = fields.Str(required=False)
