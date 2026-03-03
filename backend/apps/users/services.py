from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser


User = get_user_model()

def create_user(*, email:str, username: str, password: str) -> AbstractBaseUser:
    user = User.objects.create_user(
        email= email,
        username= username,
        password= password,
    )
    return user