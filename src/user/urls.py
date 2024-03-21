from django.urls import path, include


urlpatterns = [
    path("auth/", include("user.routes.auth_routes"), name="auth-main"),
]
