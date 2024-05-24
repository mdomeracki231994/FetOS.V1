from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect

from AppUser.models import AppUser


def register_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        user_type = request.POST.get('user_type')

        if password != password2:
            pass  # TODO Need to flash a message.
        get_user_model().objects.create_user(
            email=email,
            password=password,
            user_type=user_type,
            is_active=True,
        )
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    user_type_choices = AppUser.USER_TYPE_CHOICES
    return render(request, 'Auth/Register.html', {'user_type_choices': user_type_choices})


def login_user(request):
    if request.method == "POST":
        pass
    return render(request, 'Auth/Login.html')
