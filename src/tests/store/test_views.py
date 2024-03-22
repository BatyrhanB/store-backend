import pytest
from model_bakery import baker

from django.urls import reverse
from rest_framework import status

from store.models import Product, Order


pytestmark = pytest.mark.django_db

params_200 = [
    ("product-get"),
]

params_401 = [
    ("order-get"),
]


@pytest.mark.parametrize("param", params_200)
def test_render_list_views_200(client, param):
    url = reverse(param)
    resp = client.get(url)
    assert resp.status_code == 200


@pytest.mark.parametrize("param", params_401)
def test_render_list_views_401(client, param):
    url = reverse(param)
    resp = client.get(url)
    assert resp.status_code == 401


def test_service_details_view(client):
    products = baker.make(Product, _quantity=20)
    for product in products:
        url = reverse("product-retrive", kwargs={"pk": product.id})
        response = client.get(url)
        assert response.status_code == 200


class TestProductEndpoints:

    def test_product_list(self, api_client):
        url = reverse("product-get")
        baker.make(Product, _quantity=10)

        response = api_client().get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 10

    def test_vacancies_list(self, api_client):
        url = reverse("order-get")
        baker.make(Order, _quantity=99)

        response = api_client().get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["detail"] == "Authentication credentials were not provided."
