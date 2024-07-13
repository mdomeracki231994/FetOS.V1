from django.urls import path
from .views import create, update

urlpatterns = [
    path('create/', create, name='create_talent'),
    path('update/', update, name='update_talent'),
]
