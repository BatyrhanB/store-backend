from rest_framework import views, response, status

from store.services.cart_services import Cart


class CartAPI(views.APIView):
    """
    API view to handle cart operations such as adding, removing, and clearing items from the cart.
    """

    def get(self, request, format=None):
        """
        Handles GET requests to retrieve cart data.

        Args:
            request: HTTP request object.
            format: Optional format of the response (default is None).

        Returns:
            HTTP response containing cart data and total price.

        """
        cart = Cart(request)

        return response.Response(
            {"data": list(cart.__iter__()), "cart_total_price": cart.get_total_price()}, status=status.HTTP_200_OK
        )

    def post(self, request, **kwargs):
        """
        Handles POST requests to modify the cart.

        Args:
            request: HTTP request object.
            **kwargs: Additional keyword arguments.

        Returns:
            HTTP response confirming the cart update.

        """
        cart = Cart(request)

        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product)

        elif "clear" in request.data:
            cart.clear()

        else:
            product = request.data
            cart.add(
                product=product["product"],
                quantity=product["quantity"],
                overide_quantity=product.get("override_quantity", False),
            )

        return response.Response({"message": "cart updated"}, status=status.HTTP_202_ACCEPTED)
