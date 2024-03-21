from django.urls import path, include


urlpatterns = [
    path("cart/", include("store.routes.cart_routes"), name="cart-main"),
    path("product/", include("store.routes.product_routes"), name="product-main"),
    path("review/", include("store.routes.review_routes"), name="review-main"),
    path("order/", include("store.routes.order_routes"), name="order-main"),
]
