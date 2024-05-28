from django.db import models

from AppUser.models import AppUser


class Producer(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    store = models.CharField(max_length=50, default=None, null=True)  # TODO This will be an FK to store table
    stage_name = models.CharField(max_length=100, default=None, null=True)
    is_pro = models.BooleanField(default=False)
    is_hiring = models.BooleanField(default=False)


