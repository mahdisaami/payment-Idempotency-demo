from django.apps import AppConfig


class FakeGatewayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_gateway'
