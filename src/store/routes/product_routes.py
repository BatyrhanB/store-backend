from django.urls import path

from store.apis.product_apis import ProductListAPIView


urlpatterns = [
    path("list/", ProductListAPIView.as_view(), name="product-get"),
]
