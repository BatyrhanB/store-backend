from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    address = serializers.CharField()