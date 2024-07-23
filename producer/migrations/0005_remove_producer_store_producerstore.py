# Generated by Django 5.0.6 on 2024-07-23 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0004_alter_producer_stage_name_alter_producer_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producer',
            name='store',
        ),
        migrations.CreateModel(
            name='ProducerStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producer.producer')),
            ],
        ),
    ]