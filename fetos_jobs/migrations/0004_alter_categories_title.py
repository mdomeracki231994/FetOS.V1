# Generated by Django 5.0.6 on 2024-06-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetos_jobs', '0003_alter_categories_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]