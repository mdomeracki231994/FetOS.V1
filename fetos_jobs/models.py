from django.db import models

from AppUser.models import AppUser


class Categories(models.Model):
    title = models.CharField(max_length=255, default=None, null=True)
    description = models.TextField(default=None, null=True)


class FetosJob(models.Model):
    LEVEL_OF_NUDITY = (
        ('clothed', 'Clothed'),
        ('topless', 'Topless'),
        ('nude', 'Nude'),
        ('explicit', 'Explicit'),
    )
    SEX_CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('trans_male', 'Trans Male'),
        ('trans_female', 'Trans Female'),
        ('non_binary', 'Non-Binary'),
    )
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    producer = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    job_date_time = models.DateTimeField()
    job_description = models.CharField(max_length=155)
    level_of_nudity = models.CharField(max_length=15, choices=LEVEL_OF_NUDITY, default=None)
    # TODO Need to think through how we will recored location
    number_of_talent_needed = models.PositiveIntegerField(default=1)
    sex_needed = models.CharField(max_length=15, choices=SEX_CHOICES, default=None)
    is_public = models.BooleanField(default=False)
