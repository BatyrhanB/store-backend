from django.test import TestCase

from user.models import User
from store.models import Category, Product, Review, Order, OrderItem

from tests.store.factories import CategoryFactory, ProductFactory, ReviewFactory, OrderFactory, OrderItemFactory
from tests.user.factories import UserFactory


class CategoryModelTestCase(TestCase):
    def test_create_category(self):
        category = CategoryFactory()
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(str(category), f"Category: {category.title}")


class ProductModelTestCase(TestCase):
    def test_create_product(self):
        category = CategoryFactory()
        product = ProductFactory(category=category)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(str(product), f"Product: {product.title}")


class ReviewModelTestCase(TestCase):
    def test_create_review(self):
        user = UserFactory()
        product = ProductFactory()
        review = ReviewFactory(user=user, product=product)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.user, user)
        self.assertEqual(review.product, product)


class OrderModelTestCase(TestCase):
    def test_create_order(self):
        user = UserFactory()
        order = OrderFactory(user=user)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.user, user)


class OrderItemModelTestCase(TestCase):
    def test_create_order_item(self):
        order = OrderFactory()
        product = ProductFactory()
        order_item = OrderItemFactory(order=order, product=product)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(order_item.order, order)
        self.assertEqual(order_item.product, product)


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(str(user), user.email)
