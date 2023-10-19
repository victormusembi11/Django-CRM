"""Lead app urls."""
from django.urls import path

from . import views

app_name = "lead"

urlpatterns = [
    path("", views.lead_list, name="lead_list"),
    path("add/", views.add_lead, name="add_lead"),
]
