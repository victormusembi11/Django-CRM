"""Client views."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from client.models import Client


@login_required
def client_list(request):
    """Client list view."""
    clients = Client.objects.filter(created_by=request.user)
    return render(request, "client/client_list.html", {"clients": clients})


@login_required
def client_detail(request, pk):
    """Client detail view."""
    client = get_object_or_404(Client, pk=pk, created_by=request.user)
    return render(request, "client/client_detail.html", {"client": client})
