from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.prescription import Prescription, Med
from marshmallow import Schema, fields
from app.models.medication import Medication


class Prescription(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Prescription
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


class Medschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Med
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


class Medicationschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Medication
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


class OTPSchema(Schema):
    email = fields.Str()
    password = fields.Str()


spec = APISpec(
    title="Hopital Prescription Management System API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

spec.components.schema("Prescription", schema=Prescription)
spec.components.schema("Med", schema=Medschema)
spec.components.schema("OTP", schema=OTPSchema)
spec.components.schema("Medication", schema=Medicationschema)


pres = spec.to_dict()["components"]["schemas"]
