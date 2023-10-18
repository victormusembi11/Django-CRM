"""Test views."""
import pytest

pytestmark = pytest.mark.django_db


def test_add_lead(auth_client):
    """Test add lead view."""
    response = auth_client.get("/lead/add/")
    assert response.status_code == 200
    assert "lead/add_lead.html" in (t.name for t in response.templates)


def test_add_lead_post(auth_client):
    """Test add lead post view."""
    data = {
        "name": "test",
        "email": "johndoe@example.com",
        "description": "test",
        "priority": "low",
        "status": "new",
    }
    response = auth_client.post("/lead/add/", data=data)
    assert response.status_code == 302
    assert response.url == "/dashboard/"
