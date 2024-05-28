from django.urls import path
from .views import create_producer, producer_profile_page

urlpatterns = [
    path('create/', create_producer, name='create_producer'),
    path('profile/', producer_profile_page, name='producer_profile')
]
