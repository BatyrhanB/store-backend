from django.urls import path

from store.apis.order_apis import PlaceOrderAPIView, OrderListAPIView


urlpatterns = [
    path("place/", PlaceOrderAPIView.as_view(), name="order-post"),
    path("list/", OrderListAPIView.as_view(), name="order-get"),
]
