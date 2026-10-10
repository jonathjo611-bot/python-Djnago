from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "restaurant", "total", "status", "created")
    list_editable = ("status",)           # change the status straight from the list page
    list_filter = ("status", "restaurant")
    search_fields = ("customer_name", "phone")
    inlines = [OrderItemInline]
