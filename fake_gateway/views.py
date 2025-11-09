import random, time, uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class FakePaymentGatewayView(APIView):
    def post(self, request):
        if random.random() < 0.3:
            return Response(
                {"error": "Temporary server issue"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        time.sleep(random.uniform(0.5, 2.0))

        payment_id = str(uuid.uuid4())

        return Response({"payment_id": payment_id}, status=status.HTTP_200_OK)
