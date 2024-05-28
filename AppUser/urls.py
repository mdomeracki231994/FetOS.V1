from django.urls import path
from .views import register_user, login_user, logout_user


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register')
]