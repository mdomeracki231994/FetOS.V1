# Generated by Django 5.0.6 on 2024-06-20 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetos_jobs', '0005_alter_fetosjob_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='CategoriesRef',
        ),
    ]
