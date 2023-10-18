"""Lead test fixtures."""
import pytest
from django.contrib.auth.models import User
from django.test import Client

from lead.models import Lead


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
    )
    user.set_password("password")
    user.save()
    return user


@pytest.fixture
def lead(user):
    """Test lead."""
    lead = Lead.objects.create(
        name="John Doe",
        email="johndoe@example.com",
        description="Test description",
        created_by=user,
    )
    lead.save()
    return lead
