# Generated by Django 4.2.2 on 2023-06-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_candidate_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='highestedu',
            new_name='highest_education',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='jobcategory',
            new_name='job_category',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='jobdescription',
            new_name='job_description',
        ),
    ]
