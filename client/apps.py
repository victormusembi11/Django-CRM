"""Client configuration."""
from django.apps import AppConfig


class ClientConfig(AppConfig):
    """Client configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "client"
