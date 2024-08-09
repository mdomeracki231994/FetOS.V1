from django.shortcuts import render

from fetos_events.models import Events
from fetos_jobs.models import FetosJob


def calendar_page(request):
    fet_os_events = Events.objects.all()
    fet_os_jobs = FetosJob.objects.all()

    context = {
        'fet_os_events': fet_os_events,
        'fet_os_jobs': fet_os_jobs,
    }
    return render(request, 'fet_os_calendar/my_calendar.html', context)
