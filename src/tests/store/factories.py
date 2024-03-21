import factory
from faker import Faker

from store.models import Product, Category, Review, Order, OrderItem
from tests.user.factories import UserFactory

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: "Contacts %d" % n)

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    title = factory.Sequence(lambda n: "Contacts %d" % n)
    description = fake.job()
    price = 200.0

    class Meta:
        model = Product


class ReviewFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    rating = fake.pyint()

    class Meta:
        model = Review


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    total_price = 10000.0

    class Meta:
        model = Order


class OrderItemFactory(factory.django.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = fake.pyint()
    price = factory.LazyAttribute(lambda obj: obj.product.price * obj.quantity)

    class Meta:
        model = OrderItem
