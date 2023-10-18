"""Lead app views."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from lead.forms import AddLeadForm


@login_required
def add_lead(request):
    """Add lead view."""
    if request.method == "POST":
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)  # set to false to set created_by
            lead.created_by = request.user
            lead.save()

            return redirect("dashboard:dashboard")

    form = AddLeadForm()

    return render(request, "lead/add_lead.html", {"form": form})
