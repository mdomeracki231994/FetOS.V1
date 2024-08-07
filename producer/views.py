from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from AppUser.models import AppUser, UserAddress, SocialMediaAccounts
from fetos_jobs.models import FetosJob
from producer.models import Producer, ProducerStore


@login_required
def create_producer(request):
    user = get_object_or_404(AppUser, pk=request.user.user_id)
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        birthday = request.POST.get('birthday')
        sex = request.POST.get('sex')
        stage_name = request.POST.get('stage-name')
        store_name = request.POST.get('store-name')
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

        store, created = ProducerStore.objects.get_or_create(producer=producer)
        store.store_name = store_name

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
        return redirect('producer_profile')

    sex = AppUser.SEX_CHOICES
    first_name = request.user.first_name
    context = {
        'sex': sex,
        'first_name': first_name,
    }
    return render(request, 'Producer/CreateProducer.html', context)


def update_producer(request):
    user = request.user
    producer = get_object_or_404(Producer, user=user)
    if request.method == "POST":
        stage_name = request.POST.get('stage_name')
        producer_bio = request.POST.get('producer_bio')
        is_hiring = request.POST.get('is_hiring')

        producer.stage_name = stage_name
        if is_hiring:
            producer.is_hiring = True
        else:
            producer.is_hiring = False
        producer.producer_bio = producer_bio
        producer.save()

    context = {
        'producer_bio': producer.producer_bio if producer.producer_bio else "No Bio Provided",
        'stage_name': producer.stage_name,
        'is_hiring': producer.is_hiring,
    }
    return render(request, 'Producer/update_producer.html', context)


def producer_dashboard_page(request):
    jobs = FetosJob.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'Producer/producer_dashboard.html', context)


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
