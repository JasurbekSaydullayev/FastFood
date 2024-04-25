import uuid

from django.db import models
from foods.models import Food
from users.models import User


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Food, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_distance = models.FloatField(default=0)
    delivery_time = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"
