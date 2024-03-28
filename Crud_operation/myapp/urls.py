from django.urls import path
from .views import member

urlpatterns = [
    path("", member, name="home"),
]
