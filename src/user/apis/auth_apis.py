from django.http import HttpRequest
from rest_framework import generics, response, permissions

from user.serializers.auth_serializers import SignUpSerializer, SignInSerializer
from user.services.auth_services import AuthService
from user.models import User


class SignUpAPIView(generics.GenericAPIView):
    """
    API for signing up
    """

    serializer_class = SignUpSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = AuthService.signup(
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
            confirm_password=serializer.validated_data.get("confirm_password"),
            request=request,
        )
        return response.Response(result)


class UserVerificationAPIView(generics.GenericAPIView):
    """
    API for verifying user
    """

    queryset = User.objects.filter(is_deleted=False)
    permission_classes = (permissions.AllowAny,)

    def get(self, request: HttpRequest, *args, **kwargs):
        token = request.GET.get("token")
        token = AuthService.verify_email_user(token)
        return response.Response(
            {
                "message": "Email verified successfully",
                "results": {
                    "refresh_token": str(token),
                    "access_token": str(token.access_token),
                    "token_type": "Bearer",
                },
            }
        )


class SignInAPIView(generics.GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request: HttpRequest, *args, **kwargs) -> response.Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = AuthService.sign_in(serializer.validated_data.get("email"), serializer.validated_data.get("password"))
        return response.Response(
            {
                "message": "You signed in successfully",
                "results": {
                    "refresh_token": str(token),
                    "access_token": str(token.access_token),
                    "token_type": "Bearer",
                },
            }
        )
