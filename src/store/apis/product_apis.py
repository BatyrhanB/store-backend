from rest_framework import generics, permissions

from store.models import Product
from store.serializers.product_serializers import (
    ProductListSerializer,
    ProductCreateSerializer,
    ProductRetrieveUpdateDestroySerializer,
)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)


class ProductCreateAPIVIew(generics.CreateAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.AllowAny,)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductRetrieveUpdateDestroySerializer
    permission_classes = (permissions.AllowAny,)
