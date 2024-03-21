import uuid
from django.db import transaction

from store.models import Order, Product, OrderItem


class OrderService:
    """
    A service class handling order-related business logic.

    Methods:
        create_order(user, address, cart): Create an order for a user with the provided address and cart.

    """

    @staticmethod
    def create_order(user, address, cart):
        if len(cart) == 0:
            return None, "Cart is empty. Unable to place order."

        product_ids = [uuid.UUID(product_id) for product_id in cart.cart.keys()]

        products = Product.objects.filter(id__in=product_ids)

        product_map = {str(product.id): product for product in products}

        total_price = sum(
            product_map[str(uuid.UUID(product_id))].price * item["quantity"] for product_id, item in cart.cart.items()
        )

        with transaction.atomic():
            order = Order.objects.create(user=user, total_price=total_price, address=address)
            order_items = [
                OrderItem(
                    order=order,
                    product=product_map[product_id],
                    quantity=item["quantity"],
                    price=product_map[product_id].price,
                )
                for product_id, item in cart.cart.items()
            ]
            OrderItem.objects.bulk_create(order_items)

            cart.clear()

        return order, None
