"""Client views tests."""
import pytest
from django.urls import reverse_lazy

pytestmark = pytest.mark.django_db


def test_client_list_view(auth_client):
    """Test client list view."""
    response = auth_client.get(reverse_lazy("client:client_list"))
    assert response.status_code == 200


def test_client_detail_view(auth_client, client):
    """Test client detail view."""
    response = auth_client.get(
        reverse_lazy("client:client_detail", kwargs={"pk": client.pk})
    )
    assert response.status_code == 200
