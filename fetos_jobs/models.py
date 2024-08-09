from django.db import models

from AppUser.models import AppUser


class CategoriesRef(models.Model):
    title = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return f'{self.title}'


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
    PAY_STRUCTURE = (
        ('per_hour', 'Per Hour'),
        ('per_finished_minute', 'Per Finished Minute'),
        ('per_video', 'Per Video'),
        ('day_rate', 'Day Rate'),
    )
    TRAVEL_OPTIONS = (
        ('flight', 'Flight'),
        ('flight_and_lodging', 'Flight & Lodging'),
        ('travel_stipend', 'Travel Stipend'),
    )

    producer = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    categories = models.JSONField()
    job_date_time = models.DateTimeField(default=None, null=True)
    level_of_nudity = models.CharField(max_length=50, choices=LEVEL_OF_NUDITY, default=None)
    # TODO Need to think through how we will recorded location
    pay_structure = models.CharField(max_length=50, choices=PAY_STRUCTURE, default=None)
    travel_options = models.CharField(max_length=50, choices=TRAVEL_OPTIONS, default=None)
    travel_stipend_amount = models.IntegerField(default=None)
    number_of_talent_needed = models.PositiveIntegerField(default=1)
    sex_needed = models.CharField(max_length=50, choices=SEX_CHOICES, default=None)
    is_public = models.BooleanField(default=False)
    job_description = models.TextField(default=None, null=True)
    model_options = models.TextField(default=None, null=True)

    def __str__(self):
        return f'{self.title}'


class AppliedToJob(models.Model):
    job = models.ForeignKey(FetosJob, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
