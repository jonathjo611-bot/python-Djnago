from django.utils.http import url_has_allowed_host_and_scheme

from restaurants.models import MenuItem, Restaurant

TAX_PERCENT = 5


def get_cart(request):
    """Read the cart from the session and work out the bill.

    The session stores:  {"restaurant": 3, "items": {"12": 2, "15": 1}}
    (JSON turns the item ids into strings, so we convert back to int when needed)
    """
    raw = request.session.get("cart") or {}
    items = raw.get("items", {})
    restaurant = Restaurant.objects.filter(id=raw.get("restaurant")).first() if items else None

    lines, subtotal, count = [], 0, 0
    if restaurant:
        menu = MenuItem.objects.filter(restaurant=restaurant, id__in=[int(i) for i in items])
        for item in menu:
            qty = items[str(item.id)]
            lines.append({"item": item, "qty": qty, "total": item.price * qty})
            subtotal += item.price * qty
            count += qty

    fee = restaurant.delivery_fee if lines else 0
    tax = (subtotal * TAX_PERCENT + 50) // 100          # round half up, in whole rupees
    return {
        "restaurant": restaurant if lines else None,
        "lines": lines,
        "count": count,
        "subtotal": subtotal,
        "delivery_fee": fee,
        "tax": tax,
        "tax_percent": TAX_PERCENT,
        "total": subtotal + fee + tax,
    }


def add_item(request, item):
    cart = request.session.get("cart") or {}
    if cart.get("restaurant") != item.restaurant_id:     # a cart holds ONE restaurant
        cart = {"restaurant": item.restaurant_id, "items": {}}
    items = cart.setdefault("items", {})
    items[str(item.id)] = items.get(str(item.id), 0) + 1
    request.session["cart"] = cart


def change_qty(request, item_id, delta):
    cart = request.session.get("cart") or {}
    items = cart.get("items", {})
    key = str(item_id)
    if key in items:
        items[key] += delta
        if items[key] <= 0:
            del items[key]
        request.session["cart"] = cart


def clear_cart(request):
    request.session.pop("cart", None)


def safe_next(request, default):
    """Where to go back to after a button press - only pages on this same site."""
    url = request.POST.get("next", "")
    if url_has_allowed_host_and_scheme(url, allowed_hosts={request.get_host()}):
        return url
    return default
