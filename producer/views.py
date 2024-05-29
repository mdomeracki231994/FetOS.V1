from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from AppUser.models import AppUser, UserAddress, SocialMediaAccounts
from producer.models import Producer


@login_required
def create_producer(request):
    user = get_object_or_404(AppUser, pk=request.user.user_id)
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        birthday = request.POST.get('birthday')
        sex = request.POST.get('sex')
        stage_name = request.POST.get('stage-name')
        phone_number = request.POST.get('phone-number')
        biography = request.POST.get('biography')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address_line_one = request.POST.get('address')
        zip_code = request.POST.get('zip')

        user.first_name = first_name
        user.last_name = last_name
        user.date_of_birth = birthday
        user.sex = sex
        user.phone_number = phone_number
        user.user_bio = biography
        user.is_active = True
        user.save()

        producer, created = Producer.objects.get_or_create(user=user)
        producer.stage_name = stage_name

        address, created = UserAddress.objects.get_or_create(user=user)
        address.address_line_one = address_line_one
        address.city = city
        address.state = state
        address.zip = zip_code
        address.save()

        social_media_accounts = {
            'Twitter': request.POST.get('twitter'),
            'TickTok': request.POST.get('ticktok'),
            'Bluesky': request.POST.get('github'),
            'YouTube': request.POST.get('youtube'),
            'Instagram': request.POST.get('instagram'),
        }

        for account_title, url in social_media_accounts.items():
            if url:
                social_media_account, created = SocialMediaAccounts.objects.get_or_create(
                    user=user,
                    account_title=account_title,
                )
                social_media_account.url = url
                social_media_account.save()

    sex = AppUser.SEX_CHOICES
    first_name = request.user.first_name
    context = {
        'sex': sex,
        'first_name': first_name,
    }
    return render(request, 'Producer/CreateProducer.html', context)


@login_required
def producer_profile_page(request):
    user = request.user
    producer = get_object_or_404(Producer, user=user)
    address = get_object_or_404(UserAddress, user=user)

    context = {
        'producer': producer,
        'address': address,
        'social_media_accounts': user.socialmediaaccounts_set.all()
    }
    return render(request, 'Producer/ProfilePage.html', context)
