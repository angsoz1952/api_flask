from marshmallow import Schema, fields


class ItemSchema(Schema):
	id = fields.Str(required=False)
	nome = fields.Str(required=True)
	preco = fields.Float(required=True)
	loja_id = fields.Str(required=True)


class ItemSchemaUpdate(Schema):
	nome = fields.Str(required=False)
	preco = fields.Float(required=False)
	loja_id = fields.Str(required=False)
