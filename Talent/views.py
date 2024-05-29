from django.shortcuts import render

from AppUser.models import AppUser
from Talent.models import Talent


def create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        user_permissions = request.POST.get('user-permissions')
        email_status = request.POST.get('email-status')
        job_title = request.POST.get('job-title')
        user_role = request.POST.get('user-role')
        account = request.POST.get('account')
        biography = request.POST.get('biography')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip')
        timezone = request.POST.get('timezone')
        phone_number = request.POST.get('phone-number')
        linkedin_url = request.POST.get('linkedin')
        facebook_url = request.POST.get('facebook')
        github_url = request.POST.get('github')
        dribbble_url = request.POST.get('dribbble')
        instagram_url = request.POST.get('instagram')
        personal_website = request.POST.get('personal-website')
    sex = AppUser.SEX_CHOICES
    user_type = AppUser.USER_TYPE_CHOICES
    context = {
        'sex': sex,
        'user_type': user_type,
    }

    return render(request, 'Talent/CreateTalent.html', context)
