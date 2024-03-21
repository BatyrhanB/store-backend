from rest_framework import generics, permissions

from store.models import Product
from store.serializers.product_serializers import ProductListSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
