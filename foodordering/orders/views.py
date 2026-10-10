from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from cart.utils import clear_cart, get_cart
from .forms import CheckoutForm
from .models import STATUS_STEPS, Order, OrderItem


def _my_order_ids(request):
    return request.session.get("orders", [])


def checkout(request):
    cart = get_cart(request)
    if not cart["lines"]:
        return redirect("cart")

    below_min = cart["subtotal"] < cart["restaurant"].min_order
    form = CheckoutForm(request.POST or None)

    if request.method == "POST" and not below_min and form.is_valid():
        d = form.cleaned_data
        with transaction.atomic():
            order = Order.objects.create(
                restaurant=cart["restaurant"], customer_name=d["name"], phone=d["phone"],
                address=d["address"], payment=d["payment"], subtotal=cart["subtotal"],
                delivery_fee=cart["delivery_fee"], tax=cart["tax"], total=cart["total"],
            )
            for line in cart["lines"]:
                OrderItem.objects.create(order=order, name=line["item"].name,
                                         price=line["item"].price, quantity=line["qty"])
        clear_cart(request)
        request.session["orders"] = _my_order_ids(request) + [order.id]
        return redirect("order_track", id=order.id)

    return render(request, "orders/checkout.html", {"cart": cart, "form": form, "below_min": below_min})


def order_track(request, id):
    if id not in _my_order_ids(request):          # you can only see your own orders
        return render(request, "orders/not_yours.html", status=404)
    order = get_object_or_404(Order, id=id)
    current = order.status_index()
    steps = [{"label": label, "done": i <= current, "now": i == current}
             for i, (_, label) in enumerate(STATUS_STEPS)]
    return render(request, "orders/track.html", {"order": order, "steps": steps})


def order_advance(request, id):
    """DEMO button: pretend time has passed and move the order to its next step."""
    if id in _my_order_ids(request) and request.method == "POST":
        order = get_object_or_404(Order, id=id)
        order.status = order.next_status()
        order.save()
    return redirect("order_track", id=id)


def order_history(request):
    orders = Order.objects.filter(id__in=_my_order_ids(request)).select_related("restaurant").order_by("-created")
    return render(request, "orders/history.html", {"orders": orders})
