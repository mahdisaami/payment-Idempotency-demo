from django.urls import path

from payments.views import StartPaymentView

urlpatterns = [
    path("start/", StartPaymentView.as_view(), name="start-payment"),
]
