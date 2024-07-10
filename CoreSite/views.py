from django.shortcuts import render, redirect

from AppUser.models import AppUser


def home_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
