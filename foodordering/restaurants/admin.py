from django.contrib import admin
from .models import MenuItem, Restaurant


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "cuisine", "area", "rating", "delivery_minutes", "pure_veg")
    list_filter = ("cuisine", "pure_veg")
    search_fields = ("name", "cuisine")
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "section", "price", "veg", "bestseller")
    list_filter = ("restaurant", "veg", "bestseller")
    search_fields = ("name",)
