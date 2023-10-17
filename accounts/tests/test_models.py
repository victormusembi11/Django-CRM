"""Test user model."""
import pytest
from django.contrib.auth.models import User

from accounts.models import UserProfile

pytestmark = pytest.mark.django_db


def test_user_create(user):
    """Test user model creaded."""
    assert isinstance(user, User) is True


def test_user_profile_created(user_profile):
    """Test user profile created."""
    assert isinstance(user_profile, UserProfile) is True


def test_user_profile_model_str(user_profile):
    """Test user profile model str."""
    assert str(user_profile) == user_profile.user.username
