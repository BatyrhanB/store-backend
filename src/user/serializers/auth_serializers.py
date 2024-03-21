from rest_framework import serializers


class SignUpSerializer(serializers.Serializer):
    """
    Serializer for signing up
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True)


class SignInSerializer(serializers.Serializer):
    """
    Serializer for signing in
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)
