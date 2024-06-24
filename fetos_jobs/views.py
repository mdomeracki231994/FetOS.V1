from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from fetos_jobs.models import CategoriesRef


def create_job(request):
    if request.user.is_anonymous:
        return redirect("login")
    if request.user.user_type == "Producer":
        if request.method == "POST":
            job_title = request.POST.get('job_title')
            job_details = request.POST.get('job_details')
            job_date_time = request.POST.get('job_date_time')
            selected_categories = request.POST.get('selected_categories')


    else:
        pass  # TODO will need to return an error message announcing issue
    fetos_job_categories = CategoriesRef.objects.all()

    context = {
        "fetos_job_categories": fetos_job_categories,
    }
    return render(request, 'fetos_jobs/create_job.html', context)


def all_jobs(request):
    return render(request, 'fetos_jobs/all_jobs.html')
