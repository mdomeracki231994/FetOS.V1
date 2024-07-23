from django.urls import path
from .views import create_producer, producer_profile_page, producer_dashboard_page

urlpatterns = [
    path('create/', create_producer, name='create_producer'),
    path('dashboard/', producer_dashboard_page, name='producer_dashboard'),
    path('profile/', producer_profile_page, name='producer_profile')
]
