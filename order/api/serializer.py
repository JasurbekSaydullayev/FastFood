from decimal import Decimal

from rest_framework import serializers

from .calculate_delivery_time import calculate_distance
from ..models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    delivery_time = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        total_price = Decimal(0)
        location_delivery = (validated_data['location_lang'], validated_data['location_long'])
        delivery_distance = calculate_distance(location_delivery)
        if delivery_distance > 40:
            raise serializers.ValidationError(
                "Yetkazib berish masofasi 40 km dan oshib ketganligi sababli, Buyurtma qabul qilnmadi")
        delivery_time = 0
        active_orders = Order.objects.filter(status='Qabul qilindi').exclude(id=validated_data.get('id'))
        active_orders = active_orders.prefetch_related('order_items')
        for order in active_orders:
            for order_item in order.order_items.all():
                delivery_time += 1.25 * order_item.quantity
        for item_data in order_items_data:
            delivery_time += 1.25 * item_data['quantity']
            product = item_data['food']
            item_price = product.price * item_data['quantity']
            item_data['price'] = product.price
            total_price += item_price
        validated_data['price'] = total_price

        validated_data['delivery_time'] = delivery_time + delivery_distance * 3

        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
