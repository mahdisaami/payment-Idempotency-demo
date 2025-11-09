from django.urls import path
from .views import FakePaymentGatewayView

urlpatterns = [
    path("start/", FakePaymentGatewayView.as_view(), name="fake-payment-start"),
]
