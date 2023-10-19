"""Test views."""
import pytest

pytestmark = pytest.mark.django_db


def test_lead_list(auth_client):
    """Test lead list view."""
    response = auth_client.get("/lead/")
    assert response.status_code == 200
    assert "lead/lead_list.html" in (t.name for t in response.templates)
    assert "leads" in response.context


def test_add_lead(auth_client):
    """Test add lead view."""
    response = auth_client.get("/lead/add/")
    assert response.status_code == 200
    assert "lead/add_lead.html" in (t.name for t in response.templates)


def test_lead_detail(auth_client, lead):
    """Test lead detail view."""
    response = auth_client.get(f"/lead/{lead.pk}/")
    assert response.status_code == 200
    assert "lead/lead_detail.html" in (t.name for t in response.templates)
    assert "lead" in response.context


def test_lead_delete(auth_client, lead):
    """Test lead delete and redirect."""
    response = auth_client.get(f"/lead/{lead.pk}/delete/")
    assert response.status_code == 302
    assert response.url == "/lead/"


def test_lead_edit(auth_client, lead):
    """Test lead edit view."""
    response = auth_client.get(f"/lead/{lead.pk}/edit/")
    assert response.status_code == 200
    assert "lead/lead_edit.html" in (t.name for t in response.templates)
    assert "form" in response.context


def test_lead_edit_post(auth_client, lead):
    """Test lead edit post view."""
    data = {
        "name": lead.name + " edited",
        "email": lead.email,
        "description": lead.description + " edited",
        "priority": lead.priority,
        "status": lead.status,
    }
    response = auth_client.post(f"/lead/{lead.pk}/edit/", data=data)
    assert response.status_code == 302
    assert response.url == "/lead/"


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
    assert response.url == "/lead/"
