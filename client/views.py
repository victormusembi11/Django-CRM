"""Client views."""
from django.shortcuts import render

from client.models import Client


def client_list(request):
    """Client list view."""
    clients = Client.objects.filter(created_by=request.user)
    return render(request, "client/client_list.html", {"clients": clients})
