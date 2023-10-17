"""Test account views."""
import pytest

pytestmark = pytest.mark.django_db


def test_signup_view(client):
    """Test signup page for status code and template used."""
    response = client.get("/accounts/signup/")

    assert response.status_code == 200
    assert "accounts/signup.html" in (t.name for t in response.templates)


def test_signup_view_post(client):
    """Test signup page for 302 redirect status code after success signup."""
    response = client.post(
        "/accounts/signup/",
        {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
        },
    )

    assert response.status_code == 302
    assert response.url == "/"


def test_signup_view_post_invalid(client):
    """Test signup page for 200 status code after invalid signup."""
    response = client.post(
        "/accounts/signup/",
        {
            "username": "",
            "password1": "",
        },
    )

    assert response.status_code == 200
    assert "accounts/signup.html" in (t.name for t in response.templates)
