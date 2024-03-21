from django.urls import path

from store.apis.product_apis import ProductListAPIView, ProductCreateAPIVIew, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("list/", ProductListAPIView.as_view(), name="product-get"),
    path("create/", ProductCreateAPIVIew.as_view(), name="product-post"),
    path("detail/<uuid:pk>/", ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-retrive"),
]
