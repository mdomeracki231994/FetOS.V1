# Generated by Django 5.0.7 on 2024-07-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0014_alter_appuser_is_active_alter_appuser_is_producer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]