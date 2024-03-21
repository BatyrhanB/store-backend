import jwt
from datetime import datetime, timedelta

from typing import Union
from django.db import transaction
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate

from common.exceptions import (
    UserAlreadyExistException,
    SomethingGetWrongException,
    TokenExpiredException,
    ObjectNotFoundException,
)
from common.validators.password_validators import validate_user_password
from user.models import User
from user.services.token_services import JWTTokenService
from user.services.email_services import EmailService


class AuthService(object):
    __user_model = User

    @classmethod
    def signup(cls, email: str, password: str, confirm_password: str, request, **kwargs) -> Union[dict, None]:
        """
        User sign up
        :args
            email (str): _user's email_
            password (str): _user's password_
            confirm_password (str): _confirm password_
        :raises
            AlreadyExist: _return statusCode about already existing user_
            SomethingGetWrongException: _return statusCode about unknown server error_
        :returns
            Union[dict, None]: _return message about user succesfully signed up,
            and need to verify it or None what means exceptions object_
        """
        exist_user: User = cls.__user_model.objects.filter(email=email).first()
        if exist_user and exist_user.is_active and exist_user.is_verified:
            raise UserAlreadyExistException({"message": "User already exist"})

        verified_password: str = validate_user_password(password, confirm_password)
        try:
            with transaction.atomic():
                if exist_user:
                    exist_user.set_password(verified_password)
                    exist_user.save()
                else:
                    user = cls.__user_model.objects.create_user(email=email, password=verified_password, **kwargs)

                EmailService.send_email(
                    email=email,
                    verifcation_link=cls.get_verification_link(user, request=request),
                )
                response: dict = {"message": "User successfully signed up, please verify your email"}
                return response
        except Exception:
            raise SomethingGetWrongException({"message": "Something get wrong"})

    @staticmethod
    def get_verification_link(user, request) -> str:
        """
        Get verification link
        :args user: user instance
        :returns str: verification link
        """
        token_payload = {"email": user.email, "exp": datetime.utcnow() + timedelta(days=1)}
        jwt_token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm="HS256")

        base_url = request.build_absolute_uri("/")[:-1]
        confirmation_url = base_url + reverse("user-verify")
        confirmation_url += f"?token={jwt_token}"
        return confirmation_url

    @classmethod
    def verify_email_user(cls, token) -> dict:
        """
        Verify email user
        :args
            token (str): _token_
        :raises
            TokenExpiredException: _return statusCode about token expired_
            ObjectNotFoundException: _return statusCode about user not found_
        :returns
            dict: _return message about user succesfully verified,
            and need to verify it or None what means exceptions object_
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise TokenExpiredException({"message": "Token expired"})
        except jwt.DecodeError:
            return None
        email = payload.get("email")

        try:
            user = cls.__user_model.objects.get(email=email)
        except User.DoesNotExist:
            raise ObjectNotFoundException({"message": "User not found"})

        user.verified = True
        user.save()

        return JWTTokenService.generate_token(email=user.email)

    @classmethod
    def sign_in(cls, email: str, password: str):
        """
        Sign in user
        :args
            email (str): _user's email_
            password (str): _user's password_
        :raises
            ObjectNotFoundException: _return statusCode about user not found_
        :returns
            dict: _return message about user succesfully signed in,
            and need to verify it or None what means exceptions object_
        """
        user = authenticate(email=email, password=password)
        if user:
            return JWTTokenService.generate_token(email=user.email)
        else:
            raise ObjectNotFoundException("User not found or not active or data is not valid")
