# Generated by Django 4.2.2 on 2023-06-24 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_candidate_experience_candidate_highestedu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='max_salary',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='min_salary',
        ),
    ]
