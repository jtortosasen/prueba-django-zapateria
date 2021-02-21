from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Item
        model = Item
        fields = ['name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        from .models import Order
        model = Order
        fields = ['date_created', 'items']


