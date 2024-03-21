from rest_framework import serializers

from store.models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), write_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "product", "review", "rating", "created_at"]
        read_only_fields = ["id", "created_at"]
