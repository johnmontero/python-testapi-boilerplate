from marshmallow import Schema, fields

class UnauthorizedSchema(Schema):
    message = fields.Str(required=True)
    documentation_url = fields.Str(required=True)