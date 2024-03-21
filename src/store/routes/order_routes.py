from django.urls import path

from store.apis.order_apis import PlaceOrderAPIView


urlpatterns = [
    path("place/", PlaceOrderAPIView.as_view(), name="order-post"),
]
