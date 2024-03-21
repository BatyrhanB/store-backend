import factory

from django.contrib.auth.hashers import make_password

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: "user%d@example.com" % n)
    password = make_password("password123")
    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    middlename = factory.Faker("first_name")
    is_superuser = False
    is_admin = False
    is_staff = False
    is_verified = False
    is_active = True
