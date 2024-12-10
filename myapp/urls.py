from django.urls import path
from .views import TodoListView, home

urlpatterns = [
    path("", home, name="home"),  # Maps to the home view
    path("todos/", TodoListView.as_view(), name="todos"),  # Maps to the API view
]
