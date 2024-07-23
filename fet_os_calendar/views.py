from django.shortcuts import render


def calendar_page(request):
    return render(request, 'fet_os_calendar/calendar.html')
