"""Client urls."""
from django.urls import path

from . import views

app_name = "client"

urlpatterns = [
    path("", views.client_list, name="client_list"),
]
