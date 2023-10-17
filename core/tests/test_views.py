"""Test core views."""


def test_home_view(client):
    """Test home view."""
    response = client.get("/")
    assert response.status_code == 200


def test_about_view(client):
    """Test about view."""
    response = client.get("/about/")
    assert response.status_code == 200
