# Generated by Django 4.2.2 on 2023-07-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rename_companywebsite_jobdetails_website_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='experience',
            field=models.IntegerField(unique=True),
        ),
    ]
