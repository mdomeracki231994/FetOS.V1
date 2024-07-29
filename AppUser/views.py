from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from AppUser.models import AppUser


def register_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        user_type = request.POST.get('user_type')
        is_talent = False
        is_producer = False
        if user_type == 'talent':
            is_talent = True
        elif user_type == 'producer':
            is_producer = True
        elif user_type == 'talent_and_producer':
            is_talent = True
            is_producer = True

        if password != password2:
            print("Passwords do not match")
            pass  # TODO Need to flash a message.
        get_user_model().objects.create_user(
            email=email,
            password=password,
            is_active=True,
            is_talent=is_talent,
            is_producer=is_producer
        )
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        if request.user.is_superuser:
            return redirect('dashboard')
        elif request.user.is_talent and request.user.is_producer:
            return redirect('create_producer')
        elif request.user.is_talent:
            return redirect('create_talent')
        elif request.user.is_producer:
            return redirect('create_producer')
    return render(request, 'Auth/Register.html')


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user=user)
            if AppUser.first_name is None:
                return redirect('producer_profile')
            return redirect('home')
        else:
            print('User Does not exist')  # TODO We need to flash message
    return render(request, 'Auth/Login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
