from django.urls import path, include
from .views import RegisterUser


# app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
]
