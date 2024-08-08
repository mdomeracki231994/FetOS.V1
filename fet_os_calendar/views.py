from django.shortcuts import render

from fetos_events.models import Events


def calendar_page(request):
    fet_os_events = Events.objects.all()
    print(fet_os_events.values())

    context = {
        'fet_os_events': fet_os_events,

    }
    return render(request, 'fet_os_calendar/my_calendar.html', context)
