"""Client fixtures."""
import pytest
from django.contrib.auth.models import User

from client.models import Client


@pytest.fixture
def user(db):
    """Create user."""
    return User.objects.create_user(username="testuser", password="123")


@pytest.fixture
def client(db, user):
    """Create client."""
    return Client.objects.create(
        name="testclient", email="testclient@example.com", created_by=user
    )
