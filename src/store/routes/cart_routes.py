from django.urls import path

from store.apis.cart_apis import CartAPI


urlpatterns = [
    path("manage-session/", CartAPI.as_view(), name="cart-get-post"),
]
