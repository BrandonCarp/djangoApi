from django.urls import path
from .views import TodoListView, home, UserCreateView, UserLoginView

urlpatterns = [
    path("", home, name="home"),  # Maps to the home view
    path("todos/", TodoListView.as_view(), name="todos"),  # Maps to the API view
    path("user/create/", UserCreateView.as_view(), name="user-create"),  # User creation endpoint
    path("user/login/", UserLoginView.as_view(), name="user-login"),  # User login endpoint
]
