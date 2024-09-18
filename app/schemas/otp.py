from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.otp import OTP


class tpschema(SQLAlchemyAutoSchema):
    class meta:
        model = OTP
