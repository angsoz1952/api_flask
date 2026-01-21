from marshmallow import Schema, fields
from schemas.plain import PlainItemSchemas, PlainTagSchemas

class ItemSchema(PlainItemSchemas):
	loja_id = fields.Int(required=True)
	tags = fields.List(fields.Nested(PlainTagSchemas()), dump_only=True)


class ItemSchemaUpdate(Schema):
	nome = fields.Str(required=False)
	preco = fields.Float(required=False)
	loja_id = fields.Int(required=False)
