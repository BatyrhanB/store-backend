from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class JWTTokenService(object):
    __token = RefreshToken()

    """
    Service for generating JWT tokens.
    """
    @classmethod
    def generate_token(cls, email: str) -> dict:
        """
        Generates a JWT token for the given email.

        :param phone: The phone number for which the token should be generated.
        :return: String containing the generated token.
        """
        user = User.objects.get(email=email)
        return cls.__token.for_user(user)
