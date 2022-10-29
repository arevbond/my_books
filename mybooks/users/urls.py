from django.urls import path, include
from .views import *


# app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('all_users/', AllUsersView.as_view(), name='all_users')
]
