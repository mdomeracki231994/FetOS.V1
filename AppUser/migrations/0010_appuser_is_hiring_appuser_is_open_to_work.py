# Generated by Django 5.0.6 on 2024-07-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0009_appuser_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_hiring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_open_to_work',
            field=models.BooleanField(default=False),
        ),
    ]
