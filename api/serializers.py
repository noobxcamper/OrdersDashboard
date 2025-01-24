from rest_framework import serializers
from core.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'responder',
            'submission_id',
            'submission_date',
            'department',
            'items',
            'price',
            'variation',
            'notes',
            'quantity',
            'ship_to',
            'shipping_address',
            'hyperlink',
            'tracking_url',
            'private_notes'
        )