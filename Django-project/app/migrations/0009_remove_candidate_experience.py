# Generated by Django 4.2.2 on 2023-06-24 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_candidate_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='experience',
        ),
    ]
