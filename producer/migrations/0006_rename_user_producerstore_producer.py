# Generated by Django 5.0.6 on 2024-07-23 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0005_remove_producer_store_producerstore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producerstore',
            old_name='user',
            new_name='producer',
        ),
    ]