from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from app.models.pharmacist import Pharmacists
from app.models.patient import Patients
from app.models.doctor import Doctors
from app.models.admin import Admin
from app.models.user import OnBoarders
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class OnBoarderschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = OnBoarders
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


class Pharmacistschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Pharmacists
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


class Patientschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Patients
        include_fk = True
        exclude = ["id", "created_at", "updated_at", "patient_code"]


class Adminschema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Admin
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


class DoctorSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Doctors
        include_fk = True
        exclude = ["id", "created_at", "updated_at"]


# Create an APISpec
spec = APISpec(
    title="Hopital Prescription Management System API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

# Register the Marshmallow Schemas in the APISpec
spec.components.schema("OnBoarders", schema=OnBoarderschema)
spec.components.schema("Patients", schema=Patientschema)
spec.components.schema("Admins", schema=Adminschema)
spec.components.schema("Pharmacists", schema=Pharmacistschema)
spec.components.schema("Doctors", schema=DoctorSchema)

# Generate the Swagger schemas from the APISpec
swagger_schemas = spec.to_dict()["components"]["schemas"]
