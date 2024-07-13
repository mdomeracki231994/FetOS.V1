# Generated by Django 5.0.6 on 2024-07-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0012_remove_appuser_user_type_appuser_is_producer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='is_verified',
            new_name='is_verified_as_producer',
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_verified_as_talent',
            field=models.BooleanField(default=False),
        ),
    ]
