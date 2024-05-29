from django.urls import path
from .views import create_job


urlpatterns = [
    path('create_job/', create_job, name='create_job'),

]