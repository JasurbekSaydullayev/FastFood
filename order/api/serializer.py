from rest_framework import serializers
from foods.models import Food
from foods.api.serializers import FoodSerializer
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), many=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    delivery_time = serializers.IntegerField(read_only=True)
    delivered = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        price = sum(item.price for item in order_items_data)
        validated_data['price'] = price
        number_not_delivered_orders = Order.objects.filter(delivered=False).count()
        delivery_time = validated_data['delivery_distance'] * 3 + number_not_delivered_orders * 1.25
        validated_data['delivery_time'] = delivery_time
        order = Order.objects.create(**validated_data)
        order.order_items.set(order_items_data)
        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_items')
        instance.order_items.clear()
        instance.price = 0
        for item_data in order_items_data:
            instance.order_items.add(item_data)
            instance.price += item_data.price
        instance.save()
        return instance



