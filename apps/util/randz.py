from django.contrib.auth.models import User


def make_16_key():
    return User.objects.make_random_password(length=16)


def make_8_key():
    return User.objects.make_random_password(length=8)
