from django.urls import path
from .views import events_page, create_event, producer_events_page

urlpatterns = [
    path('events_page/', events_page, name='events_page'),
    path('producer_events_page/', producer_events_page, name='producers_events_page'),
    path('create_event/', create_event, name='create_event'),
]
