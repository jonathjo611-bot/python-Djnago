from django.shortcuts import render
from .forms import BillForm

FIXED_CHARGE = 50  # rupees, added to every bill


def calculate_bill(units):
    """Slab rates: each slab is charged only for the units that fall inside it."""
    slabs = [
        (100, 3),             # first 100 units  -> Rs 3 per unit
        (100, 5),             # next 100 units   -> Rs 5 per unit
        (100, 7),             # next 100 units   -> Rs 7 per unit
        (float("inf"), 9),    # everything above -> Rs 9 per unit
    ]
    breakdown = []
    remaining = units
    for size, rate in slabs:
        if remaining <= 0:
            break
        used = min(remaining, size)
        breakdown.append({"units": used, "rate": rate, "amount": used * rate})
        remaining -= used
    energy_charge = sum(row["amount"] for row in breakdown)
    return breakdown, energy_charge


def bill_view(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            units = form.cleaned_data["units"]
            breakdown, energy_charge = calculate_bill(units)
            context = {
                "name": name,
                "units": units,
                "breakdown": breakdown,
                "energy_charge": energy_charge,
                "fixed_charge": FIXED_CHARGE,
                "total": energy_charge + FIXED_CHARGE,
            }
            return render(request, "bill/2.html", context)
    else:
        form = BillForm()
    # GET request, or POST with errors: show the form (errors appear automatically)
    return render(request, "bill/1.html", {"form": form})
