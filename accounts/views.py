"""Accounts views."""
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def signup(request):
    """User create form view."""
    form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
