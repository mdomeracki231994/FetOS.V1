from django.db import models

from AppUser.models import AppUser


class Talent(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100)
