from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from fetos_jobs.models import CategoriesRef, FetosJob


def create_job(request):
    if request.user.is_anonymous:
        return redirect("login")
    if request.user.user_type == "Producer":
        if request.method == "POST":
            job_title = request.POST.get('job_title')
            job_date_time = request.POST.get('job_date_time')
            selected_fetos_categories = request.POST.get('selected_categories')
            level_of_nudity = request.POST.get('level_of_nudity')
            pay_structure = request.POST.get('pay_structure')
            travel_options = request.POST.get('travel_options')
            travel_stipend_amount = request.POST.get('travel_stipend_amount')
            description = request.POST.get('description')
            model_options = request.POST.get('model_options')

            job = FetosJob(
                producer=request.user,
                title=job_title,
                categories=selected_fetos_categories,
                job_date_time=job_date_time,
                job_description=description,
                level_of_nudity=level_of_nudity,
                pay_structure=pay_structure,
                travel_options=travel_options,
                travel_stipend_amount=travel_stipend_amount,
                model_options=model_options,
                number_of_talent_needed=1,  # Update as necessary
                sex_needed=model_options,  # Update as necessary
                is_public=False  # Update as necessary
            )
            job.save()
            return redirect('job_create_success')

    else:
        pass  # TODO will need to return an error message announcing issue
    fetos_job_categories = CategoriesRef.objects.all()
    level_of_nudity = FetosJob.LEVEL_OF_NUDITY
    pay_structure = FetosJob.PAY_STRUCTURE
    travel_options = FetosJob.TRAVEL_OPTIONS

    context = {
        "fetos_job_categories": fetos_job_categories,
        'level_of_nudity': level_of_nudity,
        'pay_structure': pay_structure,
        'travel_options': travel_options,
    }
    return render(request, 'fetos_jobs/create_job.html', context)


def create_success(request):
    return render(request, 'fetos_jobs/success_page.html')


def all_jobs(request):
    return render(request, 'fetos_jobs/job_board.html')
