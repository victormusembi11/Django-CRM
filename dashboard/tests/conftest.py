"""Test fixtures for the dashboard app."""
import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.fixture
def client():
    """Test client."""
    return Client()


@pytest.fixture
def user():
    """Test user."""
    user = User.objects.create_user(
        username="janedoe",
        email="janedoe@example.com",
        password="password",
    )
    user.set_password("password")
    user.save()
    return user
