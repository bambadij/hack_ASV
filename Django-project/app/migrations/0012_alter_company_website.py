# Generated by Django 4.2.2 on 2023-06-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_highestedu_candidate_highest_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=150),
        ),
    ]
