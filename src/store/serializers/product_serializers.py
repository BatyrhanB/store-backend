from rest_framework import serializers

from store.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "category", "description", "price", "created_at"]


class ProductInCartSerializer(ProductListSerializer):
    pass


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "category", "description", "price", "created_at"]
        read_only_fields = ["id", "created_at"]


class ProductRetrieveUpdateDestroySerializer(ProductCreateSerializer):
    pass
