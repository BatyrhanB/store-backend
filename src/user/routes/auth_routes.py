from django.urls import path

from user.apis.auth_apis import SignUpAPIView, UserVerificationAPIView, SignInAPIView


urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="user-sign-up"),
    path("verify/", UserVerificationAPIView.as_view(), name="user-verify"),
    path("signin/", SignInAPIView.as_view(), name="user-sign-in"),
]
