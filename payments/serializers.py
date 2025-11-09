from rest_framework import serializers

from payments.models import Payment


class PaymentStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["order_id", "amount"]
