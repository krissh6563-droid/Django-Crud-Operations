from django.urls import path
from .views import member
from .views import add
from .views import edit

urlpatterns = [
    path("", member, name="home"),
    path('add', add, name='add'),
    path('edit', edit, name='edit'),
]
