import pytest
from rest_framework.exceptions import ErrorDetail

from store.serializers.product_serializers import ProductListSerializer
from tests.store.factories import ProductFactory


class TestProductListSerializer:
    def test_statistic_serialize_model(self):
        statistics = ProductFactory.build()
        serializer = ProductListSerializer(statistics)

        assert serializer.data

    @pytest.mark.django_db
    def test_invalid_serializer(self):
        serializer = ProductListSerializer(
            data={"title": "test_title", "category": 1, "description": "test_description", "price": 23}
        )
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {"title": "test_title", "category": 1, "description": "test_description", "price": 23}
        assert serializer.errors == {
            "category": [ErrorDetail(string='Invalid pk "1" - object does not exist.', code="does_not_exist")]
        }

    def test_invalid_datatype(self):
        serializer = ProductListSerializer(
            data=[{"title": "test_title", "category": 1, "description": "test_description", "price": 23}]
        )
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {}
        assert serializer.errors == {
            "non_field_errors": [
                ErrorDetail(string="Invalid data. Expected a dictionary, but got list.", code="invalid")
            ]
        }

    def test_empty_serializer(self):
        serializer = ProductListSerializer()
        assert serializer.data == {
            "title": "",
            "category": None,
            "description": "",
            "price": None,
        }

    def test_validate_none_data(self):
        data = None
        serializer = ProductListSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors == {"non_field_errors": ["No data provided"]}

    def test_missing_attribute_during_serialization(self):
        class MissingAttributes:
            pass

        instance = MissingAttributes()
        serializer = ProductListSerializer(instance)
        with pytest.raises(AttributeError):
            serializer.data
