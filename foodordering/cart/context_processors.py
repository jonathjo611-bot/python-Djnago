def cart_summary(request):
    """Makes {{ cart_count }} available in every template (used by the navbar badge)."""
    items = (request.session.get("cart") or {}).get("items", {})
    return {"cart_count": sum(items.values())}
