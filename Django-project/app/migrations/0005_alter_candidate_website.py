# Generated by Django 4.2.2 on 2023-06-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_candidate_max_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='website',
            field=models.CharField(max_length=50),
        ),
    ]
