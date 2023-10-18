"""Lead app views."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.forms import AddLeadForm


@login_required
def add_lead(request):
    """Add lead view."""
    form = AddLeadForm()
    return render(request, "lead/add_lead.html", {"form": form})
