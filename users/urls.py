from django.urls import path
from users.views import login, register, profile, logout, users

app_name = 'users'

urlpatterns = [
    path('', users, name='/users/'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')
]