from app.models import storage
from app.models.user import Users


user = Users(
    email="jjji",
    password="1234",
    first_name="Javier",
    second_name="Jara",
    phone_number="1ii234567i8",
)
user.save()
print(user.to_dict())
