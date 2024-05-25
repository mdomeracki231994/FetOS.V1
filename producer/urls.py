from django.urls import path
from .views import create_producer

urlpatterns = [
    path('create/', create_producer, name='create_producer')
]
