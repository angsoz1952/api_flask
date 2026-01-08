from marshmallow import Schema, fields


class LojaSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    cidade = fields.Str(required=True)
    telefone = fields.Str(required=True)


class LojaSchemaUptade(Schema): 
    nome = fields.Str(required=False)
    cidade = fields.Str(required=False)
    telefone = fields.Str(required=False)