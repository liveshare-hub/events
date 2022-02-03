from django.urls import path
from .views import loginUser, createUser, logoutUser


urlpatterns = [
    path('register', createUser, name='register'),
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
]
