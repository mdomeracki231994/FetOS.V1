from django.shortcuts import render


def events_page(request):
    return render(request, 'fetos_events/events_page.html')
