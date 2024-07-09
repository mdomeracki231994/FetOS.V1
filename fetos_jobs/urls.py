from django.urls import path
from .views import create_job, all_jobs, create_success

urlpatterns = [
    path('create_job/', create_job, name='create_job'),
    path('create_job_success/', create_success, name='job_create_success'),
    path('all_jobs/', all_jobs, name='all_jobs'),

]
