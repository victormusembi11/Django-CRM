"""Client views."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from client.models import Client


@login_required
def client_list(request):
    """Client list view."""
    clients = Client.objects.filter(created_by=request.user)
    return render(request, "client/client_list.html", {"clients": clients})
