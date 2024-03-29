from django.urls import path
from .views import member
from .views import add
from .views import edit
from .views import update
from .views import delete

urlpatterns = [
    path("", member, name="home"),
    path('add', add, name='add'),
    path('edit', edit, name='edit'),
    path('update/<str:id>', update, name='update'),
    path('delete/<str:id>', delete, name='delete'),
]
