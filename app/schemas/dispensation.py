from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.dispensation import Dispensation as dispensation
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec


class dispensationschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = dispensation
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


spec = APISpec(
    title="Hopital Prescription Management System API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

spec.components.schema("Dispensation", schema=dispensationschema)
dis = spec.to_dict()["components"]["schemas"]
