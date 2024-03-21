from rest_framework import generics, permissions

from store.models import Review
from store.serializers.review_serializers import ReviewCreateSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.filter(is_deleted=False)
    serializer_class = ReviewCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)
