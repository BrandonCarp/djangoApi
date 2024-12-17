from django.urls import path
from .views import fetch_news

urlpatterns = [
    path('api/news/', fetch_news, name='fetch_news'),
]
