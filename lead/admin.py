"""Admin configuration for lead app."""
from django.contrib import admin

from lead.models import Lead

admin.site.register(Lead)
