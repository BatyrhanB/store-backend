from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Title"))

    def __str__(self):
        return f"Category: {self.title}"

    class Meta:
        db_table = "store__categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(BaseModel):
    category = models.ForeignKey(
        "store.Category",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="prodcuts",
        verbose_name=_("Category"),
    )
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Title"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_("Price"))

    def __str__(self):
        return f"Product: {self.title}"

    class Meta:
        db_table = "store__products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Review(BaseModel):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, null=False, blank=False, related_name="reviews", verbose_name=_("User")
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="reviews",
        verbose_name=_("Product"),
    )
    review = models.TextField(null=True, blank=True, verbose_name=_("Review"))
    rating = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_("Rating from (1 to 5)"),
        validators=[
            MaxValueValidator(5, message=_("The value should be no greater than 5.")),
            MinValueValidator(1, message=_("The value must be at least 1.")),
        ],
    )

    def __str__(self):
        return self.review

    class Meta:
        db_table = "store__reviews"
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")


class Order(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("User"))
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_("Total price")
    )
    address = models.CharField(max_length=510, null=False, blank=False, verbose_name=_("Address"))

    def __str__(self):
        return f"{self.user}: {self.address}"

    class Meta:
        db_table = "store__orders"
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(BaseModel):
    order = models.ForeignKey(
        "store.Order", on_delete=models.CASCADE, null=False, blank=False, related_name="items", verbose_name=_("Order")
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="items",
        verbose_name=_("Product"),
    )
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_("Price"))

    def __str__(self):
        return f"{self.order}: {self.product} - {self.quantity}"

    class Meta:
        db_table = "store__order_items"
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")
