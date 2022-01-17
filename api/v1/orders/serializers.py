from rest_framework import serializers
from core.models import Order


class OrderGenerateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'amount',
            'discount',
            'transaction_id',
            'created_at',
            'status'
        ]