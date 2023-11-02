"""Client fixtures."""
import pytest
from django.contrib.auth.models import User
from django.test import Client as TestClient

from client.models import Client


@pytest.fixture
def default_client():
    """Test client."""
    return TestClient()


@pytest.fixture
def user():
    """Test user."""
    user = User.objects.create_user(
        username="janedoe",
        email="janedoe@example.com",
    )
    user.set_password("password")
    user.save()
    return user


@pytest.fixture
def auth_client(default_client, user):
    """Test client with authenticated user."""
    default_client.login(username=user.username, password="password")
    return default_client


@pytest.fixture
def client(db, user):
    """Create client."""
    return Client.objects.create(
        name="testclient", email="testclient@example.com", created_by=user
    )
