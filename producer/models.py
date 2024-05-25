from django.db import models

from AppUser.models import AppUser


class Producer(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    store = models.CharField(max_length=50)  # TODO This will be an FK to store table
    is_pro = models.BooleanField(default=False)

