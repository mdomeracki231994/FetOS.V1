# Generated by Django 5.0.6 on 2024-05-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0002_appuser_is_active_appuser_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='user_type',
            field=models.CharField(choices=[('producer', 'Producer'), ('talent', 'Talent')], default=None, max_length=10),
        ),
    ]
