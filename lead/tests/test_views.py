"""Test views."""
import pytest

pytestmark = pytest.mark.django_db


def test_add_lead(auth_client):
    """Test add lead view."""
    response = auth_client.get("/lead/add/")
    assert response.status_code == 200
    assert "lead/add_lead.html" in (t.name for t in response.templates)
