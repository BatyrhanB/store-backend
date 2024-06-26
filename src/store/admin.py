from django.contrib import admin

from store.models import Category, Product, Review, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    list_display_links = ("title",)
    search_fields = [
        "title",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["title", "created_at", "updated_at"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price", "created_at", "updated_at"]
    list_display_links = ("title",)
    list_filter = ("category",)
    search_fields = [
        "title",
        "description",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["title", "category", "description", "price", "created_at", "updated_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "rating", "created_at", "updated_at"]
    list_display_links = ("product",)
    list_filter = (
        "product",
        "user",
        "rating",
    )
    search_fields = [
        "product",
        "user",
        "review",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["product", "user", "review", "rating", "created_at", "updated_at"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price", "address", "created_at", "updated_at"]
    list_display_links = ("user",)
    list_filter = ("user",)
    search_fields = [
        "user",
        "address",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["user", "total_price", "address", "created_at", "updated_at"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price", "created_at", "updated_at"]
    list_display_links = ("order",)
    list_filter = (
        "order",
        "product",
    )
    search_fields = [
        "order",
        "product",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["order", "product", "quantity", "price", "created_at", "updated_at"]
