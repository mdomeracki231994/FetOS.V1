# Generated by Django 5.0.6 on 2024-05-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0002_producer_is_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='is_hiring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producer',
            name='stage_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='producer',
            name='store',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
