import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from payments.models import Payment
from payments.serializers import PaymentStartSerializer


class StartPaymentView(APIView):
    def post(self, request):
        serializer = PaymentStartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_id = serializer.validated_data["order_id"]
        amount = serializer.validated_data["amount"]

        payment, _ = Payment.objects.get_or_create(order_id=order_id, defaults={"amount": amount})

        try:
            response = requests.post("http://localhost:8000/fake-gateway/start/")
            if response.status_code == 200:
                payment.payment_id = response.json().get("payment_id")
                payment.status = "COMPLETED"
                payment.save()
                return Response({"payment_id": payment.payment_id}, status=status.HTTP_200_OK)
            else:
                payment.status = "FAILED"
                payment.save()
                return Response({"error": "Gateway error"}, status=response.status_code)

        except requests.RequestException:
            payment.status = "FAILED"
            payment.save()
            return Response({"error": "Gateway unreachable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
