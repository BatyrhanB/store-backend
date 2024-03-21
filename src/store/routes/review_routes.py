from django.urls import path

from store.apis.review_apis import ReviewCreateAPIView

urlpatterns = [
    path("create/", ReviewCreateAPIView.as_view(), name="review-post"),
]
