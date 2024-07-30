# Generated by Django 5.0.7 on 2024-07-29 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetos_events', '0001_initial'),
        ('producer', '0007_producer_producer_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='producer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='producer.producer'),
            preserve_default=False,
        ),
    ]
