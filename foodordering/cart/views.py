from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from restaurants.models import MenuItem
from .utils import add_item, change_qty, clear_cart, get_cart, safe_next


def cart_view(request):
    cart = get_cart(request)
    short_by = 0
    if cart["restaurant"]:
        short_by = max(0, cart["restaurant"].min_order - cart["subtotal"])
    return render(request, "cart/cart.html", {"cart": cart, "below_min": short_by > 0, "short_by": short_by})


def cart_add(request, id):
    item = get_object_or_404(MenuItem, id=id)
    default = reverse("restaurant_detail", args=[item.restaurant_id])
    if request.method != "POST":
        return redirect(default)

    current = get_cart(request)
    other_restaurant = current["restaurant"] and current["restaurant"].id != item.restaurant_id
    if other_restaurant and not request.POST.get("replace"):
        # like Swiggy: ask before throwing away the old cart
        context = {"item": item, "current": current["restaurant"], "next": safe_next(request, default)}
        return render(request, "cart/conflict.html", context)

    add_item(request, item)
    return redirect(safe_next(request, default))


def cart_update(request, id):
    if request.method == "POST":
        delta = 1 if request.POST.get("action") == "inc" else -1
        change_qty(request, id, delta)
    return redirect(safe_next(request, reverse("cart")))


def cart_clear(request):
    if request.method == "POST":
        clear_cart(request)
    return redirect("cart")
