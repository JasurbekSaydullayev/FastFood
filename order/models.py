import uuid

from django.db import models
from foods.models import Food
from users.models import User


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location_lang = models.CharField(max_length=50, default='41.3422602')
    location_long = models.CharField(max_length=50, default='69.3371096')
    delivery_time = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='Qabul qilindi')

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.food.name} {self.price} {self.quantity}"
