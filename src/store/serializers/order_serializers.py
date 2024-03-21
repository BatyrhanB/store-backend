from rest_framework import serializers

from store.models import Order, OrderItem


class OrderPlaceSerializer(serializers.Serializer):
    address = serializers.CharField()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price"]


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "total_price", "address", "items"]
