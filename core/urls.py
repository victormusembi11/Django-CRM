from django.urls import path

from core.views import home, about

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
]
