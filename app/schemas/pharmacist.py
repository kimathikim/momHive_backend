from marshmallow import Schema, fields


class patientschema(Schema):
    email = fields.Str()
    password = fields.Str()
