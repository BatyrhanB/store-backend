from decimal import Decimal

from django.conf import settings

from store.models import Product
from store.serializers.product_serializers import ProductInCartSerializer


class Cart:
    """
    Class representing a shopping cart for an e-commerce application.

    Attributes:
        session (dict): A dictionary representing the session data for the current user.
        cart (dict): A dictionary representing the contents of the shopping cart, where keys are product IDs
                     and values are dictionaries containing information about each product in the cart.

    Methods:
        __init__(self, request): Initializes the cart object by retrieving or creating a cart in the session.
        save(self): Marks the session as modified to ensure changes are saved.
        add(self, product, quantity=1, overide_quantity=False): Adds a product to the cart or updates its quantity.
        remove(self, product): Removes a product from the cart.
        __iter__(self): Iterates through the items in the cart, fetching product details from the database.
        __len__(self): Returns the total number of items in the cart.
        get_total_price(self): Calculates and returns the total price of all items in the cart.
        clear(self): Clears the cart by removing it from the session.

    """

    def __init__(self, request):
        """
        Initializes the cart object.

        Args:
            request: An HTTP request object containing session data.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save an empty cart in session if it doesn't exist
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        """
        Marks the session as modified to ensure changes are saved.
        """
        self.session.modified = True

    def add(self, product, quantity=1, overide_quantity=False):
        """
        Adds a product to the cart or updates its quantity.

        Args:
            product (dict): A dictionary representing the product being added to the cart.
            quantity (int): The quantity of the product to add (default is 1).
            overide_quantity (bool): Whether to override the quantity if the product is already in the cart.
                                     If False, the quantity will be incremented (default is False).
        """
        product_id = str(product["id"])
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product["price"])}
        if overide_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product):
        """
        Removes a product from the cart.

        Args:
            product (dict): A dictionary representing the product to be removed from the cart.
        """
        product_id = str(product["id"])
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterates through the items in the cart, fetching product details from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = ProductInCartSerializer(product).data
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Returns the total number of items in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculates and returns the total price of all items in the cart.
        """
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())

    def clear(self):
        """
        Clears the cart by removing it from the session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
