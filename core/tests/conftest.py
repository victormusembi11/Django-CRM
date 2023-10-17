"""Test fixtures for core app."""
import pytest
from django.test import Client


@pytest.fixture
def client() -> Client:
    """Test client fixture."""
    return Client()
