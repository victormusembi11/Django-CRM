"""Test fixtures for accounts app."""
import pytest
from django.contrib.auth.models import User
from django.test import Client

from accounts.models import UserProfile


@pytest.fixture
def client() -> Client:
    """Test client fixture."""
    return Client()


@pytest.fixture
def user():
    """User test fixture."""
    user = User.objects.create(username="johndoe", email="johndoe@example.com")
    user.set_password("john@123")
    user.save()
    return user


@pytest.fixture
def user_profile(user):
    """User profile test fixture."""
    return UserProfile.objects.create(user=user)
