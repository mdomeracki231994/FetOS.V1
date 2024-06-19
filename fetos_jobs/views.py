from django.shortcuts import render
from django.contrib import messages


def create_job(request):
    if request.user.user_type == "Producer":
        if request.method == "POST":
            job_poster_id = request.user.id
            job_title = request.POST.get('job_title')
            job_details = request.POST.get('job_details')
            job_date_time = request.POST.get('job_date_time')

    else:
        pass  # TODO will need to return an error message announcing issue
    return render(request, 'fetos_jobs/create_job.html')


def all_jobs(request):
    return render(request, 'fetos_jobs/all_jobs.html')
