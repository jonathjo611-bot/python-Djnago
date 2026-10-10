from django.shortcuts import render
from .forms import DepositForm
from .models import Deposit


def calculate(request):
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():            # validate FIRST, then save
            deposit = form.save()
            return render(request, "fd/2.html", {"d": deposit})
    else:
        form = DepositForm()
    return render(request, "fd/1.html", {"form": form})


def history(request):
    data = Deposit.objects.order_by("-created")
    return render(request, "fd/3.html", {"data": data})
