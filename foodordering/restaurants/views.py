from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from cart.utils import get_cart
from .models import Restaurant

SORTS = {"rating": "-rating", "time": "delivery_minutes", "fee": "delivery_fee"}


def restaurant_list(request):
    q = request.GET.get("q", "").strip()
    cuisine = request.GET.get("cuisine", "")
    veg_only = request.GET.get("veg") == "1"
    sort = request.GET.get("sort", "rating")

    restaurants = Restaurant.objects.all()
    if q:
        # match the restaurant name, its cuisine, OR any dish on its menu
        restaurants = restaurants.filter(
            Q(name__icontains=q) | Q(cuisine__icontains=q) | Q(menu__name__icontains=q)
        ).distinct()
    if cuisine:
        restaurants = restaurants.filter(cuisine=cuisine)
    if veg_only:
        restaurants = restaurants.filter(pure_veg=True)
    restaurants = restaurants.order_by(SORTS.get(sort, "-rating"), "name")

    context = {
        "restaurants": restaurants,
        "cuisines": Restaurant.objects.order_by("cuisine").values_list("cuisine", flat=True).distinct(),
        "q": q, "cuisine": cuisine, "veg_only": veg_only, "sort": sort,
    }
    return render(request, "restaurants/list.html", context)


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    cart = get_cart(request)
    here = cart["restaurant"] is not None and cart["restaurant"].id == restaurant.id
    context = {
        "restaurant": restaurant,
        "items": restaurant.menu.all(),
        # {item id: quantity} so the template can show ADD or a + / - stepper
        "qtys": {line["item"].id: line["qty"] for line in cart["lines"]} if here else {},
        "cart": cart if here else None,
    }
    return render(request, "restaurants/detail.html", context)
