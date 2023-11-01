"""Client models tests."""
import pytest

pytestmark = pytest.mark.django_db


def test_client_model(user, client):
    """Test client model."""
    assert client.name == "testclient"
    assert client.email == "testclient@example.com"
    assert client.created_by == user


def test_client_model_str(client):
    """Test client model str."""
    assert str(client) == "testclient"
