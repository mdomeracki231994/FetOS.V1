from django.db import models

from AppUser.models import AppUser


class Talent(models.Model):
    SEX = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('trans_female', 'Trans Female'),
        ('trans_male', 'Trans Male'),
        ('non_binary', 'Non-Binary'),
    )
    sex = models.CharField(max_length=20, choices=SEX, default=None)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100)
