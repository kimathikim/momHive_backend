from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields


class Pharmacistschema(Schema):
    email = fields.Str()
    password = fields.Str()


class AdminSchema(Schema):
    email = fields.Str()
    password = fields.Str()


class DoctorSchema(Schema):
    email = fields.Str()
    password = fields.Str()


spec = APISpec(
    title="Hopital Prescription Management System API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

spec.components.schema("Pharmacists", schema=Pharmacistschema)
spec.components.schema("Doctors", schema=DoctorSchema)
spec.components.schema("Admin", schema=AdminSchema)
login_schemas = spec.to_dict()["components"]["schemas"]
