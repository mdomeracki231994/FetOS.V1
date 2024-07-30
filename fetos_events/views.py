from django.shortcuts import render, redirect, get_object_or_404

from producer.models import Producer
from .forms import EventForm
from .models import Events


# TODO Will be allowed to see as a talent user.
def events_page(request):
    return render(request, 'fetos_events/events_page.html')


#  FIXME need to gate anyone who is not a producer.
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            producer = Producer.objects.get(user=request.user)
            form.save(producer=producer)
            return redirect('producers_events_page')
    else:
        form = EventForm()
    return render(request, 'fetos_events/create_event.html', {'form': form})


def producer_events_page(request):
    producer = get_object_or_404(Producer, user=request.user)
    events = Events.objects.filter(producer=producer)
    context = {
        'events': events,
    }
    return render(request, 'fetos_events/producers_event_page.html', context)
