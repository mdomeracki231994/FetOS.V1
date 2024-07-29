from django.db import models

from AppUser.models import AppUser


class Producer(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100, default=None, null=True)
    producer_bio = models.TextField(null=True, blank=True)
    is_pro = models.BooleanField(default=False)
    is_hiring = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class ProducerStore(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)

    # TODO Will need to record store location.
    def __str__(self):
        return f'{self.producer} {self.store_name}'
