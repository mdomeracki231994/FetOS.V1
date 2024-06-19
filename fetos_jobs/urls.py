from django.urls import path
from .views import create_job, all_jobs

urlpatterns = [
    path('create_job/', create_job, name='create_job'),
    path('all_jobs/', all_jobs, name='all_jobs'),
]
