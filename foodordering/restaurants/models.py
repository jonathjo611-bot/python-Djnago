from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    area = models.CharField(max_length=60)
    emoji = models.CharField(max_length=4, default="🍽️")
    description = models.CharField(max_length=200, blank=True)
    rating = models.FloatField(default=4.0)
    delivery_minutes = models.PositiveIntegerField(default=30)
    delivery_fee = models.PositiveIntegerField(default=30, help_text="Rupees. 0 means free delivery")
    min_order = models.PositiveIntegerField(default=100, help_text="Minimum item total, in rupees")
    pure_veg = models.BooleanField(default=False)

    def hue(self):
        return (self.id * 53) % 360

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu")
    section = models.CharField(max_length=50, help_text="e.g. Starters, Mains, Desserts")
    section_order = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    price = models.PositiveIntegerField(help_text="Rupees")
    veg = models.BooleanField(default=True)
    bestseller = models.BooleanField(default=False)

    class Meta:
        ordering = ["section_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.restaurant})"
