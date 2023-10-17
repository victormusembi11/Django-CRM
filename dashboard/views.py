"""Dashboard views."""
from django.shortcuts import render


def dashboard_view(request):
    """Dashboard view."""
    return render(request, "dashboard/dashboard.html")
