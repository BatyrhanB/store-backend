from rest_framework import generics, permissions
from django_filters import rest_framework as filters

from store.models import Product
from store.serializers.product_serializers import (
    ProductListSerializer,
    ProductCreateSerializer,
    ProductRetrieveUpdateDestroySerializer,
)
from store.filters import ProductFilter


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(is_deleted=False).select_related("category")


class ProductCreateAPIVIew(generics.CreateAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.AllowAny,)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductRetrieveUpdateDestroySerializer
    permission_classes = (permissions.AllowAny,)
