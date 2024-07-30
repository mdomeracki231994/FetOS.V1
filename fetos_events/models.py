from django.db import models

from producer.models import Producer


class EventLocation(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state} {self.zip_code}"


class Events(models.Model):
    title = models.CharField(max_length=200)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="events")
    description = models.TextField()
    event_date_time = models.DateTimeField()
    location = models.ForeignKey(EventLocation, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
