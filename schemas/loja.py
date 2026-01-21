from marshmallow import Schema, fields

from schemas.plain import PlainLojaSchemas, PlainItemSchemas, PlainTagSchemas


class LojaSchema(PlainLojaSchemas):
    itens = fields.List(fields.Nested(PlainItemSchemas()), dump_only=True)

    tags = fields.List(fields.Nested(PlainTagSchemas()), dump_only=True)
    


class LojaSchemaUptade(Schema): 
    nome = fields.Str(required=False)
   