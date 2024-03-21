from django.urls import path, include


urlpatterns = [
    path("cart/", include("store.routes.cart_routes"), name="cart-main"),
    path("product/", include("store.routes.product_routes"), name="product-main"),
]
