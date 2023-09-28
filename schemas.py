from marshmallow import Schema, fields


class ModeloBuscaSchema(Schema):
    id = fields.Int(dump_only=True)  # dump_only means it won't be loaded when deserializing
    ip_address = fields.Str(required=True)
    pokemon_name = fields.Str(required=True)

