from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.doctor import Doctors


class DoctorSchema(SQLAlchemyAutoSchema):
    class meta:
        model = Doctors
