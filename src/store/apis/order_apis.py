from rest_framework import generics, response, status, permissions

from store.models import Order
from store.services.cart_services import Cart
from store.services.order_services import OrderService
from store.serializers.order_serializers import OrderPlaceSerializer, OrderListSerializer


class PlaceOrderAPIView(generics.GenericAPIView):
    """
    API endpoint to place an order.

    """

    serializer_class = OrderPlaceSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to place an order.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The response containing the result of the order placement.

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart = Cart(request)

        order, error_message = OrderService.create_order(request.user, serializer.validated_data["address"], cart)

        if error_message:
            return response.Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(
            {"message": "Order placed successfully.", "order_id": order.id}, status=status.HTTP_201_CREATED
        )


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).select_related("user")
