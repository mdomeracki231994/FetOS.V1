from django.urls import path
from .views import events_page

urlpatterns = [
    path('events_page/', events_page, name='events_page'),
]
