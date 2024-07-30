# forms.py
from django import forms

from .models import Events, EventLocation


class EventForm(forms.ModelForm):
    address_line_1 = forms.CharField(max_length=255, required=True)
    address_line_2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Events
        fields = ['title', 'description', 'event_date_time']

    def save(self, commit=True, producer=None):
        event = super().save(commit=False)
        location = EventLocation(
            address_line_1=self.cleaned_data['address_line_1'],
            address_line_2=self.cleaned_data['address_line_2'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            zip_code=self.cleaned_data['zip_code']
        )
        if commit:
            location.save()
            event.location = location
            if producer:
                event.producer = producer
            event.save()
        return event
