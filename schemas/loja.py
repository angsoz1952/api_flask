from marshmallow import Schema, fields

from schemas.plain import PlainLojaSchemas, PlainItemSchemas


class LojaSchema(PlainLojaSchemas):
    itens = fields.List(fields.Nested(PlainItemSchemas()), dump_only=True)
    


class LojaSchemaUptade(Schema): 
    nome = fields.Str(required=False)
   