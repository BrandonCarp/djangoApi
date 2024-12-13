from django.urls import path
from .views import BlogListCreateView


urlpatterns = [
    # path("", home, name="home"),  # Maps to the home view
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create')
    # path("user/create/", UserCreateView.as_view(), name="user-create"),  # User creation endpoint
    # path("user/login/", UserLoginView.as_view(), name="user-login"),  # User login endpoint
]
