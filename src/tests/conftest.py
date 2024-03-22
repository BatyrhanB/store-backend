import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from user.models import User


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def user():
    return baker.make(User)
