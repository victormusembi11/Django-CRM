"""Dashboard views tests."""
import pytest
from django.contrib.auth.models import User
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_dashboard_view(client):
    """Test dashboard view."""
    User.objects.create_user(username="janedoe", password="password")
    client.login(username="janedoe", password="password")

    response = client.get(reverse("dashboard:dashboard"))

    assert response.status_code == 200
    assert response.context["user"].is_authenticated


def test_dashboard_view_unauthenticated(client):
    """Test dashboard view unauthenticated."""
    response = client.get(reverse("dashboard:dashboard"))

    assert response.status_code == 302
    assert response.url == "/accounts/login/?next=/dashboard/"
