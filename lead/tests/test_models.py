"""Lead model tests."""
import pytest

pytestmark = pytest.mark.django_db


def test_lead_model(lead):
    """Test lead model."""
    assert lead.name == "John Doe"
    assert lead.email == "johndoe@example.com"
    assert lead.description == "Test description"
    assert lead.priority == "medium"
    assert lead.status == "new"
    assert lead.created_at
    assert lead.modified_at
    assert str(lead) == "John Doe"
