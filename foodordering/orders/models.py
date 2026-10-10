from django.db import models
from restaurants.models import Restaurant

STATUS_STEPS = [
    ("placed", "Order placed"),
    ("preparing", "Preparing your food"),
    ("on_the_way", "Out for delivery"),
    ("delivered", "Delivered"),
]


class Order(models.Model):
    PAYMENT = [("cod", "Cash on delivery"), ("upi", "UPI on delivery")]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="orders")
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    payment = models.CharField(max_length=3, choices=PAYMENT, default="cod")
    subtotal = models.PositiveIntegerField()
    delivery_fee = models.PositiveIntegerField()
    tax = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=12, choices=STATUS_STEPS, default="placed")
    created = models.DateTimeField(auto_now_add=True)

    def status_index(self):
        return [key for key, _ in STATUS_STEPS].index(self.status)

    def next_status(self):
        keys = [key for key, _ in STATUS_STEPS]
        i = self.status_index()
        return keys[min(i + 1, len(keys) - 1)]

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)          # copied, so old orders keep their price
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def line_total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.name}"
